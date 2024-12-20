
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import reporting_methods
import plotly.express as px
import streamlit as st
import pandas as pd

from dotenv import load_dotenv


from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage, SystemMessage,
)

load_dotenv()

def use_model(**kwargs):
    if kwargs.get('name') == 'openai':
        kwargs.pop('name')
        return ChatOpenAI(**kwargs)
    else:
        return "No model found"

model_args_no_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000,
                                       streaming=False)

model_args_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000)

def translate_state_to_meta(state, code_groups, location, boundary):

    meta = {
        "name": location,
        "start": state['start_date'],
        "end": state['end_date'],
        "feature_type": state['feature_type'],
        "code_group_category": "Selected Codes",
        "boundary": boundary,
        "boundary_name": location if boundary else None,
        "feature_name": location if not boundary else None,
        "report_codes": state['codes'],
        "info_columns": reporting_methods.info_columns,
        "columns_of_interest": reporting_methods.feature_variables
    }

    meta['report_title'] = f"{meta['name']} {meta['feature_type']}"
    meta['report_subtitle'] = f"Codes: {meta['code_group_category']}"
    meta['title_notes'] = "Proof of concept AI assisted reporting"
    meta['author'] = "hammerdirt analyst"
    meta['code_types'] = code_groups.loc[meta['report_codes']].groupname.unique().tolist()

    return reporting_methods.ReportMeta(**meta)

def filter_dataframe_with_reportmeta(report_meta: reporting_methods.ReportMeta, data):
    """
    Filters the DataFrame based on the conditions provided in report_meta.

    Parameters
    ----------
    report_meta : dict
        Dictionary containing the filtering criteria.
    state : AppState
        The application state containing the DataFrame to filter.

    Returns
    -------
    pd.DataFrame
        The filtered DataFrame.
    """
    filtered_data = data.copy()

    # Apply date range filter
    if report_meta.get('start'):
        filtered_data = filtered_data[filtered_data['date'] >= f"{report_meta.start}"]
    if report_meta.get('end'):
        filtered_data = filtered_data[filtered_data['date'] <= f"{report_meta.end}"]

    # Apply boundary conditions
    if report_meta.get('boundary') and report_meta.boundary_name:
        boundary = report_meta.boundary
        boundary_name = report_meta.boundary_name
        filtered_data = filtered_data[filtered_data[boundary] == boundary_name]

    # Apply feature type filter
    if report_meta.get('feature_type'):
        if report_meta.feature_type == 'lake':
            filtered_data = filtered_data[filtered_data['feature_type'] == 'l']
        elif report_meta.feature_type == 'river':
            filtered_data = filtered_data[filtered_data['feature_type'] == 'r']

    # Apply feature name filter
    if report_meta.get('feature_name'):
        filtered_data = filtered_data[filtered_data['feature_name'] == report_meta.feature_name]

    # Apply object codes filter
    if report_meta.get('report_codes'):
        codes = report_meta.report_codes
        filtered_data = filtered_data[filtered_data['code'].isin(codes)]

    return filtered_data


def baseline_report_and_data(report_meta: reporting_methods.ReportMeta, data, code_material):

    df = filter_dataframe_with_reportmeta(report_meta, data)
    s, l = reporting_methods.make_report_objects(df, feature_variables=report_meta.columns_of_interest,
                               info_columns=report_meta.info_columns)

    # baseline report sections
    admin_boundaries = reporting_methods.extract_roughdraft_text(s.administrative_boundaries())
    features = reporting_methods.extract_roughdraft_text(s.feature_inventory())
    summary_stats = reporting_methods.extract_roughdraft_text(s.sampling_results_summary)
    materials = reporting_methods.extract_roughdraft_text(s.material_report(code_material))
    survey_totals = reporting_methods.extract_roughdraft_text(reporting_methods.survey_totals_for_all_info_cols(report_meta, s))
    inventory = reporting_methods.extract_roughdraft_text(s.object_summary())

    # report title section
    title = "## " + report_meta.report_title + "\n"
    objectsoi = "**Objects:** " + ', '.join(report_meta.code_types) + "\n\n"
    notes = "**Notes:** " + report_meta.title_notes + "\n\n"
    author = "**Author:** " + report_meta.author + "\n\n"
    intro = f'{title}{objectsoi}{notes}{author}'

    # individual sections
    for section in [summary_stats, admin_boundaries, features, materials, survey_totals, inventory]:
        intro += section + "\n"

    return intro

def generate_reports(state, code_groups, code_material, data):
    reports = []

    if len(state['canton']) > 0:
        for location in state['canton']:
            meta = translate_state_to_meta(state, code_groups, location, "canton")
            report = baseline_report_and_data(meta, data, code_material)
            reports.append(report)

    if len(state['city']) > 0:
        for location in state['city']:
            meta = translate_state_to_meta(state, code_groups, location, "city")
            report = baseline_report_and_data(meta, data, code_material)
            reports.append(report)

    if len(state['feature_name']) > 0:
        for location in state['feature_name']:
            meta = translate_state_to_meta(state, code_groups, location, None)
            report = baseline_report_and_data(meta, data, code_material)
            reports.append(report)

    return "\n".join(reports)

def map_markers(filtered_data, lat_lon):
    """Map the markers"""

    nsamples = filtered_data.groupby('location', observed=True)['sample_id'].nunique()
    qty_location = filtered_data.groupby('location', observed=True)['quantity'].sum()
    rate_location = filtered_data.groupby('location', observed=True)['pcs/m'].mean().round(2)
    last_sample = filtered_data.groupby('location', observed=True)['date'].max()

    # merge the pop-up information with the gps coordinates
    df = pd.concat([nsamples, qty_location, rate_location, last_sample], axis=1)
    df = df.merge(lat_lon[['longitude', 'latitude']], left_index=True, right_index=True)
    df['location'] = df.index
    df.rename(columns={'sample_id': 'nsamples', 'date': 'last sample'}, inplace=True)
    df.reset_index(drop=False, inplace=True)
    return df

def scatter_map(filtered_data, lat_lon):
    """
    Generates a map with markers using Plotly's scatter_map.
    - Markers use lat/lon from map_markers.
    - Hover information includes samples, quantity, pcs/m, and last sample date.
    """
    # Call your map_markers function to get the processed data
    df = map_markers(filtered_data, lat_lon)
    print("Making map markers\n")
    print(f"Map marker columns: {', '.join(df.columns)}")

    # Add hover text for each marker
    # df["hover_text"] = (
    #     "Location: " + df["location"] +
    #     "<br>Samples: " + df["nsamples"].astype(str) +
    #     "<br>Total Quantity: " + df["quantity"].astype(str) +
    #     "<br>Rate (pcs/m): " + df["pcs/m"].astype(str) +
    #     "<br>Last Sample: " + df["date"].astype(str)
    # )

    # Generate map with scatter_map
    fig = px.scatter_map(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="location",
        hover_data=['quantity', 'nsamples', 'pcs/m', 'last sample'],  # Hover text dynamically formatted
        # color_discrete_sequence=["fuchsia"],
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

    return fig


def apply_filters():
    """
    Updates `filtered_data` based on the current selections in session state.
    Uses OR logic for each selection and dynamically narrows down options.
    """
    print("Applying filters\n")
    survey_data = st.session_state["survey_data"]  # Original unfiltered data
    filtered_data = survey_data.copy()

    # Step 1: Filter by Canton
    selected_cantons = st.session_state["canton"]
    if selected_cantons:
        filtered_data = filtered_data[filtered_data["canton"].isin(selected_cantons)]

    # Step 2: Filter by City
    selected_cities = st.session_state["city"]
    if selected_cities:
        filtered_data = filtered_data[filtered_data["city"].isin(selected_cities)]

    # Step 3: Filter by Feature Name
    selected_feature_names = st.session_state["feature_name"]
    if selected_feature_names:
        filtered_data = filtered_data[filtered_data["feature_name"].isin(selected_feature_names)]

    # Step 4: Filter by Feature Type
    feature_type = st.session_state["feature_type"]
    if feature_type != "both":
        feature_code = "l" if feature_type == "lake" else "r"
        filtered_data = filtered_data[filtered_data["feature_type"] == feature_code]
    selected_codes = st.session_state['selected_objects']
    if selected_codes:
        filtered_data = filtered_data[filtered_data['code'].isin(selected_codes)]
    date_range = st.session_state["date_range"]
    if date_range:
        print(date_range, type(date_range[0]))
        print(type(filtered_data['date'].min()), filtered_data['date'].max())
        print(filtered_data['date'].min() < pd.Timestamp(date_range[1]))
        mask = (filtered_data['date'] >= pd.Timestamp(date_range[0])) & (filtered_data['date'] <= pd.Timestamp(date_range[1]))
        filtered_data = filtered_data[mask]
    # Update session state with the filtered data
    st.session_state["filtered_data"] = filtered_data.reset_index(drop=True)

def clear_filters(load_survey_data):
    """Clear all filters and reinitialize session state."""
    # Clear all session state variables
    st.session_state.clear()

    # Reinitialize the session state
    initialize_session_state(load_survey_data)

def update_date_range(filtered_data):
    """
    Updates the min and max date range based on the filtered data.
    Ensures all dates are consistently `datetime.date` objects.
    """
    # Calculate the min and max dates as datetime.date
    min_date = filtered_data["date"].min()
    max_date = filtered_data["date"].max()

    # Ensure date_range exists in session state
    if "date_range" not in st.session_state or len(st.session_state["date_range"]) != 2:
        st.session_state["date_range"] = (min_date, max_date)

    # Extract start_date and end_date from session state
    start_date, end_date = st.session_state["date_range"]
    print(type(start_date), type(end_date))

    # Convert to datetime.date if they are Timestamps
    if isinstance(start_date, pd.Timestamp):
        pass
    else:
        start_date = pd.to_datetime(start_date)
    if isinstance(end_date, pd.Timestamp):
        pass
    else:
        end_date = pd.to_datetime(end_date)

    # Clamp the start_date and end_date to the min and max dates
    start_date = max(min_date, min(start_date, max_date))
    end_date = max(min_date, min(end_date, max_date))

    # Update session state with the clamped values
    st.session_state["date_range"] = (start_date, end_date)

    return start_date, end_date

def abstract_prompt(language, feature_type, objects, cantons):
    """Prompt for the abstract generation task."""

    if feature_type == "lake":
        lakes_or_rivers = "lakes"
    elif feature_type == "river":
        lakes_or_rivers = "rivers"
    else:
        lakes_or_rivers = "lakes and rivers"

    aprompt = (
        f"You are a data scientist. You are writing the description of the data from a scatterplot. The data is  from"
        f" observations of {objects} found along {lakes_or_rivers} in {', '.join(cantons)}. The data has been selected by the client."
        " These observations are given in total pieces per meter per sample. A sample is defined by a location and a date",
        ". Your task is to write an informative abstract about the user provided report. Each report has the following"
        " sections:\n\nTitle, subtitle, summary",
        "statistics, administrative boundaries,",
        " the named features, and the material composition. After these sections the aggregated survey data is grouped",
        " for different regions and features. Each report is concluded with an inventory of each of the objects selected",
        " by the client.\n\nYour abstract must include information about the cities cantons or",
        " features included in the report. It must also include the names of the objects (look in the inventory) which"
        " are the subject of the report.",
        " The fail rate is the rate at which we expect to find at least one of the objects at a survey.",
        " From the summary statistics include The total number (quantity) of objects, the number of samples",
        " (summary statistics) and start and end date of samples should also be mentioned.",
        " The objects in the report are selected by the client. The report is about those objects and nothing more."
        " You must answer in paragraph form, limit your response to two paragraphs.\n\nThis is an abstract for a"
        " professional document. It should sound like one. We do not need any general closing statements. Your abstract"
        f" only concerns the contents of the report.\n\nPlease reply in the following language: {language}."
    )
    return ''.join(aprompt)

def scatterplot_prompt(start, end, interval, group_mean, objects, color, feature_type, cantons, language):
    """
    Generates a scatter plot prompt based on the provided parameters.
    """
    if feature_type == "lake":
        lakes_or_rivers = "lakes"
    elif feature_type == "river":
        lakes_or_rivers = "rivers"
    else:
        lakes_or_rivers = "lakes and rivers"



    prompt = (
        f"You are a data scientist. You are writing the description of the data from a scatterplot. The data is  from"
        f" observations of {objects} found along {lakes_or_rivers} in {', '.join(cantons)}. The data has been selected by the client."
        " These observations are given in total pieces per meter per sample. A sample is defined by a location and a date",
        ". Your task is to summarize the data in the plot AND identify any important features in the data.",
        " The plot characteristics are as follows::\n\n1. x axis: date of the sample\n2. y axis: pieces per meter, the sum of all",
        f" the objects found divided by the length of the shoreline that was surveyed.\n3. groups: {color} the regional aggregation",
        f" of the surveys.\n4. x axis start date {start}, x axis end date {end}\n5. y axis 90% interval: {interval}\n\n",
        f"The results by groups are as follows: {group_mean}\n\n.",
        "Your summary must be brief and to the point. The client has an image of the plot and your summary is to help them understand.",
        " Your audience is professional and they know how to read a scatterplot. Your summary should be about the data and not the plot."
        " You must answer in paragraph form in a concise and factual manner. Limit your response to two paragraphs. No titles or labels are wanted.\n\n",
        f"Your answer must be in the following language: {language}."
    )

    return ''.join(prompt)

def scatterplot_caption(data, color_by, language, llm):
    """
    Generates a caption for the scatter plot based on the filtered data and the color_by parameter.
    """
    d = data.groupby(['sample_id', 'date', color_by], as_index=False)["pcs/m"].sum()
    grouped_data_mean = d.groupby([color_by], as_index=False)["pcs/m"].mean()
    start_date, end_date = data.date.min().date(), data.date.max().date()
    ysummary = d["pcs/m"].describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95])
    print(data.columns)
    language_column_map = {"English": "en", "French": "fr", "German": "de"}
    description_column = language_column_map[st.session_state["language"]]
    objects = data[description_column].unique()
    objects = ', '.join(objects)
    cantons = data['canton'].unique()
    feature_type = data['feature_type'].unique()
    if len(feature_type) > 1:
        feature_type = "both"
    else:
        if feature_type[0] == 'l':
            feature_type = "lake"
        else:
            feature_type = "river"
    querry = scatterplot_prompt(start_date, end_date, ysummary, grouped_data_mean, objects, color_by, feature_type, cantons, language)
    abstract_message = [
        SystemMessage("follow the users instructions"),
        HumanMessage(content=querry)
    ]

    response = llm.invoke(abstract_message)
    caption = response.content

    return caption

def scatterplot_title(language, labels, color):
    """
    Generates a title for a scatterplot in the specified language.

    Args:
        language (str): The desired language for the title ("English", "French", "German").
        labels (dict): A dictionary containing language-specific labels for the color groupings.
        color (str): The key for the color grouping.

    Returns:
        str: The scatterplot title in the specified language.
    """

    grouper = labels[color].get(language, labels[color].get("English"))

    title_templates = {
        "English": f"Cumulative pcs/m per survey by survey date, grouped by {grouper}",
        "French": f"Pièces cumulées/m par enquête par date d'enquête, regroupées par {grouper}",
        "German": f"Kumulative Stk./m pro Umfrage nach Umfragedatum, gruppiert nach {grouper}",
    }

    return title_templates.get(language, title_templates["English"])

def scatterplot(data, language, labels, color_by):
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
        title=scatterplot_title(language, labels, color_by),
        labels={"date": "", "pcs/m": "pieces/meter"},
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

def handle_grouped_data_for_barchart(data, x_axis, y_axis):
    """Aggregates data for a barchart according to user requests and data type"""
    print('Handling grouped data\n')
    language_column_map = {"English": "en", "French": "fr", "German": "de"}
    description_column = language_column_map[st.session_state["language"]]
    if x_axis == 'object':
        x_axis = description_column
    if y_axis == "number of samples":
        grouped_data = data.groupby(x_axis, as_index=False)['sample_id'].nunique()
        grouped_data[y_axis] = grouped_data['sample_id']
        grouped_data.drop('sample_id', axis=1, inplace=True)
    if y_axis == "quantity":
        grouped_data = data.groupby(x_axis)[y_axis].sum().reset_index()
    if y_axis == "pcs/m":
        grouped_data = data.groupby(['sample_id', x_axis], as_index=False)[y_axis].sum()
        grouped_data = grouped_data.groupby(x_axis, as_index=False)[y_axis].mean().reset_index()

    return grouped_data

def barchart_prompt(data, x_axis, y_axis, language):
    """Creates a prompt for a barchart given the data and the x and y axis labels"""

    grouped_data = handle_grouped_data_for_barchart(data, x_axis, y_axis)
    feature_type = data['feature_type'].unique()
    if len(feature_type) > 1:
        lakes_or_rivers = "lakes and rivers"
    elif feature_type[0] == 'l':
        lakes_or_rivers = "lakes"
    else:
        lakes_or_rivers = "rivers"
    cantons = data['canton'].unique()
    description_column = language_column_map[language]
    objects = data[description_column].unique()
    prompt = (
        f"You are a data scientist. You are writing the description of the data from a bar plot. The data is  from"
        f" observations of {', '.join(objects)} found along {lakes_or_rivers} in {', '.join(cantons)}. The data has been selected by the client."
        f"Your task is to summarize the data in the bar chart AND identify any important features in the data.",
        f"The barchart characteristics are as follows::\n\n1. x axis: {x_axis} this is one of the following: canton,"
        " city, feautre_name, object. canton and city refer to locations in switzerland. feature_name refers to specific lakes or rivers.\n"
        f"2. yaxis : {y_axis} this is one of the following quantity, pcs/m, number of samples. Quantity refers to the"
        " number of objects found by x-axis category. pcs/m refers to the average number of objects observed per meter of shoreline."
        " number of samples refers to the number of times that samples were taken per xaxis category. Or you could say number of trips to the beach\n\n"
        f" the data used to create the chart is below:\n\n{grouped_data.to_markdown()}\n\n",
        "Identify the min and max values in the charts. Identify or define the xlabels provide details. summary must be brief"
        " and to the point. The client has an image of the plot and your summary is to help them understand.",
        " Your audience is professional and they know how to read a barplot. Your summary should be about the data. Further analysis"
        " is not needed. You must answer in paragraph form in a concise and factual manner.\n\n",
        f"Your answer must be in the following language: {language}."
    )

    return ''.join(prompt)

def barchart_caption(data, x_axis, y_axis, language, llm):
    """Creates a narrative for a barchart given the data and the x and y axis labels"""

    querry = barchart_prompt(data, x_axis, y_axis, language)
    abstract_message = [
        SystemMessage("follow the users instructions"),
        HumanMessage(content=querry)
    ]

    response = llm.invoke(abstract_message)
    caption = response.content

    return caption

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
        title=f"Bar Chart: Total {y_axis.capitalize()} by {x_axis.capitalize()}",
        labels={x_axis: x_axis.capitalize(), y_axis: y_axis.capitalize()},
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

def initialize_session_state(load_survey_data):
    """Set up initial state for session variables."""
    # Language selection
    if "language" not in st.session_state:
        st.session_state["language"] = "English"

    # Data and filtering
    if "filtered_data" not in st.session_state:
        st.session_state["filtered_data"] = load_survey_data()

    if "survey_data" not in st.session_state:
        st.session_state["survey_data"] = load_survey_data()

    if "date_range" not in st.session_state:
        min_date = st.session_state["filtered_data"]["date"].min()
        max_date = st.session_state["filtered_data"]["date"].max()
        st.session_state["date_range"] = (min_date, max_date)

    if "rough_drafts" not in st.session_state:
        st.session_state["rough_drafts"] = "No roughdrafts generated yet."

    if 'abstract' not in st.session_state:
        st.session_state['abstract'] = "No abstract generated yet."

    if 'inventory' not in st.session_state:
        st.session_state['inventory'] = "No inventory generated yet."

    if 'map_fig' not in st.session_state:
        st.session_state['map_fig'] = "No map generated yet."

def reporter_prompt(summary, scatterplot, barchart, inventory, rough_draft):
    aprompt = (
                "You are helping a data scientist write a summary report of volunteer observations of objects found along",
                " lakes and rivers in Switzerland. The data is collected using the JRC/EU method counting beach litter. This",
                " method is defined in the _Guide for monitoriring marine litter in european seas. Your other reference document",
                " is the federal report on litter density of swiss lakes (IQAASL) published in 2021 and available here:\n\n",
                "[IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n\n",
                "The client has already prepared a rough draft of the report as well as a bar chart, scatter plot and map.",
                " Your task is to answer the clients questions reference these reports. The client is preparing a decision",
                " support document and is relying on your for brief answers that can be supported by the documments provided",
                " below or the previously mentioned references. The client has provided the following documents:\n\n",
                f"summary: {summary}\n\n",
                f"scatterplot: {scatterplot}\n\n",
                f"barchart: {barchart}\n\n",
                f"inventory: {inventory}\n\n",
                f"rough draft: {rough_draft}\n\n",
                "!Instructions!\n\n"
                "The column names and descriptions for inventory items:\n1. object: the use or plain language description"
                "\n2. code: the MLW code for the item\n3. quantity: the total number of items found\n4. pcs/m: the average number"
                " of items per meter of shoreline.\n5 % of total: the proportion of the curent set of data.\n6. number of samples:"
                " the number of samples collected\n7. fail rate: the proportion of samples that contained the objects\n\n",
                "You are to discuss plastics, trash or litter in the environment, citizen-science, swiss or european policy",
                " concerning plastics and trash in the environment, probability and statistics, calculus, bayes theorem, bayesian statistics",
                " other topics of a sensitive or sexual nature are not to be considered.",
            )
    return ''.join(aprompt)

intro_one = {
    "English": """
    This is an application of large language models (LLMs) and machine learning to provide summary reports of volunteer observations of marine litter using the OSPAR, JRC, or NOAA methods for counting beach litter.
    """,
    "French": """
    Ceci est une application de modèles de langage avancés (LLMs) et d'apprentissage automatique pour fournir des rapports résumés des observations bénévoles des déchets marins en utilisant les méthodes OSPAR, JRC ou NOAA pour le comptage des déchets sur les plages.
    """,
    "German": """
    Dies ist eine Anwendung großer Sprachmodelle (LLMs) und maschinellen Lernens, um zusammenfassende Berichte über die Beobachtungen von Freiwilligen zu Meeresmüll zu erstellen, basierend auf den OSPAR-, JRC- oder NOAA-Methoden zur Erfassung von Strandmüll.
    """
}

intro_two = {
    "English": """
    The inspiration for this is the millions of people each year throughout the world who spend the time to collect the data.
    """,
    "French": """
    L'inspiration pour cela vient des millions de personnes à travers le monde qui, chaque année, prennent le temps de collecter les données.
    """,
    "German": """
    Die Inspiration dafür sind die Millionen von Menschen weltweit, die jedes Jahr Zeit investieren, um die Daten zu sammeln.
    """}

intro_content = {
    "English": """
    **Welcome to the Swiss Litter Monitoring App!**

    This app is designed to help stakeholders understand and analyze the types and quantities of litter found along rivers and lakes across Switzerland. By leveraging volunteer-collected data and established guidelines for monitoring marine litter in European seas, the app provides an insightful and comprehensive tool for tackling solid waste issues in these environments.

    **Key Features:**
    - Comprehensive Data Access: Explore all monitoring data collected since 2015.
    - Insights and Reporting: Prepare detailed reports and consolidate volunteer observations.
    - Community Collaboration: Benefit from the work of dedicated volunteers.

    **Based on Proven Research:**  
    This app is built on methodologies and insights from the following works:
    - [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)  
    - [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)  
    - [Land Use](https://hammerdirt-analyst.github.io/landuse/titlepage.html)  
    - [Plastock](https://associationsauvegardeleman.github.io/plastock/)  
    - [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)  

    **Open Source and Transparent:**  
    The app's source code, data, and documentation are available for review and collaboration:
    [Explore the documentation and source code here](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).
    """,
    "French": """
    **Bienvenue dans l'application Swiss Litter Monitoring!**

    Cette application est conçue pour aider les parties prenantes à comprendre et analyser les types et quantités de déchets trouvés le long des rivières et des lacs en Suisse. En s'appuyant sur des données collectées par des volontaires et des lignes directrices établies pour surveiller les déchets marins dans les mers européennes, l'application fournit un outil précieux et complet pour faire face aux problèmes de déchets solides dans ces environnements.

    **Principales caractéristiques :**
    - Accès complet aux données : Explorez toutes les données collectées depuis 2015.
    - Informations et rapports : Préparez des rapports détaillés et consolidez les observations des volontaires.
    - Collaboration communautaire : Profitez du travail de bénévoles dévoués.

    **Basé sur des recherches éprouvées :**  
    Cette application repose sur des méthodologies et des informations provenant des travaux suivants :
    - [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)  
    - [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)  
    - [Land Use](https://hammerdirt-analyst.github.io/landuse/titlepage.html)  
    - [Plastock](https://associationsauvegardeleman.github.io/plastock/)  
    - [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)  

    **Source ouverte et transparente :**  
    Le code source, les données et la documentation de l'application sont disponibles pour consultation et collaboration :
    [Explorez la documentation et le code source ici](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).
    """,
    "German": """
    **Willkommen in der Swiss Litter Monitoring App!**

    Diese App soll Interessengruppen dabei helfen, die Arten und Mengen von Abfall zu verstehen und zu analysieren, die entlang von Flüssen und Seen in der Schweiz gefunden werden. Durch die Nutzung von von Freiwilligen gesammelten Daten und etablierten Richtlinien zur Überwachung von Meeresmüll in europäischen Gewässern bietet die App ein wertvolles und umfassendes Werkzeug zur Bewältigung von Problemen mit festen Abfällen in diesen Umgebungen.

    **Hauptmerkmale:**
    - Umfassender Datenzugriff: Erkunden Sie alle seit 2015 gesammelten Überwachungsdaten.
    - Einblicke und Berichte: Erstellen Sie detaillierte Berichte und konsolidieren Sie Beobachtungen von Freiwilligen.
    - Gemeinschaftliche Zusammenarbeit: Profitieren Sie von der Arbeit engagierter Freiwilliger.

    **Basierend auf bewährter Forschung:**  
    Diese App basiert auf Methoden und Erkenntnissen aus den folgenden Arbeiten:
    - [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)  
    - [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)  
    - [Land Use](https://hammerdirt-analyst.github.io/landuse/titlepage.html)  
    - [Plastock](https://associationsauvegardeleman.github.io/plastock/)  
    - [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)  

    **Offen und transparent:**  
    Der Quellcode, die Daten und die Dokumentation der App sind zur Überprüfung und Zusammenarbeit verfügbar:
    [Entdecken Sie hier die Dokumentation und den Quellcode](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).
    """
}

labels = {
    "language": {
        "English": "Language",
        "French": "Langue",
        "German": "Sprache"
    },
    "filtering_data": {
        "English": "Filtering Data",
        "French": "Filtrage des données",
        "German": "Daten filtern"
    },
    "date_range": {
        "English": "Date Range",
        "French": "Plage de dates",
        "German": "Datumsbereich"
    },
    "canton": {
        "English": "Canton",
        "French": "Canton",
        "German": "Kanton"
    },
    "city": {
        "English": "City",
        "French": "Ville",
        "German": "Stadt"
    },
    "feature_type": {
        "English": "Feature Type",
        "French": "Type de caractéristique",
        "German": "Merkmaltyp"
    },
    "clear_filters": {
        "English": "Clear Filters",
        "French": "Effacer les filtres",
        "German": "Filter löschen"
    },
    "apply_filters": {
        "English": "Apply Filters",
        "French": "Appliquer les filtres",
        "German": "Filter anwenden"
    },
    "objects": {
        "English": "Objects of Interest",
        "French": "Objets d'intérêt",
        "German": "Interessante Objekte"
    },
    "feature_name": {
        "English": "Feature Name",
        "French": "Nom du lac/rivière",
        "German": "Merkmalsname"
    },
    "step_1": {
        "English": "Step 1",
        "French": "Étape 1",
        "German": "Schritt 1"
    },
    "step_2": {
        "English": "Step 2",
        "French": "Étape 2",
        "German": "Schritt 2"
    },
    "step_3": {
        "English": "Step 3",
        "French": "Étape 3",
        "German": "Schritt 3"
    },
    "selected_parameters": {
        "English": "Selected Parameters",
        "French": "Paramètres sélectionnés",
        "German": "Ausgewählte Parameter"
    },
    "whats_this": {
        "English": "What's this?",
        "French": "Qu'est-ce que c'est ?",
        "German": "Was ist das?"
    },
    "parameter_selection": {
        "English": "Parameter Selection",
        "French": "Sélection des paramètres",
        "German": "Parameterauswahl"
    },
    "step_1_subheader": {
        "English": ":orange[Step 1:] Select regions or feature of interest",
        "French": ":orange[Étape 1 :] Sélectionnez les régions ou caractéristiques d'intérêt",
        "German": ":orange[Schritt 1 :] Wählen Sie Regionen oder interessante Merkmale aus"
    },
    "step_2_subheader": {
        "English": ":orange[Step 2:] Select date range",
        "French": ":orange[Étape 2 :] Sélectionnez la plage de dates",
        "German": ":orange[Schritt 2:] Wählen Sie den Datumsbereich aus"
    },
    "step_3_subheader": {
        "English": ":orange[Step 3:] Select objects of interest",
        "French": ":orange[Étape 3 :] Sélectionnez les objets d'intérêt",
        "German": ":orange[Schritt 3:] Wählen Sie interessante Objekte aus"
    },
    "step_4_subheader": {
        "English": ":orange[Step 4:] Filter data",
        "French": ":orange[Étape 4 :] Filtrer les données",
        "German": "orange[Schritt 4:] Daten filtern"
    },
    "step_5_subheader": {
        "English": ":orange[Step 5:] Make rough draft",
        "French": ":orange[Étape 5 :] Rédigez un brouillon",
        "German": ":orange[Schritt 5:] Entwurf erstellen"
    },
    "step_6_subheader": {
        "English": ":orange[Step 6:] Scatterplot parameters",
        "French": ":orange[Étape 6 :] Nuage de points",
        "German": ":orange[Schritt 6:] Streuplot-Parameter"
    },
    "step_7_subheader": {
        "English": ":orange[Step 7:] Barchart parameters",
        "French": ":orange[Étape 7 :] Diagramme en barres",
        "German": ":orange[Schritt 7:] Balkendiagramm-Parameter"
    },
    "start_date": {
        "English": "Start Date",
        "French": "Date de début",
        "German": "Anfangsdatum"
    },
    "end_date": {
        "English": "End Date",
        "French": "Date de fin",
        "German": "Enddatum"
    },
    "selected_date_range": {
        "English": "Selected Date Range",
        "French": "Plage de dates sélectionnée",
        "German": "Ausgewählter Datumsbereich"
    },
    "selected_parameters_subheader": {
        "English": "Selected Parameters",
        "French": "Paramètres sélectionnés",
        "German": "Ausgewählte Parameter"
    },
    "apply_filters_button": {
        "English": "Apply Filters",
        "French": "Appliquer les filtres",
        "German": "Filter anwenden"
    },
    "filters_applied_message": {
        "English": "Filters applied! ",
        "French": "Filtres appliqués ! ",
        "German": "Filter angewendet!"
    },
    "make_roughdraft": {
        "English": "Make Roughdraft",
        "French": "Créer un brouillon",
        "German": "Entwurf erstellen"
    }

}

def translate_columns(language):
    # Translation dictionaries for column names
    translations = {
        "French": {
            "code": "code",
            "object": "objet",
            "quantity": "quantité",
            "pcs/m": "pcs/m",
            "% of total": "% du total",
            "number of samples": "Nombre d'échantillons",
            "fail rate": "taux d'échec"
        },
        "German": {
            "code": "Code",
            "object": "Objekt",
            "quantity": "Menge",
            "pcs/m": "Stk/m",
            "% of total": "% des Gesamt",
            "number of samples": "Proben nummer",
            "fail rate": "Fehlerrate"
        }
    }

    # Return the translation dictionary for the requested language
    if language in translations:
        return translations[language]
    else:
        raise ValueError(f"Language '{language}' not supported. Choose 'French' or 'German'.")

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

st.header("Shoreline litter assessment")
language = st.radio(
    "", ["English", "French", "German"], index=0, horizontal=True, key="language"
)
st.markdown(intro_one[language])
st.image("resources/goodimage.webp")
st.markdown(intro_two[language])
with st.expander(f"**{labels['whats_this'][language]}**", expanded=False):
    st.markdown(intro_content[language])

with st.expander(f"**{labels['parameter_selection'][language]}**", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        print("Inside parameter selection\n")
        st.write(f'**{labels["step_1_subheader"][language]}**')
        survey_data = st.session_state["survey_data"]

        selected_cantons = st.multiselect(
            label=labels["canton"][language],
            options=survey_data["canton"].unique(),
            default=st.session_state.get("canton", []),
            key="canton"
        )

        if selected_cantons:
            available_cities = survey_data[survey_data["canton"].isin(selected_cantons)]["city"].unique()
        else:
            available_cities = survey_data["city"].unique()

        selected_cities = st.multiselect(
            label=labels["city"][language],
            options=available_cities,
            default=st.session_state.get("city", []),
            key="city"
        )

        if selected_cantons:
            available_feature_names = survey_data[survey_data["canton"].isin(selected_cantons)]["feature_name"].unique()

        if selected_cities:
            available_feature_names = survey_data[survey_data["city"].isin(selected_cities)]["feature_name"].unique()

        if not selected_cantons and not selected_cities:
            available_feature_names = survey_data["feature_name"].unique()

        selected_feature_names = st.multiselect(
            label=labels["feature_name"][language],
            options=available_feature_names,
            default=st.session_state.get("feature_name", []),
            key="feature_name"
        )

        if selected_cantons:
            available_feature_types = survey_data[survey_data["canton"].isin(selected_cantons)]["feature_type"].unique()
        if selected_cities:
            available_feature_types = survey_data[survey_data["city"].isin(selected_cities)]["feature_type"].unique()
        if not selected_cantons and not selected_cities:
            available_feature_types = survey_data["feature_type"].unique()
        feature_type_mapping = {"l": "lake", "r": "river"}
        available_feature_types_labels = [feature_type_mapping[ft] for ft in available_feature_types if
                                          ft in feature_type_mapping]
        if len(available_feature_types_labels) > 1:
            available_feature_types_labels.append("both")

        feature_type = st.radio(
            label=labels["feature_type"][language],
            options=available_feature_types_labels if available_feature_types_labels else ["both"],
            horizontal=True,
            index=0,
            key="feature_type"
        )

        st.write(f'**{labels["step_2_subheader"][language]}**')

        min_date, max_date = update_date_range(st.session_state["filtered_data"])
        print(f'in streamlit: {type(min_date)}, {max_date}\nsession state: {st.session_state["date_range"]}\n')

        start_date = st.date_input(
            label=labels["start_date"][language],
            value=min_date,
            min_value=min_date,
            max_value=max_date,
            key="start_date"
        )
        end_date = st.date_input(
            label=labels["end_date"][language],
            value=max_date,
            min_value=min_date,
            max_value=max_date,
            key="end_date"
        )
        st.session_state["date_range"] = (start_date, end_date)
        selected_parameters = {
            "canton": selected_cantons,
            "city": selected_cities,
            "feature_name": selected_feature_names,
            "feature_type": feature_type,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "codes": st.session_state["selected_objects"] if "selected_objects" in st.session_state else []
           }
        st.write(f'**{labels["step_3_subheader"][language]}**')

        language_column_map = {"English": "en", "French": "fr", "German": "de"}
        description_column = language_column_map[st.session_state["language"]]

        filtered_data = st.session_state["filtered_data"]
        available_objects = filtered_data["code"].unique()

        object_descriptions = {row["code"]: row[description_column] for _, row in load_codes().iterrows() if
                               row["code"] in available_objects}

        selected_objects = st.multiselect(
            label=labels["objects"][language],
            options=list(object_descriptions.keys()),
            format_func=lambda x: f"{x} - {object_descriptions.get(x, '')}",
            default=st.session_state.get("selected_objects", []),
            key="selected_objects"
        )

        selected_codes = [obj.split(" - ")[0] for obj in selected_objects]
        selected_parameters["codes"] = selected_codes  # Update dynamically

    with col2:
        st.write(f'**{labels["selected_parameters_subheader"][language]}**')
        st.json(selected_parameters)
        st.write(f'**{labels["step_4_subheader"][language]}**')
        if st.button(labels["apply_filters_button"][language], key="apply_filters_button"):
            apply_filters()
            st.success(labels["filters_applied_message"][language])
        if st.button(labels['clear_filters'][language], key="clear_filters_button"):
            clear_filters(load_survey_data)
            st.success("Filters cleared!")
        st.write(f'**{labels["step_5_subheader"][language]}**')
        if st.button(labels["make_roughdraft"][language], key="make_roughdraft_button"):
            st.session_state["final_selected_parameters"] = selected_parameters

st.subheader("Survey results")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Summary", labels["step_6_subheader"][language], labels["step_7_subheader"][language], "inventory", "Rough Draft"])

with tab1:
    if "final_selected_parameters" in st.session_state:

        if st.session_state["abstract"] == "No abstract generated yet.":
            current_llm = use_model(**model_args_no_streaming)
            code_use = load_codes()[['code', 'groupname']].set_index('code')
            code_material = load_codes()[['code', 'material']].set_index('code')
            st.session_state["rough_drafts"] = generate_reports(st.session_state["final_selected_parameters"], code_use, code_material, st.session_state['filtered_data'])
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
                SystemMessage(abstract_prompt(st.session_state['language'], feature_type, objects, cantons)),
                HumanMessage(content=st.session_state['rough_drafts'])
            ]
            an_absract = current_llm.invoke(abstract_message)
            st.session_state['abstract'] = an_absract.content
            st.markdown(st.session_state['abstract'])
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

            map_fig = scatter_map(chart_data, lat_lon())
            st.session_state["map_fig"] = map_fig
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
        else:
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
            chart_data = st.session_state.get("filtered_data", pd.DataFrame())
    else:
        st.warning("No roughdraft created yet. Pleas apply filters after setting your filters.")
        current_llm = use_model(**model_args_no_streaming)
        chart_data = pd.DataFrame()

with tab2:
    if not chart_data.empty:
        current_llm = use_model(**model_args_no_streaming)
        scatter_color_by = st.selectbox("Color By", ["canton", "city", "feature_name"], key="scatter_color_by")
        scatter_fig = scatterplot(chart_data, st.session_state['language'], labels, scatter_color_by)
        st.plotly_chart(scatter_fig, use_container_width=True, config=config)

        if "scatterplot_previous_color_by" not in st.session_state or st.session_state["scatterplot_previous_color_by"] != scatter_color_by :
            st.session_state["scatterplot_caption"] = None
            st.session_state["scatterplot_previous_color_by"] = scatter_color_by

        if st.button("Explain Chart", key="scatterplot_caption_button"):
            l = st.session_state['language']
            explanation = scatterplot_caption(chart_data, scatter_color_by, l, current_llm)
            st.session_state["scatterplot_caption"] = explanation

        if st.session_state.get("scatterplot_caption"):
            st.write(st.session_state["scatterplot_caption"])
        else:
            st.warning("No data available. Please apply filters.")

with tab3:
    if not chart_data.empty:
        print('in bar chart\n')
        print(f"The chart data columns are: {chart_data.columns}\n")
        x_axis = st.selectbox("X-Axis", ["canton", "city", "feature_name", "object"], key="bar_x_axis")
        y_axis = st.selectbox("Y-Axis", ["quantity", "pcs/m", "number of samples"], key="bar_y_axis")
        barchart_color_by = x_axis
        bar_fig = barchart(chart_data, x_axis, y_axis)
        st.plotly_chart(bar_fig, use_container_width=True, config=config)

        if "barchart_previous_color_by" not in st.session_state or st.session_state["barchart_previous_color_by"] != barchart_color_by :
            st.session_state["barchart_caption"] = None
            st.session_state["barchart_previous_color_by"] = barchart_color_by

        if "barchart_previous_y" not in st.session_state or st.session_state["barchart_previous_y"] != y_axis:
            st.session_state["barchart_caption"] = None
            st.session_state["barchart_previous_y"] = y_axis

        if st.button("Explain Chart", key="barchart_explain_button"):
            l = st.session_state['language']
            explanation = barchart_caption(chart_data,x_axis, y_axis, l, current_llm)
            st.session_state["barchart_caption"] = explanation
        if st.session_state.get("barchart_caption"):
            st.write(st.session_state["barchart_caption"])

        else:
            st.warning("No data available. Please apply filters.")

    else:
        st.warning("No data available. Please apply filters.")

with tab4:
    if not chart_data.empty:
        s = reporting_methods.SurveyReport(chart_data)
        adict = s.object_summary()
        inv = adict[0]['dataframe']
        print(st.session_state['language'])
        inv.rename(columns={'sample_id': 'number of samples'}, inplace=True)
        if st.session_state['language'] != 'English':
            column_translations = translate_columns(st.session_state['language'])
            inv.rename(columns=column_translations, inplace=True)
        inv = inv.style.set_table_styles(reporting_methods.table_css_styles).format(**reporting_methods.format_kwargs)
        st.session_state["inventory"] = reporting_methods.extract_roughdraft_text(adict)
        st.dataframe(inv)
    else:
        st.warning("No data available. Please apply filters.")

with tab5:
    if "final_selected_parameters" in st.session_state:
        st.write(st.session_state["rough_drafts"])
    else:
        st.warning("No data available. Please apply filters.")

st.subheader("Discussion")
if "final_selected_parameters" in st.session_state:

    if st.session_state["barchart_caption"] is not None and st.session_state["scatterplot_caption"] is not None:
        if "messages" not in st.session_state:
            st.session_state.messages = []
        chat_llm = ChatOpenAI(**model_args_streaming)
        print(st.session_state.keys())
        the_report_prompt = reporter_prompt(
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

        # session state
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                AIMessage(content="Hello, I am a report assistant how can i help you?"),
            ]

        # conversation
        for message in st.session_state.chat_history:
            if isinstance(message, AIMessage):
                with st.chat_message("AI"):

                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.write(message.content)

        # user input
        user_query = st.chat_input("Type your message here...")
        if user_query is not None and user_query != "":
            st.session_state.chat_history.append(HumanMessage(content=user_query))

            with st.chat_message("Human"):
                st.markdown(user_query)

            with st.chat_message("AI"):
                query = [HumanMessage(content=user_query)]
                response = the_report_agent.stream(query)
                # print(response)
                # st.session_state.chat_history.append(AIMessage(content=response))
                r = st.write_stream(response)

            st.session_state.chat_history.append(AIMessage(content=r))
    else:
        st.warning("You need to update the chart explanations. before you can chat")

else:
    st.warning("No roughdrafts generated yet.")
