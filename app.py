from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import reporting_methods
import plotly.express as px
import streamlit as st
import pandas as pd
import prompts
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage, SystemMessage,
)
from typing import Union

load_dotenv()

language_column_map = {"English": "en", "French": "fr", "German": "de"}

def use_model(**kwargs) -> Union[ChatOpenAI, str]:
    """
    Initializes and returns a ChatOpenAI model instance based on the provided keyword arguments.

    Parameters
    ----------
    **kwargs : dict
        Keyword arguments to configure the ChatOpenAI model. Must include a 'name' key with the value 'openai'.

    Returns
    -------
    ChatOpenAI
        An instance of the ChatOpenAI model if 'name' is 'openai'.
    str
        A message indicating no model was found if 'name' is not 'openai'.
    """
    if kwargs.get('name') == 'openai':
        kwargs.pop('name')
        return ChatOpenAI(**kwargs)
    else:
        return "No model found"

def use_labels(label: str, language: str = None) -> str:
    if language is None:
        language = st.session_state['language']
    return prompts.labels[label][language]

def generate_reports(state, code_groups, material_spec, data):
    """Generate reports based on the selected state, code groups, material spec, and data"""
    reports = []

    if len(state['canton']) > 0:
        for location in state['canton']:
            meta = reporting_methods.translate_state_to_meta(state, code_groups, location, "canton")
            report = reporting_methods.baseline_report_and_data(meta, data, material_spec)
            reports.append(report)

    if len(state['city']) > 0:
        for location in state['city']:
            meta = reporting_methods.translate_state_to_meta(state, code_groups, location, "city")
            report = reporting_methods.baseline_report_and_data(meta, data, code_material)
            reports.append(report)

    if len(state['feature_name']) > 0:
        for location in state['feature_name']:
            meta = reporting_methods.translate_state_to_meta(state, code_groups, location, None)
            report = reporting_methods.baseline_report_and_data(meta, data, code_material)
            reports.append(report)

    return "\n".join(reports)

def map_markers(f_data, map_coords):
    """Map the markers"""

    nsamples = f_data.groupby('location', observed=True)['sample_id'].nunique()
    qty_location = f_data.groupby('location', observed=True)['quantity'].sum()
    rate_location = f_data.groupby('location', observed=True)['pcs/m'].mean().round(2)
    last_sample = f_data.groupby('location', observed=True)['date'].max()

    # merge the pop-up information with the gps coordinates
    df = pd.concat([nsamples, qty_location, rate_location, last_sample], axis=1)
    df = df.merge(map_coords[['longitude', 'latitude']], left_index=True, right_index=True)
    df['location'] = df.index
    df.rename(columns={'sample_id': 'nsamples', 'date': 'last sample'}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def scatter_map(f_data, map_coords):
    """
    Generates a map with markers using Plotly's scatter_map.
    - Markers use lat/lon from map_markers.
    - Hover information includes samples, quantity, pcs/m, and last sample date.
    """
    # Call your map_markers function to get the processed data
    df = map_markers(f_data, map_coords)
    print("Making map markers\n")
    print(f"Map marker columns: {', '.join(df.columns)}")

    fig = px.scatter_map(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="location",
        hover_data=['quantity', 'nsamples', 'pcs/m', 'last sample'],
        zoom=8,
        height=500
    )
    fig.update_traces(marker={'size': 10, 'symbol': 'cross'})

    fig.update_layout(
        map_style="white-bg",
        map_layers=[
            {
                "below": "traces",
                "sourcetype": "raster",
                "sourceattribution": "© swisstopo",
                "opacity": 0.4,
                "source": [
                    "https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg"
                ]
            }
        ],
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    return fig, df

def apply_filters():
    """
    Updates `f_data` based on the current selections in session state.
    Uses OR logic for each selection and dynamically narrows down options.
    """
    print("Applying filters\n")
    s_data = st.session_state["survey_data"]  # Original unfiltered data
    f_data = s_data.copy()
    params = st.session_state['selected_parameters']

    # Step 1: Filter by Canton
    s_cantons = params["canton"]
    if s_cantons:
        f_data = f_data[f_data["canton"].isin(params['canton'])]

    # Step 2: Filter by City
    s_cities = params["city"]
    if s_cities:
        f_data = f_data[f_data["city"].isin(params['city'])]

    # Step 3: Filter by Feature Name
    s_feature_names = params["feature_name"]
    if s_feature_names:
        f_data = f_data[f_data["feature_name"].isin(s_feature_names)]

    # Step 4: Filter by Feature Type
    f_type = params["feature_type"]
    if f_type != "both":
        feature_code = "l" if f_type == "lake" else "r"
        f_data = f_data[f_data["feature_type"] == feature_code]
    s_codes = params['selected_objects']
    if s_codes:
        f_data = f_data[f_data['code'].isin(params['selected_objects'])]
    date_range = st.session_state["date_range"]
    if date_range:
        mask = (f_data['date'] >= pd.Timestamp(date_range[0])) & (f_data['date'] <= pd.Timestamp(date_range[1]))
        f_data = f_data[mask]
    # Update session state with the filtered data
    st.session_state["filtered_data"] = f_data.reset_index(drop=True)

def clear_filters(data_from_cache):
    """Clear all filters and reinitialize session state."""
    # Clear all session state variables
    st.session_state.clear()

    # Reinitialize the session state
    initialize_session_state(data_from_cache)
    # st.session_state.clear()
    # initialize_session_state(data_from_cache)

def update_date_range(f_data):
    """
    Updates the min and max date range based on the filtered data.
    Ensures all dates are consistently `datetime.date` objects.
    """
    # Calculate the min and max dates as datetime.date
    min_d = f_data["date"].min()
    max_d = f_data["date"].max()

    # Ensure date_range exists in session state
    if "date_range" not in st.session_state or len(st.session_state["date_range"]) != 2:
        st.session_state["date_range"] = (min_d, max_d)

    # Extract start_date and end_date from session state
    start_d, end_d = st.session_state["date_range"]

    # Convert to datetime.date if they are Timestamps
    if isinstance(start_d, pd.Timestamp):
        pass
    else:
        start_d = pd.to_datetime(start_d)
    if isinstance(end_d, pd.Timestamp):
        pass
    else:
        end_d = pd.to_datetime(end_d)

    # Clamp the start_date and end_date to the min and max dates
    start_d = max(min_d, min(start_d, max_d))
    end_d = max(min_d, min(end_d, max_d))

    # Update session state with the clamped values
    st.session_state["date_range"] = (start_d, end_d)

    return start_d, end_d

def scatterplot_caption(data, color_by, selected_language, llm):
    """
    Generates a caption for the scatter plot based on the filtered data and the color_by parameter.
    """
    d = data.groupby(['sample_id', 'date', color_by], as_index=False)["pcs/m"].sum()
    grouped_data_mean = d.groupby([color_by], as_index=False)["pcs/m"].mean()
    grouped_data_mean = grouped_data_mean.sort_values(by="pcs/m", ascending=False)
    s_date, e_date = data.date.min().date(), data.date.max().date()
    ysummary = d["pcs/m"].describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95])
    print(data.columns)

    d_column = language_column_map[st.session_state["language"]]
    s_objects = data[d_column].unique()
    s_objects = ', '.join(s_objects)
    s_cantons = data['canton'].unique()
    s_feature_type = data['feature_type'].unique()
    if len(s_feature_type) > 1:
        s_feature_type = "both"
    else:
        if s_feature_type[0] == 'l':
            s_feature_type = "lake"
        else:
            s_feature_type = "river"
    querry = prompts.scatterplot_prompt(s_date, e_date, ysummary, grouped_data_mean, s_objects, color_by, s_feature_type, s_cantons, selected_language)
    scatterplot_message = [
        SystemMessage("follow the users instructions"),
        HumanMessage(content=querry)
    ]

    return llm.stream(scatterplot_message)

def scatterplot(data, s_language, s_labels, color_by):
    """
    Creates a scatter plot.
    - x-axis: date
    - y-axis: pcs/m
    - color: Selected feature (canton, city, or feature_name)
    """
    new_data = data.groupby(['sample_id', color_by, 'date'], as_index=False)['pcs/m'].sum()
    fig = px.scatter(
        new_data,
        x="date",
        y="pcs/m",
        color=color_by,
        labels={"date": "", "pcs/m": prompts.labels["pieces_per_meter"][s_language]},
    )

    fig.update_traces(
        marker=dict(
            symbol="x",
            size=8,
            line=dict(width=0.5, color="white"),
        ),
        selector=dict(mode='markers')
    )
    fig.update_layout(
        margin=dict(l=60, r=60, t=80, b=60),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(size=12),
        legend=dict(
            title="Legend",
            x=1.02,
            y=1,
            xanchor="left",
        )
    )
    fig.update_xaxes(showgrid=True, gridwidth=.25, gridcolor='rgba(47, 79, 79, 0.5)')
    fig.update_yaxes(showgrid=True, gridwidth=.25, gridcolor='rgba(47, 79, 79, 0.5)')
    return fig

def handle_grouped_data_for_barchart(data: pd.DataFrame, x_axis: str, y_axis: str) -> pd.DataFrame:
    """Aggregates data for a barchart according to user requests and data type"""
    print('Handling grouped data\n')

    description_column = language_column_map[st.session_state["language"]]

    if x_axis == 'object':
        x_axis = description_column
    if y_axis == "number of samples":
        grouped_data = data.groupby(x_axis, as_index=False)['sample_id'].nunique()
        grouped_data[y_axis] = grouped_data['sample_id']
        grouped_data.drop('sample_id', axis=1, inplace=True)
        grouped_data = grouped_data.sort_values(by=y_axis, ascending=False)
    if y_axis == "quantity":
        grouped_data = data.groupby(x_axis)[y_axis].sum().reset_index()
        grouped_data = grouped_data.sort_values(by=y_axis, ascending=False)
    if y_axis == "pcs/m":
        grouped_data = data.groupby(['sample_id', x_axis], as_index=False)[y_axis].sum()
        grouped_data = grouped_data.groupby(x_axis, as_index=False)[y_axis].mean().reset_index()
        grouped_data = grouped_data.sort_values(by=y_axis, ascending=False)

    return grouped_data

def barchart_caption(data, x_axis, y_axis, s_language, llm):
    """Creates a narrative for a barchart given the data and the x and y axis labels"""
    grouped_data = handle_grouped_data_for_barchart(data, x_axis, y_axis)
    querry = prompts.barchart_prompt(data, grouped_data, x_axis, y_axis, s_language)
    barchart_message = [
        SystemMessage("follow the users instructions"),
        HumanMessage(content=querry)
    ]

    aresponse = llm.stream(barchart_message)

    return aresponse

def barchart(data, x_axis, y_axis):
    """
    Creates a bar chart.
    - x-axis: one of the following ["canton", "city", "feature_name", "object"]
    - y-axis: one of the following ["quantity", "pcs/m", "number of samples"]
    """

    grouped_data = handle_grouped_data_for_barchart(data, x_axis, y_axis)
    if x_axis == "object":
        # we are using the plain language description of the object
        language_column_map = {"English": "en", "French": "fr", "German": "de"}
        description_column = language_column_map[st.session_state["language"]]
        x_axis = description_column

    fig = px.bar(
        grouped_data,
        x=x_axis,
        y=y_axis,
        labels={x_axis: " ", y_axis: prompts.labels[y_axis][st.session_state["language"]]},
        color=x_axis,
    )
    fig.update_layout(
        margin=dict(l=60, r=60, t=80, b=60),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(size=12),
        legend=dict(
            title="Legend",
            x=1.05,
            y=1,
            xanchor="left",
        )
    )
    return fig

def apply_location_filters(data, selected_parameters):
    """This applies location filters only and formats the date column"""

    if len(selected_parameters["canton"]) > 0:
        data = data[data["canton"].isin(selected_parameters["canton"])]
    if len(selected_parameters["city"]) > 0:
        data = data[data["city"].isin(selected_parameters["city"])]
    if len(selected_parameters["feature_name"]) > 0:
        data = data[data["feature_name"].isin(selected_parameters["feature_name"])]
    if selected_parameters["feature_type"] not in ['river', 'lake']:
        pass
    else:
        if selected_parameters['feature_type'] == 'lake':
            data = data[data['feature_type'] == 'l']
        else:
            data = data[data["feature_type"] == 'r']
    data['date'] = pd.to_datetime(data['date'])
    # data['date'] = data['date'].dt.date
    return data

def initialize_session_state(load_survey_data):
    """Set up initial state for session variables."""
    # Language selection
    if "language" not in st.session_state:
        st.session_state["language"] = "English"

    # Data and filtering
    if "filtered_data" not in st.session_state:
        st.session_state["filtered_data"] = None #load_survey_data()

    if "survey_data" not in st.session_state:
        st.session_state["survey_data"] = load_survey_data()

    if "date_range" not in st.session_state:
        min_d = st.session_state["survey_data"]["date"].min()
        max_d = st.session_state["survey_data"]["date"].max()
        st.session_state["date_range"] = (min_d, max_d)

    if "rough_drafts" not in st.session_state:
        st.session_state["rough_drafts"] = "No roughdrafts generated yet."

    if 'abstract' not in st.session_state:
        st.session_state['abstract'] = "No abstract generated yet."

    if 'inventory' not in st.session_state:
        st.session_state['inventory'] = "No inventory generated yet."

    if 'map_fig' not in st.session_state:
        st.session_state['map_fig'] = "No map generated yet."

    if 'map_markers' not in st.session_state:
        st.session_state['map_markers'] = "No map markers generated yet."

    if 'scatterplot_caption' not in st.session_state:
        st.session_state['scatterplot_caption'] = None

    if 'barchart_caption' not in st.session_state:
        st.session_state['barchart_caption'] = None

    if "filters_confirmed" not in st.session_state:
        st.session_state["filters_confirmed"] = False

    if "selected_parameters" not in st.session_state:
        st.session_state["selected_parameters"] = {
            "canton": [],
            "city": [],
            "feature_name": [],
            "feature_type": "both",
            "date_range": {'start': None, 'end': None},
            "selected_objects": []
        }
    if 'filtered_applied' not in st.session_state:
        st.session_state['filtered_applied'] = False

agent_intro = {
            "English": " ".join([
                "Hi, I am the report assistant.",
                "The rough draft, inventory and the text from the selected charts are loaded and available to me.",
                "This is only a demonstration, we did not hook up the RAG agent but you can consult the references here:",
                "https://hammerdirt-analyst.github.io/feb_2024/references.html."
            ]),
            "French": " ".join([
                "Bonjour, je suis l'assistant de rapport.",
                "L'ébauche, l'inventaire et le texte des graphiques sélectionnés sont chargés et à ma disposition.",
                "Ceci est seulement une démonstration, nous n'avons pas connecté l'agent RAG mais vous pouvez consulter les références ici :",
                "https://hammerdirt-analyst.github.io/feb_2024/references.html."
            ]),
            "German": " ".join([
                "Hallo, ich bin der Berichtsassistent.",
                "Der Entwurf, das Inventar und der Text aus den ausgewählten Diagrammen sind geladen und stehen mir zur Verfügung.",
                "Dies ist nur eine Demonstration, wir haben den RAG-Agenten nicht angeschlossen, aber Sie können die Referenzen hier einsehen:",
                "https://hammerdirt-analyst.github.io/feb_2024/references.html."
            ])
        }


# start app

@st.cache_data
def load_survey_data():
    a = pd.read_csv('data/end_process/before_2019.csv')
    b = pd.read_csv('data/end_process/after_2019.csv')
    c = pd.read_csv('data/end_process/after_may_2021.csv')

    land_use = pd.read_csv('data/end_process/new_lu.csv')
    data = pd.concat([a, b, c])
    t = data.merge(land_use, left_on='location', right_on='location')
    t["date"] = pd.to_datetime(t["date"])
    t.drop('city-center', axis=1, inplace=True)
    t.dropna(inplace=True)
    t.reset_index(drop=True, inplace=True)
    return t
@st.cache_data
def load_codes():
    codes = pd.read_csv("data/end_process/codes.csv")
    return codes
@st.cache_data
def beaches():
    beaches = pd.read_csv('data/end_process/beaches.csv')
    return beaches
@st.cache_data
def lat_lon():
    # beaches = pd.read_csv('data/end_process/beaches.csv')
    lat_lon = beaches()[['slug', 'latitude', 'longitude']].set_index('slug')
    return lat_lon

initialize_session_state(load_survey_data=load_survey_data)
model_args_no_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000,
                                       streaming=False)
model_args_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000)
if 'language' not in st.session_state:
    st.header("Shoreline litter assessment")
else:
    st.header(prompts.labels["shoreline_litter_assessment"][st.session_state['language']])
language = st.radio(
    "", ["English", "French", "German"], index=0, horizontal=True, key="language"
)
st.markdown(prompts.labels["intro_one"][language])
st.image("resources/goodimage.webp")
st.markdown(prompts.labels["intro_two"][language])

with st.expander(f"**{prompts.labels['whats_this'][language]}**", expanded=False):
    st.markdown(prompts.labels["intro_content"][language])

st.markdown(prompts.labels["instruction_labels"][language])

with st.expander(f"**{prompts.labels['parameter_selection'][language]}**", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f'**{prompts.labels["step_1_subheader"][language]}**')
        survey_data = st.session_state["survey_data"]

        # selected_parameters = st.session_state["selected_parameters"].copy()

        # Step 1: Select regions or features
        st.session_state['selected_parameters']["canton"] = st.multiselect(
            label=prompts.labels["canton"][language],
            options=survey_data["canton"].unique(),
            default=st.session_state['selected_parameters']["canton"],
            key="canton"
        )

        if len(st.session_state['selected_parameters']["canton"]) > 0:
            available_cities = apply_location_filters(survey_data, st.session_state['selected_parameters']).city.unique()
        else:
            available_cities = survey_data.city.unique()
        st.session_state['selected_parameters']["city"] = st.multiselect(
            label=prompts.labels["city"][language],
            options=available_cities,
            default=st.session_state['selected_parameters']["city"],
            key="city"
        )

        if len(st.session_state['selected_parameters']["city"]) > 0:
            available_feature_names = apply_location_filters(survey_data, st.session_state['selected_parameters']).feature_name.unique()
        if len(st.session_state['selected_parameters']["canton"]) > 0:
            available_feature_names = survey_data[survey_data["canton"].isin(st.session_state['selected_parameters']["canton"])]["feature_name"].unique()
        else:
            available_feature_names = survey_data["feature_name"].unique()
        st.session_state['selected_parameters']["feature_name"] = st.multiselect(
            label=prompts.labels["feature_name"][language],
            options=available_feature_names,
            default=st.session_state['selected_parameters']["feature_name"],
            key="feature_name"
        )

        available_feature_types = apply_location_filters(survey_data, st.session_state['selected_parameters']).feature_type.unique()
        if len(available_feature_types) > 1:
            available_feature_types = ["lake", "river", "both"]
        else:
            if "l" in available_feature_types:
                available_feature_types = ["lake"]
            else:
                available_feature_types = ["river"]
        st.session_state['selected_parameters']['feature_type']= st.pills(
            label=prompts.labels["select_feature_type"][language],
            options= available_feature_types,
            format_func=lambda x: prompts.labels[x][language],
            default= st.session_state['selected_parameters']["feature_type"] if st.session_state['selected_parameters']["feature_type"] in available_feature_types else None,
            key="feature_type"
        )

        st.write(f'**{prompts.labels["step_2_subheader"][language]}**')

        # Step 2: Select Date Range
        available_dates =apply_location_filters(survey_data, st.session_state['selected_parameters'])
        min_date, max_date = update_date_range(available_dates)
        start_date = st.date_input(
            label=prompts.labels["start_date"][language],
            value=min_date,
            min_value=min_date,
            max_value=max_date,
            key="start_date"
        )
        end_date = st.date_input(
            label=prompts.labels["end_date"][language],
            value=max_date,
            min_value=min_date,
            max_value=max_date,
            key="end_date"
        )
        st.session_state['selected_parameters']["date_range"] = {'start':start_date, 'end': end_date}

        # Step 3: Apply Filters and select objects
        st.markdown(f'**{prompts.labels["step_3_subheader"][language]}**')
        st.markdown(prompts.labels["filter_one_instructions"][language])

        if st.button(prompts.labels["apply_filters_button"][language], key="apply_filters_buttonx"):

            filtered_data = apply_location_filters(survey_data, st.session_state['selected_parameters'])

            date_mask = ((filtered_data["date"] >= pd.Timestamp(st.session_state['selected_parameters']["date_range"]['start'])) &
                 (filtered_data["date"] <= pd.Timestamp(st.session_state['selected_parameters']["date_range"]['end'])))

            filtered_data = filtered_data[date_mask].copy()
            st.session_state['filtered_applied'] = True

            st.session_state["filtered_data"] = filtered_data
            #st.session_state["selected_parameters"] = selected_parameters
        if st.session_state['filtered_applied']:
            st.success(prompts.labels["filters_applied_message"][language])
        # warning if no filters are applied
        if len(st.session_state['selected_parameters']['canton']) + len(st.session_state['selected_parameters']['city']) + len(st.session_state['selected_parameters']['feature_name']) == 0:
            st.info(prompts.labels['no_filter_warning'][language])
        # object Selection
        if st.session_state["filtered_data"] is not None:
            available_objects = st.session_state["filtered_data"]
            available_objects = available_objects[available_objects.quantity > 0]
            available_object_codes = available_objects["code"].unique()

            if len(available_object_codes) == 0:
                st.warning(prompts.labels["nofilters"][language])
            else:
                these_codes = load_codes()[load_codes()["code"].isin(available_object_codes)]
                description_column = {"English": "en", "French": "fr", "German": "de"}[language]
                object_descriptions = {row["code"]: row[description_column] for _, row in these_codes.iterrows()}

                selected_objects = st.multiselect(
                    label=prompts.labels["objects"][language],
                    options=list(object_descriptions.keys()),
                    format_func=lambda x: f"{x} - {object_descriptions.get(x, '')}",
                    default=st.session_state.get("selected_objects", []),
                    key="selected_objects"
                )

                st.session_state["selected_parameters"]["selected_objects"] = selected_objects
        else:
            st.warning(prompts.labels["please_apply_filters"][language])

    with col2:
        # step 4 : confirm filters
        st.markdown(f'**{prompts.labels["step_4_subheader"][language]}**')
        st.markdown(prompts.labels["confirm_filter"][language])

        # confirm filters button logic
        if st.session_state["filtered_applied"]:
            if st.button(prompts.labels["confirmfilters"][language], key="confirm_filters_button"):
                apply_filters()
                st.session_state["filters_confirmed"] = True
                st.success(prompts.labels["filters_confirmed_message"][language])
                if st.session_state["filtered_data"].quantity.sum() == 0:
                    st.warning("No data available. Please adjust filters.")
                    st.session_state["filters_applied"] = False  # Reset the flag if the data is empty
        else:
            st.warning(prompts.labels["confirm_denied"][language])

        # clear filters button logic
        if st.button(prompts.labels["clear_filters"][language], key="clear_filters_button"):
            st.session_state['filtered_applied'] = False
            clear_filters(load_survey_data)
            st.success("Filters cleared!")


        st.markdown(f'**{prompts.labels["selected_parameters_subheader"][language]}**')
        # display selected parameters
        st.json(st.session_state['selected_parameters'])

        st.markdown(f'**{prompts.labels["step_5_subheader"][language]}**')

        # Disable "make_roughdraft" button conditionally
        if not st.session_state["filters_confirmed"] or st.session_state["filtered_data"].empty:
            st.warning(prompts.labels["no_data_warning"][language])
            st.button(prompts.labels["make_roughdraft"][language], key="make_roughdraft_button", disabled=True)
        else:
            if st.button(prompts.labels["make_roughdraft"][language], key="make_roughdraft_button"):
                st.session_state["final_selected_parameters"] = st.session_state['selected_parameters']

if "language" not in st.session_state:
    st.subheader("Survey results")
else:
    st.subheader(prompts.labels["survey_results"][st.session_state['language']])

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        prompts.labels["summary"][language],
        prompts.labels["step_6_subheader"][language],
        prompts.labels["step_7_subheader"][language],
        prompts.labels["inventory"][language],
        prompts.labels["rough_draft"][language],
        prompts.labels['map_markers'][language]]
)

with tab1:
    if "final_selected_parameters" in st.session_state:

        if st.session_state["abstract"] == "No abstract generated yet.":
            current_llm = use_model(**model_args_no_streaming)
            code_use = load_codes()[['code', 'groupname']].set_index('code')
            code_material = load_codes()[['code', 'material']].set_index('code')
            st.json(st.session_state["selected_parameters"])
            st.session_state["rough_drafts"] = generate_reports(st.session_state["selected_parameters"], code_use, code_material, st.session_state['filtered_data'])
            chart_data = st.session_state.get("filtered_data", pd.DataFrame())
            description_column = language_column_map[st.session_state["language"]]
            objects = chart_data[description_column].unique()
            objects = ', '.join(objects)
            cantons = chart_data['canton'].unique()
            feature_type = chart_data['feature_type'].unique()
            if len(feature_type) > 1:
                feature_type = "both"
            elif feature_type[0] == 'l':
                    feature_type = "lake"
            else:
                feature_type = "river"

            abstract_message = [
                SystemMessage(prompts.abstract_prompt(st.session_state['language'], feature_type, objects, cantons)),
                HumanMessage(content=st.session_state['rough_drafts'])
            ]


            an_absract = current_llm.stream(abstract_message)
            abstract = st.write_stream(an_absract)
            st.session_state['abstract'] = abstract
        else:
            st.markdown(st.session_state['abstract'])

        config = {
            "displayModeBar": True,
            "toImageButtonOptions": {
                "format": "png",
                "filename": "custom_plot",
                "height": 800,
                "width": 1200,
                "scale": 2,
            },
        }
        if st.session_state["map_fig"] == "No map generated yet.":
            chart_data = st.session_state.get("filtered_data", pd.DataFrame())

            map_fig, map_markers = scatter_map(chart_data, lat_lon())
            st.session_state["map_fig"] = map_fig
            st.session_state["map_markers"] = map_markers
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
        else:
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
            chart_data = st.session_state.get("filtered_data", pd.DataFrame())
    else:
        st.warning(prompts.labels["no_rough_draft_message"][language])
        chart_data = pd.DataFrame()

with tab2:
    if not chart_data.empty:
        current_llm = use_model(**model_args_streaming)

        scatter_color_by = st.selectbox(
            label=prompts.labels["color_markers_by"][language],
            options = ['canton', 'city', 'feature_name'],
            format_func=use_labels,
            key="scatter_color_by"
        )

        scatter_fig = scatterplot(chart_data, st.session_state['language'], prompts.labels, scatter_color_by)
        st.plotly_chart(scatter_fig, use_container_width=True, config=config)

        if "scatterplot_previous_color_by" not in st.session_state:
            st.session_state["scatterplot_previous_color_by"] = None
        if "scatterplot_caption" not in st.session_state:
            st.session_state["scatterplot_caption"] = None

        if st.session_state["scatterplot_previous_color_by"] != scatter_color_by:
            st.session_state["scatterplot_caption"] = None
            st.session_state["scatterplot_previous_color_by"] = scatter_color_by

        if st.session_state["scatterplot_caption"] is not None:
            st.write(st.session_state["scatterplot_caption"])
        else:
            if st.button(prompts.labels["explain_graphic"][st.session_state["language"]], key="scatterplot_caption_button"):
                l = st.session_state['language']
                explanation = scatterplot_caption(chart_data, scatter_color_by, l, current_llm)
                scatter_plot_caption = st.write_stream(explanation)
                st.session_state["scatterplot_caption"] = scatter_plot_caption
    else:
       st.warning(prompts.labels["no_rough_draft_message"][language])

with tab3:
    if not chart_data.empty:
        print('in bar chart\n')
        print(f"The chart data columns are: {chart_data.columns}\n")
        x_axis = st.selectbox(
            label="X-Axis",
            options=["canton", "city", "feature_name", "object"],
            format_func=use_labels,
            key="bar_x_axis")
        y_axis = st.selectbox(
            label="Y-Axis",
            options=["quantity", "pcs/m", "number of samples"],
            format_func=use_labels,
            key="bar_y_axis")
        barchart_color_by = x_axis
        bar_fig = barchart(chart_data, x_axis, y_axis)
        st.plotly_chart(bar_fig, use_container_width=True, config=config)

        if "barchart_previous_color_by" not in st.session_state or st.session_state["barchart_previous_color_by"] != barchart_color_by :
            st.session_state["barchart_caption"] = None
            st.session_state["barchart_previous_color_by"] = barchart_color_by

        if "barchart_previous_y" not in st.session_state or st.session_state["barchart_previous_y"] != y_axis:
            st.session_state["barchart_caption"] = None
            st.session_state["barchart_previous_y"] = y_axis

        if st.session_state["barchart_caption"] is not None:
            st.write(st.session_state["barchart_caption"])
        else:
            if st.button(prompts.labels["explain_graphic"][st.session_state["language"]], key="barchart_caption_button"):
                l = st.session_state['language']
                explanation = barchart_caption(chart_data,x_axis, y_axis, l, current_llm)
                bar_chart_caption = st.write_stream(explanation)

                st.session_state["barchart_caption"] = bar_chart_caption
    else:
        st.warning(prompts.labels["no_rough_draft_message"][language])

with tab4:
    if not chart_data.empty:
        s = reporting_methods.SurveyReport(chart_data)
        adict = s.object_summary()
        inv = adict[0]['dataframe']
        print(st.session_state['language'])
        inv.rename(columns={'sample_id': 'number of samples'}, inplace=True)
        if st.session_state['language'] != 'English':
            column_translations = prompts.translate_columns(st.session_state['language'])
            inv.rename(columns=column_translations, inplace=True)
        # inv = inv.style.set_table_styles(reporting_methods.table_css_styles).format(**reporting_methods.format_kwargs)
        st.session_state["inventory"] = reporting_methods.extract_roughdraft_text(adict)
        st.dataframe(inv.style.set_table_styles(reporting_methods.table_css_styles).format(**reporting_methods.format_kwargs))
    else:
        st.warning(prompts.labels["no_rough_draft_message"][language])

with tab5:
    if "final_selected_parameters" in st.session_state:
        st.write(st.session_state["rough_drafts"])
    else:
        st.warning(prompts.labels["no_rough_draft_message"][language])

with tab6:
    if isinstance(st.session_state.map_markers, (str, )):
        st.warning("No map markers generated yet.")
    else:
        st.dataframe(st.session_state["map_markers"])

if 'language' not in st.session_state:
    st.subheader("Discussion")
else:
    st.subheader(prompts.labels["discussion"][st.session_state['language']])

if "final_selected_parameters" in st.session_state:

    if st.session_state["barchart_caption"] is not None and st.session_state["scatterplot_caption"] is not None:
        if "messages" not in st.session_state:
            st.session_state.messages = []
        chat_llm = ChatOpenAI(**model_args_streaming)
        the_report_prompt = prompts.reporter_prompt(
            st.session_state['abstract'],
            st.session_state["scatterplot_caption"],
            st.session_state["barchart_caption"],
            st.session_state["inventory"],
            st.session_state["rough_drafts"])

        a_report_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    the_report_prompt
                ),MessagesPlaceholder(variable_name="messages")
            ]
        )

        the_report_agent = a_report_prompt | chat_llm

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                AIMessage(content=agent_intro[st.session_state["language"]]),
            ]

        for message in st.session_state.chat_history:
            if isinstance(message, AIMessage):
                with st.chat_message("AI"):

                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.write(message.content)

        user_query = st.chat_input("Type your message here...")
        if user_query is not None and user_query != "":
            st.session_state.chat_history.append(HumanMessage(content=user_query))

            with st.chat_message("Human"):
                st.markdown(user_query)

            with st.chat_message("AI"):
                query = [HumanMessage(content=user_query)]
                response = the_report_agent.stream(query)
                r = st.write_stream(response)

            st.session_state.chat_history.append(AIMessage(content=r))
    else:
        st.warning(prompts.labels["update_captions"][language])
else:
    st.warning(prompts.labels["no_rough_draft_message"][language])
