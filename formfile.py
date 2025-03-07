# from os import WCONTINUED

from streamlit import session_state as ss
import streamlit as st
import pandas as pd

from dotenv import load_dotenv

import reporting_methods_new as rmn
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AIMessage
)
import prompts_labels
from prompts_labels import inventory_prompt

load_dotenv()
model_args_streaming = dict(model="gpt-4o-mini", temperature=0.4, max_tokens=2000)


@st.cache_data
def load_data():
    data = pd.read_csv('data/end_process/after_2019.csv')
    return data

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


if 'selected_regions' not in ss:
    ss.selected_regions = []
if 'selected_codes' not in ss:
    ss.selected_codes = []
if 'roughdraft' not in ss:
    ss.roughdraft = "No roughdraft yet"
if 'report' not in ss:
    ss.report = False


with st.container(key='A_form'):
    st.markdown("### You can make a report and/or compare cantons, cities, lakes or rivers")
    st.write("Start by defining what you want to report on:")
    region = st.pills(
        label="Region",
        options =["Canton", "City", "Lake", "River"],
        key='region',
        label_visibility='collapsed',
        default=None
    )

    selected_region = ss.region is not None
    if selected_region:
        selected_city_or_canton = ss.region in ['Canton', 'City']
        selected_river_or_lake = ss.region in ['Lake', 'River']
    if selected_region and selected_city_or_canton:
        st.markdown(f"Do you want to compare or report on lakes, rivers or both within the {region.lower()} boundaries?")
        feature_type = st.pills(
            label="Feature Type",
            options = ["Lake", "River", "Both"],
            key='feature_type',
            label_visibility='collapsed',
            default=None
        )
    if selected_region and selected_city_or_canton:

        if ss.feature_type is not None:

            st.markdown(f"### Select the {ss.region} of interest")
            st.markdown(f"Select up to three {ss.region.lower()}s to compare or report on.")
            options = rmn.create_regional_options(load_data(), ss.region)
            selected_regions = st.multiselect(
                label="Select regions",
                options=options,
                key='selected_regions',
                label_visibility='collapsed',
                max_selections=4,
                default=None
            )
        else:
            st.markdown("You need to decide if you want to report on lakes, rivers or both")

    elif selected_region and selected_river_or_lake:
        st.markdown(f"### Select the {ss.region} of interest")
        st.markdown(f"Select up to three {ss.region.lower()}s to compare or report on.")
        options = rmn.create_regional_options(load_data(), ss.region)
        selected_regions = st.multiselect(
            label="Select regions",
            options=options,
            key='selected_regions',
            label_visibility='collapsed',
            max_selections=4,
            default=None
        )


    if 'selected_regions' in ss and len(ss.selected_regions) > 0:

        st.markdown("### Select the objects you want to report on:")
        st.markdown(f"Do you want to report on an object group or select specific objects? If you are comparing regions we recommend selecting specific objects or object groups.")
        disabled_object_group = len(ss.selected_regions) == 0

        object_groups = st.pills(
            label="Object Group",
            options=["All", "Specific objects", "object group"],
            key='object_group',
            label_visibility='collapsed',
            disabled=disabled_object_group,
            default=None)

        if ss.object_group is not None:
            kwargs = {
                'selected_regions': ss.selected_regions,
            }
            if ss.region in ['Canton', 'City']:
                kwargs['feature_type'] = ss.feature_type
            code_options = rmn.filter_data(load_data(), ss).code.unique()
            groupnames = load_codes()[load_codes().code.isin(code_options)]['groupname'].unique()
            if ss.object_group == 'Specific objects':
                selected_objects = st.multiselect(
                    label="Select objects",
                    options=code_options,
                    key='selected_objects',
                    label_visibility='collapsed',
                    max_selections=5,

                )
                ss.selected_codes = selected_objects
            if ss.object_group == 'object group':
                selected_group = st.selectbox(
                    label="Select object group",
                    options=[None, *groupnames],
                    key='selected_group',
                    label_visibility='collapsed'
                )
                if selected_group is not None:
                    selected_objects = load_codes()[load_codes().groupname == ss.selected_group]['code'].unique()
                    ss.selected_codes = selected_objects
            if ss.object_group == 'All':
                ss.selected_codes = code_options
    else:
        st.markdown("You need to select a canton, lake, river or city to continue")
if st.button("Reset options"):
    # st.write(ss.keys())
    for key in ss.keys():
        del ss[key]

with st.container(key='make report'):
    st.markdown("### Make a report")
    docs = ""
    if 'region' not in ss or ss.region is None:
        st.markdown("You need to select region type to make a report")
    if 'selected_regions' not in ss or len(ss.selected_regions) == 0:
        st.markdown("You need to select a region to make a report")
    if 'selected_codes' in ss and len(ss.selected_codes) == 0:
        st.markdown("You need to select objects to make a report")
    elif 'selected_codes' in ss and len(ss.selected_codes) > 0:
        code_description = load_codes()[['code', 'en']]
        code_description = code_description.to_dict(orient='records')
        code_description = {item['code']: item['en'] for item in code_description}
        ss.language = 'English'
        # st.write(code_description)
        ss.code_description = code_description
        # st.write(code_description)
        report_data = rmn.filter_data(load_data(), ss)
        code_material = load_codes()[['code', 'material']].set_index('code')
        ss.code_material = code_material
        if len(ss.selected_regions) == 1:
            doc, sections = rmn.baseline_report_and_data(report_data, ss)
            docs += doc
            ss.roughdraft = docs

        if len(ss.selected_regions) > 1:
            # data = filter_data(load_data(), ss)
            # code_material = load_codes()[['code', 'material']].set_index('code')
            # ss.code_material = code_material
            doc, sections = rmn.baseline_report_and_data(report_data, ss)
            docs += doc
            for region in ss.selected_regions:
                report_state = ss.to_dict()
                # st.write(report_state)
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

if 'roughdraft' in ss and ss.roughdraft != "No roughdraft yet" and ss.report == False:

    current_llm = ChatOpenAI(**model_args_streaming)

    intro_prompt = prompts_labels.introduction_prompt(ss)
    messages = [
        SystemMessage(
            content="Follow the instruction in the message"),

        HumanMessage(content=intro_prompt)

    ]
    introduction = current_llm.stream(messages)
    intro_stream = st.write_stream(introduction)

    with st.container(key='map', border=True):
        st.markdown("### Map of survey locations")

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
        # chart_data = st.session_state.get("filtered_data", pd.DataFrame())
        map_fig, map_markers = rmn.scatter_map(report_data, lat_lon())
        st.session_state["map_markers"] = map_markers
        st.plotly_chart(map_fig, use_container_width=True)
    admin_prompt = prompts_labels.admin_prompt_cantons_lakes(ss)
    messages = [
        SystemMessage(
            content="Follow the instruction in the message"),

        HumanMessage(content=admin_prompt)

    ]
    admin = current_llm.stream(messages)
    admin_stream = st.write_stream(admin)
    with st.container(key='scatterplot', border=True):
        st.markdown("### Scatterplot of survey results")
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

    inventory_prompt = prompts_labels.inventory_prompt(ss)
    messages = [
        SystemMessage(
            content="Follow the instruction in the message"),

        HumanMessage(content=inventory_prompt)

    ]
    inventory = current_llm.stream(messages)
    inventory_stream = st.write_stream(inventory)
    ss.report = True
    with st.expander("Roughdraft"):
        st.markdown(ss.roughdraft)
if 'roughdraft' in ss and ss.roughdraft != "No roughdraft yet" and ss.report == True:
    current_llm = ChatOpenAI(**model_args_streaming)
    if "messages" not in ss:
        ss.messages = []
    # the_report_prompt = prompts.reporter_prompt(
    #     st.session_state['abstract'],
    #     st.session_state["scatterplot_caption"],
    #     st.session_state["barchart_caption"],
    #     st.session_state["inventory"],
    #     st.session_state["rough_drafts"],
    #     )



    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content=prompts_labels.agent_intro[ss["language"]]),
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
        docs, context = rmn.langchain_receiver(user_query)
        print(context)

        the_report_prompt = prompts_labels.reporter_prompt(ss)


        a_report_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    the_report_prompt
                ), MessagesPlaceholder(variable_name="messages")
            ]
        )

        the_report_agent = a_report_prompt | current_llm

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            query = [HumanMessage(content=user_query)]
            response = the_report_agent.stream(query)
            r = st.write_stream(response)

        st.session_state.chat_history.append(AIMessage(content=r))
else:
    st.markdown("No roughdraft yet")






