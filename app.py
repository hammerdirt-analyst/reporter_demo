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

load_dotenv()
language_column_map = {"English": "en", "French": "fr", "German": "de"}
def use_model(**kwargs):
    if kwargs.get('name') == 'openai':
        kwargs.pop('name')
        return ChatOpenAI(**kwargs)
    else:
        return "No model found"

def translate_state_to_meta(state, code_groups, location, boundary) -> reporting_methods.ReportMeta:
    """Converts the form state into a ReportMeta object. The report_meta object is used to filter the data and generate reports."""

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

def filter_dataframe_with_reportmeta(report_meta: reporting_methods.ReportMeta, data: pd.DataFrame):
    """
    Filters the DataFrame based on the conditions provided in report_meta.

    Parameters
    ----------
    report_meta : dict
        Dictionary containing the filtering criteria.
    data : pd.DataFrame
        The application state containing the DataFrame to filter.

    Returns
    -------
    pd.DataFrame
        The filtered DataFrame.
    """
    f_data = data.copy()

    # Apply date range filter
    if report_meta.get('start'):
        f_data = f_data[f_data['date'] >= f"{report_meta.start}"]

    if report_meta.get('end'):
        f_data = f_data[f_data['date'] <= f"{report_meta.end}"]

    # Apply boundary conditions
    if report_meta.get('boundary') and report_meta.boundary_name:
        boundary = report_meta.boundary
        boundary_name = report_meta.boundary_name
        f_data = f_data[f_data[boundary] == boundary_name]

    # Apply feature type filter
    if report_meta.get('feature_type'):
        if report_meta.feature_type == 'lake':
            f_data = f_data[f_data['feature_type'] == 'l']
        elif report_meta.feature_type == 'river':
            f_data = f_data[f_data['feature_type'] == 'r']

    # Apply feature name filter
    if report_meta.get('feature_name'):
        f_data = f_data[f_data['feature_name'] == report_meta.feature_name]

    # Apply object codes filter
    if report_meta.get('report_codes'):
        codes = report_meta.report_codes
        f_data = f_data[f_data['code'].isin(codes)]

    return f_data

def baseline_report_and_data(report_meta: reporting_methods.ReportMeta, data, material_spec):

    df = filter_dataframe_with_reportmeta(report_meta, data)
    survey_report = reporting_methods.SurveyReport(df) # , feature_variables=report_meta.columns_of_interest,
                               # info_columns=report_meta.info_columns)

    # baseline report sections
    admin_boundaries = reporting_methods.extract_roughdraft_text(survey_report.administrative_boundaries())
    features = reporting_methods.extract_roughdraft_text(survey_report.feature_inventory())
    summary_stats = reporting_methods.extract_roughdraft_text(survey_report.sampling_results_summary)
    materials = reporting_methods.extract_roughdraft_text(survey_report.material_report(material_spec))
    survey_totals = reporting_methods.extract_roughdraft_text(reporting_methods.survey_totals_for_all_info_cols(report_meta, survey_report))
    inventory = reporting_methods.extract_roughdraft_text(survey_report.object_summary())

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

def generate_reports(state, code_groups, material_spec, data):
    reports = []

    if len(state['canton']) > 0:
        for location in state['canton']:
            meta = translate_state_to_meta(state, code_groups, location, "canton")
            report = baseline_report_and_data(meta, data, material_spec)
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
    df.reset_index(drop=False, inplace=True)
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

    return fig

def apply_filters():
    """
    Updates `f_data` based on the current selections in session state.
    Uses OR logic for each selection and dynamically narrows down options.
    """
    print("Applying filters\n")
    s_data = st.session_state["survey_data"]  # Original unfiltered data
    f_data = s_data.copy()

    # Step 1: Filter by Canton
    s_cantons = st.session_state["canton"]
    if s_cantons:
        f_data = f_data[f_data["canton"].isin(selected_cantons)]

    # Step 2: Filter by City
    s_cities = st.session_state["city"]
    if s_cities:
        f_data = f_data[f_data["city"].isin(selected_cities)]

    # Step 3: Filter by Feature Name
    s_feature_names = st.session_state["feature_name"]
    if s_feature_names:
        f_data = f_data[f_data["feature_name"].isin(selected_feature_names)]

    # Step 4: Filter by Feature Type
    f_type = st.session_state["feature_type"]
    if f_type != "both":
        feature_code = "l" if feature_type == "lake" else "r"
        f_data = f_data[f_data["feature_type"] == feature_code]
    s_codes = st.session_state['selected_objects']
    if s_codes:
        f_data = f_data[f_data['code'].isin(selected_codes)]
    date_range = st.session_state["date_range"]
    if date_range:
        print(date_range, type(date_range[0]))
        print(type(f_data['date'].min()), f_data['date'].max())
        print(f_data['date'].min() < pd.Timestamp(date_range[1]))
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

    # aresponse = llm.invoke(scatterplot_message)
    # caption = aresponse.content

    return llm.stream(scatterplot_message)

def scatterplot_title(s_language, s_labels, color):
    """
    Generates a title for a scatterplot in the specified language.

    Args:
        s_language (str): The desired language for the title ("English", "French", "German").
        s_labels (dict): A dictionary containing language-specific labels for the color groupings.
        color (str): The key for the color grouping.

    Returns:
        str: The scatterplot title in the specified language.
    """

    grouper = labels[color].get(s_language, s_labels[color].get("English"))

    title_templates = {
        "English": f"Cumulative pcs/m per survey by survey date, grouped by {grouper}",
        "French": f"Pièces cumulées/m par enquête par date d'enquête, regroupées par {grouper}",
        "German": f"Kumulative Stk./m pro Umfrage nach Umfragedatum, gruppiert nach {grouper}",
    }

    return title_templates.get(language, title_templates["English"])

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
        title=scatterplot_title(s_language, s_labels, color_by),
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
    if y_axis == "quantity":
        grouped_data = data.groupby(x_axis)[y_axis].sum().reset_index()
    if y_axis == "pcs/m":
        grouped_data = data.groupby(['sample_id', x_axis], as_index=False)[y_axis].sum()
        grouped_data = grouped_data.groupby(x_axis, as_index=False)[y_axis].mean().reset_index()

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
    # caption = aresponse.content

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
        min_d = st.session_state["filtered_data"]["date"].min()
        max_d = st.session_state["filtered_data"]["date"].max()
        st.session_state["date_range"] = (min_d, max_d)

    if "rough_drafts" not in st.session_state:
        st.session_state["rough_drafts"] = "No roughdrafts generated yet."

    if 'abstract' not in st.session_state:
        st.session_state['abstract'] = "No abstract generated yet."

    if 'inventory' not in st.session_state:
        st.session_state['inventory'] = "No inventory generated yet."

    if 'map_fig' not in st.session_state:
        st.session_state['map_fig'] = "No map generated yet."

    if 'scatterplot_caption' not in st.session_state:
        st.session_state['scatterplot_caption'] = None

    if 'barchart_caption' not in st.session_state:
        st.session_state['barchart_caption'] = None


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

English_instructions = (
    "Make a summary of data and select chart contents.\n\n"
    "1. Select a canton, city, lake or river.\n"
    "2. Select your date range.\n"
    "3. Select the objects of interest.\n"
    "4. Apply filters.\n"
    "5. Make rough drafts.\n"
    "6. Define chart contents and create summary of chart.\n"
    "7. Chat with data.\n\n"
)

French_instructions = (
    "Faites un résumé des données et sélectionnez le contenu du graphique.\n\n"
    "1. Sélectionnez un canton, une ville, un lac ou une rivière.\n"
    "2. Sélectionnez votre plage de dates.\n"
    "3. Sélectionnez les objets d'intérêt.\n"
    "4. Appliquez des filtres.\n"
    "5. Faites des brouillons.\n"
    "6. Définissez le contenu du graphique et créez un résumé du graphique.\n"
    "7. Discutez avec les données.\n\n"
)

German_instructions = (
    "Erstellen Sie eine Datenzusammenfassung und wählen Sie die Diagramminhalte aus.\n\n"
    "1. Wählen Sie einen Kanton, eine Stadt, einen See oder einen Fluss aus.\n"
    "2. Wählen Sie Ihren Datumsbereich aus.\n"
    "3. Wählen Sie die interessierenden Objekte aus.\n"
    "4. Wenden Sie Filter an.\n"
    "5. Erstellen Sie grobe Entwürfe.\n"
    "6. Definieren Sie die Diagramminhalte und erstellen Sie eine Zusammenfassung des Diagramms.\n"
    "7. Chatten Sie mit den Daten.\n\n"
)

instruction_labels = {
    "English": English_instructions,
    "French": French_instructions,
    "German": German_instructions
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
        "English": ":orange[Step 1: Select regions or feature of interest]",
        "French": ":orange[Étape 1 : Sélectionnez les régions ou caractéristiques d'intérêt]",
        "German": ":orange[Schritt 1 : Wählen Sie Regionen oder interessante Merkmale aus]"
    },
    "step_2_subheader": {
        "English": ":orange[Step 2: Select date range]",
        "French": ":orange[Étape 2 : Sélectionnez la plage de dates]",
        "German": ":orange[Schritt 2: Wählen Sie den Datumsbereich aus]"
    },
    "step_3_subheader": {
        "English": ":orange[Step 3: Select objects of interest]",
        "French": ":orange[Étape 3 : Sélectionnez les objets d'intérêt]",
        "German": ":orange[Schritt 3: Wählen Sie interessante Objekte aus]"
    },
    "step_4_subheader": {
        "English": ":orange[Step 4: Filter data]",
        "French": ":orange[Étape 4 : Filtrer les données]",
        "German": "orange[Schritt 4: Daten filtern]"
    },
    "step_5_subheader": {
        "English": ":orange[Step 5: Make rough draft]",
        "French": ":orange[Étape 5 : Rédigez un brouillon]",
        "German": ":orange[Schritt 5: Entwurf erstellen]"
    },
    "step_6_subheader": {
        "English": ":orange[Step 6: Scatterplot parameters]",
        "French": ":orange[Étape 6 : Nuage de points]",
        "German": ":orange[Schritt 6: Streuplot-Parameter]"
    },
    "step_7_subheader": {
        "English": ":orange[Step 7: Barchart parameters]",
        "French": ":orange[Étape 7 : Diagramme en barres]",
        "German": ":orange[Schritt 7: Balkendiagramm-Parameter]"
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
    },
    "survey_results": {
        "English":"Survey results",
        "French": "Résultats de l'enquête",
        "German": "Umfrageergebnisse"
    },
    "discussion": {
        "English": "Discussion",
        "French": "Discussion",
        "German": "Diskussion"
    },
    "shoreline_litter_assessment": {
        "English": "Shoreline litter assessment",
        "French": "Évaluation des déchets sur le littoral",
        "German": "Bewertung des Küstenmülls"
    },
    "summary": {
        "English": "Summary",
        "French": "Résumé",
        "German": "Zusammenfassung"
    },
    "rough_draft": {
        "English": "Rough draft",
        "French": "Brouillon",
        "German": "Entwurf"
    },
    "inventory": {
        "English": "Inventory",
        "French": "Inventaire",
        "German": "Inventar"
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
model_args_no_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000,
                                       streaming=False)

model_args_streaming = dict(name='openai', model="gpt-4o-mini", temperature=0.6, max_tokens=1000)
if 'language' not in st.session_state:
    st.header("Shoreline litter assessment")
else:
    st.header(labels["shoreline_litter_assessment"][st.session_state['language']])
language = st.radio(
    "", ["English", "French", "German"], index=0, horizontal=True, key="language"
)
st.markdown(intro_one[language])
st.image("resources/goodimage.webp")
st.markdown(intro_two[language])

with st.expander(f"**{labels['whats_this'][language]}**", expanded=False):
    st.markdown(intro_content[language])

st.markdown(instruction_labels[language])

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

        feature_type_translations = {
            "lake": {"English": "Lake", "French": "Lac", "German": "See"},
            "river": {"English": "River", "French": "Rivière", "German": "Fluss"},
            "both": {"English": "Both", "French": "Les deux", "German": "Beide"}
        }

        feature_type_mapping = {"l": "lake", "r": "river"}
        available_feature_types_labels = [feature_type_mapping[ft] for ft in available_feature_types if
                                          ft in feature_type_mapping]
        if len(available_feature_types_labels) > 1:
            available_feature_types_labels.append("both")

        def format_option(option):
            return feature_type_translations[option][language]

        feature_type = st.radio(
            label="Select feature type",
            options=available_feature_types_labels if available_feature_types_labels else ["both"],
            format_func=format_option,
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

        available_objects = st.session_state["filtered_data"]["code"].unique()

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

if "language" not in st.session_state:
    st.subheader("Survey results")
else:
    st.subheader(labels["survey_results"][st.session_state['language']])

tab1, tab2, tab3, tab4, tab5 = st.tabs([labels["summary"][language], labels["step_6_subheader"][language], labels["step_7_subheader"][language], labels["inventory"][language], labels["rough_draft"][language]])

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
                SystemMessage(prompts.abstract_prompt(st.session_state['language'], feature_type, objects, cantons)),
                HumanMessage(content=st.session_state['rough_drafts'])
            ]


            an_absract = current_llm.stream(abstract_message)
            abstract = st.write_stream(an_absract)
            # print(abstract)
            # g=AIMessage(content=abstract)
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

            map_fig = scatter_map(chart_data, lat_lon())
            st.session_state["map_fig"] = map_fig
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
        else:
            st.plotly_chart(st.session_state["map_fig"], use_container_width=True)
            chart_data = st.session_state.get("filtered_data", pd.DataFrame())
    else:
        st.warning("No rough-draft created")
        # current_llm = use_model(**model_args_no_streaming)
        chart_data = pd.DataFrame()

with tab2:
    if not chart_data.empty:
        current_llm = use_model(**model_args_streaming)

        scatter_color_by = st.selectbox(
            "Color By", ["canton", "city", "feature_name"], key="scatter_color_by"
        )

        scatter_fig = scatterplot(chart_data, st.session_state['language'], labels, scatter_color_by)
        st.plotly_chart(scatter_fig, use_container_width=True, config=config)

        # Initialize session state variables if not already set
        if "scatterplot_previous_color_by" not in st.session_state:
            st.session_state["scatterplot_previous_color_by"] = None
        if "scatterplot_caption" not in st.session_state:
            st.session_state["scatterplot_caption"] = None

        # Reset caption if color-by selection changes
        if st.session_state["scatterplot_previous_color_by"] != scatter_color_by:
            st.session_state["scatterplot_caption"] = None
            st.session_state["scatterplot_previous_color_by"] = scatter_color_by

        # Display existing caption or handle button click
        if st.session_state["scatterplot_caption"] is not None:
            st.write(st.session_state["scatterplot_caption"])
        else:
            if st.button("Explain Chart", key="scatterplot_caption_button"):
                l = st.session_state['language']
                explanation = scatterplot_caption(chart_data, scatter_color_by, l, current_llm)
                scatter_plot_caption = st.write_stream(explanation)

                # Store the generated caption in session state
                st.session_state["scatterplot_caption"] = scatter_plot_caption
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

        if st.session_state["barchart_caption"] is not None:
            st.write(st.session_state["barchart_caption"])
        else:
            if st.button("Explain Chart", key="barchart_caption_button"):
                l = st.session_state['language']
                explanation = barchart_caption(chart_data,x_axis, y_axis, l, current_llm)
                bar_chart_caption = st.write_stream(explanation)

                st.session_state["barchart_caption"] = bar_chart_caption
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
        st.warning("Select parameters, update the chart definitions and then you can chat with the data")

if 'language' not in st.session_state:
    st.subheader("Discussion")
else:
    st.subheader(labels["discussion"][st.session_state['language']])

if "final_selected_parameters" in st.session_state:

    if st.session_state["barchart_caption"] is not None and st.session_state["scatterplot_caption"] is not None:
        if "messages" not in st.session_state:
            st.session_state.messages = []
        chat_llm = ChatOpenAI(**model_args_streaming)
        print(st.session_state.keys())
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
        # session state
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                AIMessage(content=agent_intro[st.session_state["language"]]),
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
                r = st.write_stream(response)

            st.session_state.chat_history.append(AIMessage(content=r))
    else:
        st.warning("You need to update the chart explanations. before you can chat")

else:
    st.warning("No roughdrafts generated yet.")
