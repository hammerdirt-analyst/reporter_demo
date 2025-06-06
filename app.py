"""
app.py
author: Roger Erismann
purpose: submission to prototypefund.opendata.ch

This is the main file for the streamlit app. It is a digital assistant that helps put local environmental observations in
 the context of regional and national strategies. The app has three main tasks: forecasting, reporting and chatting with the references.

The forecasting task is not yet available. The reporting task allows the user to select a region, feature type, region(s)
and object group to generate a report. The chat task allows the user to chat with the references. The app is multilingual
and can be set to English, German, French or Italian. The app is designed to be a minimum viable product for AI assisted reporting.
"""
from streamlit import session_state as ss
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)
import reporting_methods as rmn
import prompts_labels

load_dotenv()

# llms for the chat and report
model_chat = "gpt-4o"
model_report = "gpt-4o-mini"
chat_llm = ChatOpenAI(model=model_chat, temperature=0.5, frequency_penalty=0.5, max_tokens=1500)
report_llm = ChatOpenAI(model=model_chat, temperature=0.3, max_tokens=1500, frequency_penalty=0.5)
inventory_llm = ChatOpenAI(model=model_report, temperature=0, max_tokens=1500)

filters = ["region", "feature_type", "selected_regions"]

# methods to set the current task
def forecast_values():
    print('changing to forecast')
    ss.current_task = "forecasting"

def report_values():
    print('changing to report')
    ss.current_task = "reporting"

def chat_with_references():
    print('changing to chat')
    ss.current_task = "chatting"

def display_current_parameters(state):
    print('displaying current parameters')
    current_params = {}
    if ss.current_task == "reporting":
        for filter in filters:
            if filter in state:
                current_params.update({filter: state[filter]})
    if ss.current_task == "forecasting":
        if 'reference_canton' in ss:
            current_params.update({"reference_canton": ss['reference_canton']})
        if 'reference_lake' in ss:
            current_params.update({"reference_lake": ss['reference_lake']})
        if 'reference_land_use' in ss:
            current_params.update({"reference_land_use": ss['reference_land_use']})
    if ss.current_task == "chatting":
        current_params.update({"llm model": model_chat })

    return current_params

# format the options according to language for the report types
def format_report_type_func(option):
    index = prompts_labels.labels['report_type_options']["English"].index(option)
    return prompts_labels.labels['report_type_options'][ss.language][index]

def format_feature_type_func(option):
    index = prompts_labels.labels['feature_type_options']["English"].index(option)
    return prompts_labels.labels['feature_type_options'][ss.language][index]

def format_object_group_func(option):
    index = prompts_labels.labels['code_groupnames']["English"].index(option)
    res = prompts_labels.labels['code_groupnames'][ss.language][index]
    return res

def format_groupname_func(option):
    if option is None:
        return "None"
    selected_language = ss.get("language", "English")  # Default to English
    res = prompts_labels.code_group_translations.get(selected_language, prompts_labels.code_group_translations["English"]).get(option, option)  # Return translated term or default
    return res

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
    lat_lon = beaches()[['slug', 'latitude', 'longitude']].set_index('slug')
    return lat_lon

if 'reset_options' in ss and ss['reset_options'] is True:
    print('resetting')
    for key in ss.keys():
        print(key)
        del ss[key]

st.set_page_config(
    page_title="The state of things",
    page_icon="resources/goodimage.jpeg",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This digital assistant helps put local environmental observations in the context of regional and national strategies."
    }
)

language = st.radio("Select language", ["English", "German", "French", "Italian"], horizontal=True, key='language')

if 'current_task' not in ss:
    ss.current_task = None

with st.sidebar:
    st.markdown("**Decision support from the field**")
    st.image("resources/images/goodimage.webp", width=400)
    st.markdown("**[Roger](https://www.linkedin.com/in/rogererismann) and [Shannon](https://www.linkedin.com/in/shannon-erismann-3a287746) Erismann - 2025**\n* _Minimum viable product - AI assisted reporting_\n* _Submission to [prototypefund](https://prototypefund.opendata.ch/en/about/digital-sufficiency/)_\n* _more info: [hammerdirt](https://hammerdirt.ch/)_")

    nsammples = load_survey_data().sample_id.nunique()
    ncantons = load_survey_data().canton.nunique()
    ncities = load_survey_data().city.nunique()
    nlocations = load_survey_data().location.nunique()
    nobjects = load_survey_data().quantity.sum()

    with st.expander("**Data: the big picture**", expanded=False):
        st.markdown(f"1. **Number of samples:** {nsammples}\n2. **Number of cantons:** {ncantons}\n3. **Number of cities:** {ncities}\n4. **Number of locations:** {nlocations}\n5. **Number of objects:** {nobjects}")
    with st.expander("**Articles in Retrieval Augmented Generation (RAG)**", expanded=False):
        st.markdown(prompts_labels.current_articles_rag)

    display_params = display_current_parameters(ss)

    if ss.current_task is None:
        st.markdown('**Current Task: None**')
    else:
        st.markdown(f"**Current Task: {ss.current_task.capitalize()}**")
        st.json(display_params)

with st.container(key="introduction"):
    # introduction and references
    st.title(prompts_labels.openning[ss.language])
    st.subheader(prompts_labels.secondopenning[ss.language])
    st.markdown(prompts_labels.report_assistant_text[ss.language])
    with st.expander(f"**{prompts_labels.labels['whats_this'][ss.language]}**", expanded=False):
        st.markdown(prompts_labels.what_this_reprorting_method_does[ss.language])
        st.markdown(prompts_labels.valuing_citizen_science[ss.language])
        st.markdown(prompts_labels.data_info_text[ss.language])

with st.container(key="task_container"):
    # side by side button to select a task
    st.subheader(prompts_labels.what_would_you_like_to_do[ss.language])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button(prompts_labels.tasks[ss.language]['Chat with the references'], type='primary', on_click=chat_with_references, use_container_width=True,
                  key='chatting')
    with col2:
        st.button(prompts_labels.tasks[ss.language]["Make a report"], type='primary', on_click=report_values, use_container_width=True, key='reporting')
    with col3:
        st.button(prompts_labels.tasks[ss.language]["Evaluate a sample / get a forecast"], type='primary', on_click=forecast_values, use_container_width=True,
                  key='forecasting')

# forecasting
if 'current_task' in ss and ss.current_task == "forecasting":
    st.markdown("**:red[Cette fonctionnalité n'est pas encore disponible - Diese Funktion ist noch nicht verfügbar - Questa funzione non è ancora disponibile - This function is not yet available]**")
    st.markdown(prompts_labels.sampleExplanation[ss.language])
    st.markdown(prompts_labels.properlyFormattedCsv[ss.language])
    st.markdown(prompts_labels.sampleTable)
# reporting
if 'current_task' in ss and ss.current_task == "reporting":
    # set state for the reporting section
    if 'selected_regions' not in ss:
        ss.selected_regions = []
    if 'selected_codes' not in ss:
        ss.selected_codes = []
    if 'roughdraft' not in ss:
        ss.roughdraft = prompts_labels.labels["no_rough_draft_yet"][ss.language]
    if 'report' not in ss:
        ss.report = False
    if 'region' not in ss:
        ss.region = None
    if 'feature_type' not in ss:
        ss.feature_type = None
    if 'object_group' not in ss:
        ss.object_group = None
    if 'generate_report' not in ss:
        ss.generate_report = False
    if 'report_sections' not in ss:
        ss.report_sections = {}
    # select the report parameters
    with st.container(key='A_form'):
        st.markdown(prompts_labels.define_the_report_parameters[ss.language])
        # select canton, lake, river or city
        with st.container(key='select_region_type', border=True):
            st.markdown(prompts_labels.labels['select_report_type'][ss.language])
            region = st.pills(
                label="Region",
                options=prompts_labels.labels['report_type_options']["English"],
                key='region',
                label_visibility='collapsed',
                format_func = format_report_type_func,
                default=None
            )
            # has lake, city, canton or river been selected
            selected_region = ss.region is not None
            if selected_region:
                selected_city_or_canton = ss.region in ['Canton', 'City']
                selected_river_or_lake = ss.region in ['Lake', 'River']
        # if canton or city has been selected are we reporting on lakes or rivers or both within the canton or city
        with st.container(key='select_feature_type', border=True):
            if selected_region and selected_city_or_canton:
                st.markdown(prompts_labels.labels['select_feature_type'][ss.language])
                feature_type = st.pills(
                    label="Feature Type",
                    options=prompts_labels.labels['feature_type_options']["English"],
                    key='feature_type',
                    label_visibility='collapsed',
                    format_func=format_feature_type_func,
                    default=None
                )
                selected_feature_type = ss.feature_type is not None
        # if canton or city has been selected and the feature type has been selected
        # select the canton(s) or city(ies) to report on
        with st.container(key='select_region', border=True):
            if selected_region:
                # the available citys, lakes, cantons or rivers to report on
                options = rmn.create_regional_options(load_survey_data(), ss.region)
                options = sorted(options)
                args = {
                    'label':"Select regions",
                    'options':options,
                    'key':'selected_regions',
                    'label_visibility':'collapsed',
                    'max_selections':4,
                    'default':None
                }
                # if city or canton has been selected select the city(s) or canton(s) to report on
                if selected_city_or_canton:
                    if ss.feature_type is not None:
                        st.markdown(prompts_labels.labels["select_locations"][ss.language])
                        selected_regions = st.multiselect(**args)
                # if lake or river has been selected select the lake(s) or river(s) to report on
                if selected_river_or_lake:
                    st.markdown(prompts_labels.labels["select_locations"][ss.language])
                    selected_regions = st.multiselect(**args)

        # if the lake, river, canton or city has been selected and the feature type has been selected
        # select the object group or specific objects to report on
        if 'selected_regions' in ss and len(ss.selected_regions) > 0:
            with st.container(key='select_codes_objects', border=True):
                st.markdown(prompts_labels.labels["select_object_group_type"][ss.language])
                st.markdown(prompts_labels.labels["select_object_group_type_instructions"][ss.language])

                # if selected_regions is empty the selector is disabled
                disabled_object_group = len(ss.selected_regions) == 0

                object_groups = st.pills(
                    label="Object Group",
                    options=prompts_labels.labels['object_group_type_options']["English"],
                    key='object_group',
                    label_visibility='collapsed',
                    format_func=format_object_group_func,
                    disabled=disabled_object_group,
                    default=None)

                # the code options are dependent on the selected regions
                # filter the data with the paramters up to this point and
                # and define the availble code options
                code_options = rmn.location_filter_data(load_survey_data(), ss)
                code_options = sorted(code_options.code.unique())
                groupnames = load_codes()[load_codes().code.isin(code_options)]['groupname'].unique()
                groupnames = sorted(groupnames)
                code_description = load_codes()[load_codes().code.isin(code_options)][['code', prompts_labels.key_to_code_description[ss.language]]]
                code_description = code_description.sort_values('code')
                code_description = code_description.to_dict(orient='records')
                code_description = {item['code']: item[prompts_labels.key_to_code_description[ss.language]] for item in code_description}
                ss.code_description = code_description
                # either select all object, object groups or specific objects
                if ss.object_group is not None:
                    print('checking object group')
                    if ss.object_group == 'Specific objects':
                        st.multiselect(
                            label="Select objects",
                            options=code_options,
                            format_func= lambda x: f'{x}: {ss.code_description[x]}',
                            key='selected_objects',
                            label_visibility='collapsed',
                            max_selections=5,
                        )
                        ss.selected_codes = ss.selected_objects
                    if ss.object_group == 'Object group':
                        selected_group = st.selectbox(
                            label="Select object group",
                            options=[None, *groupnames],
                            key='selected_group',
                            label_visibility='collapsed',
                            format_func=format_groupname_func
                        )
                        # if the have selected a groupname
                        # extract the codes for that group
                        if selected_group is not None:
                            selected_objects = load_codes()[load_codes().groupname == ss.selected_group]['code'].unique()
                            ss.selected_codes = selected_objects
                    if ss.object_group == 'All':
                        ss.selected_codes = code_options
                    # define the report data for the report
                    report_data = rmn.location_filter_data(load_survey_data(), ss)
                    report_data = report_data[report_data.code.isin(ss.selected_codes)]
                    their_is_not_report_data = len(report_data) == 0
                    if isinstance(report_data, pd.DataFrame):
                        st.markdown(f"**{len(report_data)}** records selected")
                    # user can generate the report
                    st.button(prompts_labels.labels['generate_report'][ss.language], key='generate_report', type='primary', disabled=their_is_not_report_data)

       
    st.button(
            label =prompts_labels.labels["reset_options"][ss.language],
            key='reset_options',
    )
    if ss["reset_options"]:
        st.markdown("resetting")

    with st.container(key='make report'):

        docs = ""
        # make the report from the survey report model
        if ss.generate_report is True:
            st.markdown(f'### {prompts_labels.labels["making_your_report"][ss.language]}')
            ss.code_material = load_codes()[['code', 'material']].set_index('code')
            # if only one region is selected
            if len(ss.selected_regions) == 1:
                doc, sections = rmn.baseline_report_and_data(report_data, ss)
                docs += doc
                ss.roughdraft = docs
            # if more than one region is selected
            if len(ss.selected_regions) > 1:
                # first make a combined report
                doc, sections = rmn.baseline_report_and_data(report_data, ss)
                docs += doc
                # make a report for each region
                for region in ss.selected_regions:
                    report_state = ss.to_dict()
                    if report_state['region'] in ['Canton', 'City']:
                        region_data = report_data[report_data[report_state['region'].lower()] == region]
                        report_state.update({'selected_regions': [region]})
                        sub_doc, sections = rmn.baseline_report_and_data(region_data, report_state)
                        docs += sub_doc
                    if report_state['region'] in ['Lake', 'River']:
                        region_data = report_data[report_data['feature_name'] == region]
                        report_state.update({'selected_regions': [region]})
                        sub_doc, sections = rmn.baseline_report_and_data(region_data, report_state)
                        docs += sub_doc
                ss.roughdraft = docs
        else:
            st.markdown(f'### {prompts_labels.labels["parameters_not_set"][ss.language]}')

    if 'roughdraft' in ss and ss.roughdraft != prompts_labels.labels["no_rough_draft_yet"][ss.language]:
        # if the report has not been sent to inference
        if 'introduction' not in ss.report_sections:
            intro_messages = prompts_labels.summarize_section_prompt(prompts_labels.introduction_prompt(ss))
            introduction = report_llm.stream(intro_messages)
            intro_stream = st.write_stream(introduction)
            ss.report_sections['introduction'] = intro_stream
        else:
            # other wise you what is in state
            st.write(ss.report_sections['introduction'])

        with st.container(key='map', border=True):
            # make a map of the selected regions
            # map config
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
            map_fig, map_markers = rmn.scatter_map(report_data, lat_lon())
            ss["map_markers"] = map_markers
            st.plotly_chart(map_fig, use_container_width=True)
        # if the admin section has not been sent to inference
        if 'admin' not in ss.report_sections:
            admin_messages = prompts_labels.summarize_section_prompt(prompts_labels.admin_prompt_cantons_lakes(ss))
            admin = report_llm.stream(admin_messages)
            admin_stream = st.write_stream(admin)
            ss.report_sections['admin'] = admin_stream
        else:
            # other wise you what is in state
            st.write(ss.report_sections['admin'])
        # make a scatter plot of the selected regions
        with st.container(key='scatterplot', border=True):
            combined_report = len(ss['selected_regions']) > 1
            if ss['region'] == 'Canton':
                if combined_report:
                    groups = ['sample_id', 'canton', 'date']
                    color_by = 'canton'
                else:
                    groups = ['sample_id', 'city', 'date']
                    color_by = 'city'
            if ss['region'] == 'City':
                groups = ['sample_id', 'city', 'date']
                color_by = 'city'
            if ss['region'] in ['Lake', 'River']:
                if combined_report:
                    groups = ['sample_id', 'feature_name', 'date']
                    color_by = 'feature_name'
                else:
                    groups = ['sample_id', 'city', 'date']
                    color_by = 'city'
            new_data = report_data.groupby(groups, as_index=False)['pcs/m'].sum()
            scatter_fig = rmn.scatterplot(new_data, color_by, ss['language'])
            st.plotly_chart(scatter_fig, use_container_width=True)
        # if the inventory section has not been sent to inference
        if 'inventory' not in ss.report_sections:
            inventory_messages = prompts_labels.summarize_section_prompt(prompts_labels.inventory_prompt(ss))
            inventory = inventory_llm.stream(inventory_messages)
            inventory_stream = st.write_stream(inventory)
            ss.report_sections['inventory'] = inventory_stream
        else:
            # other wise you what is in state
            st.write(ss.report_sections['inventory'])
        # signal the completion of the report
        ss.report = True

        st.markdown("**View the query results below**")
        with st.expander("Query results"):
            st.markdown(ss.roughdraft)

    if 'roughdraft' in ss and ss.roughdraft != prompts_labels.labels['no_rough_draft_yet'][ss.language] and ss.report == True:
        # if the rough draft has been completed
        # if the report has been sent to inference
        # enable the chat with the report
        if "messages" not in ss:
            ss.messages = []
        if "chat_history_report" not in ss:
            ss.chat_history_report = [
                AIMessage(content=prompts_labels.agent_intro[ss["language"]]),
            ]
        for message in ss.chat_history_report:
            if isinstance(message, AIMessage):
                with st.chat_message("AI"):
                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.write(message.content)
        user_query = st.chat_input("Type your message here...")
        if user_query is not None and user_query != "":
            ss.chat_history_report.append(HumanMessage(content=user_query))
            # do a vector similarity search
            context, sources = rmn.langchain_receiver(user_query)
            # add context, sources and report to prompt
            report_prompt = prompts_labels.report_chat_prompt(ss, context, sources)
            # make the agent
            the_report_agent = report_prompt | chat_llm

            with st.chat_message("Human"):
                st.markdown(user_query)

            with st.chat_message("AI"):
                query = [HumanMessage(content=user_query)]
                response = the_report_agent.stream(query)
                r = st.write_stream(response)

            ss.chat_history_report.append(AIMessage(content=r))
    else:
        st.markdown(prompts_labels.labels["no_rough_draft_yet"][ss.language])

# chat task no report
if 'current_task' in ss and ss.current_task == "chatting":
    with st.container(key='chat_container'):
        st.markdown(prompts_labels.chat_description[ss.language])
    if "messages" not in ss:
        ss.messages = []
    if "chat_history" not in ss:
        ss.chat_history = [
            AIMessage(content=prompts_labels.chat_rag[ss.language]),
        ]

    for message in ss.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        ss.chat_history.append(HumanMessage(content=user_query))
        context, sources = rmn.langchain_receiver(user_query)
        rag_sys = prompts_labels.rag_response_system_prompt(context, sources)

        the_report_agent = rag_sys | chat_llm

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            response = the_report_agent.stream([HumanMessage(content=user_query)])
            r = st.write_stream(response)
        ss.chat_history.append(AIMessage(content=r))
