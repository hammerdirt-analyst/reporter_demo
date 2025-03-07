openning = 'The state of things'

secondopenning = (
    "Making sense of litter counts at the beach. A practical application of citizen science:"
    " Decision Support.")

tasks = ['**Evaluate a sample / get a forecast**', '**Make a report**', '**Chat with the references**']

# Evaluate a sample
sampleExplanation = (
    "This function allows you to evaluate a beach litter inventory or get a forecast using either the surrounding"
    " land-use as a reference, one of several cantons, or one of several lakes.\n\n**Evaluate a sample:**\nIf you"
    " have a properly formatted .csv file you can upload the beach litter counts directly. If you have counts for just a"
    " few items you can enter them in a list with the chat agent. Supply the object description, the number of objects" 
    " the length in meters of beach or mountain trail, for example: _plastic bottles, 2, 50 m_.\n\n**Forecast**\nIf you want"
    " to forecast or predict quantities of specific items just enter the object description or the code. Recall that you"
    " can search for the code in the sidebar.")

properlyFormattedCsv = (
    "The .csv file should have the following columns: 'code', 'quantity', 'length'. Your data is not stored. If you want"
    " to enter your data into the reference values you need to have a login. For the moment no logins are being issued"
    " because there is no budget for ongoing operations.")

sampleTable = (
    "*Properly formatted .csv file*\n\n"
    "| code | quantity | length |\n"
    "|------|----------|--------|\n"
    "| G27   | 2        | 50     |\n"
    "| G28   | 3        | 50     |\n"
)

report_assistant_text = {
    "English": (
        "This digital assistant helps put local environmental observations in the context of regional and national strategies."
        " Plastics and other trash in the environment are a recognized nuisance. In Switzerland the population is agreed:"
        " we prefer less trash and plastics in the environment. Here you can make reports and chat with them or chat with"
        " reference documents on the subject of beach litter."

)}

what_this_reprorting_method_does = {
    "English": (
        "**What this reporting method does**\n\n"
        "This reporting method aggregates the data according to administrative boundaries or geographic boundaries."
        " Stakeholders can quickly review and compare survey results between cities, cantons, lakes or ir rivers."
        " Comparing results in this way can help identify locations that are"
        " in need of investment, or locations that are performing well in relation to their peers.\n**In the first case we"
        " identify need in the second case we identify best practices**."
         )
}

valuing_citizen_science = {
    "English": (
        "**Valuing Citizen Science**\n\nCitizen science is a valuable tool for collecting data at scale. Volunteer observations"
        " are used in ornithological and botanical studies regularly. The practical application of the data"
        " collected in citizen science projects remains limited, usually it is used for messaging or awareness campaigns."
        " However, their is a practical application of the data for monitoring and assessments. Specifically in the case"
        " of litter on the beach or in the forest. At the municipal level sampling will help identify the problem areas and"
        " can help identify the source. At the cantonal level the aggregated results will identify the most common objects"
        " that are found. Making it easy to identify priorities both geographically and in terms of object abundance."
        " \n\nThis data also serves as a field report for decision support packages that are addressing plastics in the environment."
        " Litter counts add context to the top down approach of monitoring or estimating the amount of plastic in the environment."
        " Furthermore, with this prototype these results are now easy to verify and can be used to assess progress towards a reduction goal."
        " **In this way participatory science can be used to raise awareness, advance research, inform policy and monitor progress**."
    )}

data_info_text = {
    "English": (
        "**Where does the data come from?**\n\nThe data was collected by volunteers and experts from NGOs all over Switzerland.\n\n"
        "Collecting data is simple, go to the beach, walk along the water and count and identify the man-made objects you find.\n\n"
        "**Based on field experience**, this app is built on methodologies and insights from the following works:\n\n"
        "- [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n"
        "- [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)\n"
        "- [Land Use](https://hammerdirt-analyst.github.io/landuse/titlepage.html)\n"
        "- [Plastock](https://associationsauvegardeleman.github.io/plastock/)\n"
        "- [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)\n\n"
        "**Open Source and Transparent**\n\n"
        "The app's source code, data, and documentation are available for review and collaboration:\n"
        "[Explore the documentation and source code here](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).\n\n")}

what_would_you_like_to_do = (
    "Tasks: What would you like to do?")

current_articles_rag = (
    "1. The guide for monitoring marine litter in European seas 2023\n"
    "2. Differentiating urban runoff marine transport\n"
    "3. EU marine litter baselines 2012 2016\n"
    "4. EU marine litter thresholds 2020\n"
    "5. EU Riverine shoreline litter monitoring\n"
    "6. Revealing the role of land use features on macrolitter distribution in Swiss freshwaters\n"
    "7. The Swiss Litter Report 2018\n\n")

labels = {
    "whats_this": {
        "English": "Some background information",
        "French": "Quelques informations générales",
        "German": "Einige Hintergrundinformationen"
    },
    "canton": {
        "English": ":red[Canton]",
        "French": "Canton",
        "German": "Kanton"
    },
    "city": {
        "English": ":red[City]",
        "French": "Ville",
        "German": "Stadt"
    },
    "feature_name": {
        "English": ":red[Feature Name]",
        "French": "Nom du lac/rivière",
        "German": "Merkmalsname"
    },
    "select_feature_type": {
        "English": ":red[Select feature type]",
        "French": "Sélectionnez le type de fonctionnalité",
        "German": "Funktionstyp auswählen"
    },
    "l": {"English": "Lake", "French": "Lac", "German": "See"},
    "r": {"English": "River", "French": "Rivière", "German": "Fluss"},
    "both": {"English": "Both", "French": "Les deux", "German": "Beide"},
    "nofilters": {
        "English": "You have not selected any filters. This will return all data.",
        "French": "Vous n'avez sélectionné aucun filtre. Cela renverra toutes les données.",
        "German": "Sie haben keine Filter ausgewählt. Dies wird alle Daten zurückgeben."
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
    "objects": {
        "English": "Objects of Interest",
        "French": "Objets d'intérêt",
        "German": "Interessante Objekte"
    },
    "codegroups": {
        "English": "Code Groups",
        "French": "Groupes de codes",
        "German": "Codegruppen"
    },
    "pieces_per_meter": {
        "English": "pieces/meter",
        "French": "pièces/mètre",
        "German": "Stücke/Meter"
    }
}

agent_intro = {
            "English": " ".join([
                "Hi, I am the report assistant.",
                "The rough draft is loaded and available to me.",
                "This is only a demonstration, we have started to include the reference texts in a Retrieval Augmented Generation (RAG) - set up.",
                "You can look up the available references in the side bar."
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

chat_description = {
    "English": (
        "This is where you can explore the reference documents. The available documents are listed in the in the sidebar. We are"
        " adding documents every week. So check back later if you don't find what you need. If you want to chat with the survey" 
        " results you need to make a report")
}
def introduction_prompt(state):
    """Prompt for the abstract generation task."""
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        " the introduction to the data analysis section.\n\nThe introduction must include the following information:\n\n"
        "1. The name of the  from the title.\n"
        "2. The date range covered by the samples\n3. The number of samples\n4. The number of survey locations\n5. The min, max mean and median sample results, in pcs/m"
        "6. The total quantity of objects found.\n7. The material composition of the objects found.\n8. The type of objects under consideration, either a list or the classification."
        " The classification or the list of codes is in the subject line. If the number of objects under consideration is greater than five list a few and refer the reader"
        " to the inventory. If the classification is given state the classification and refer the reader to the inventory for the complete list.\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n1. The information you need to write this is in the title, subtitle and summary statistics sections of the report above."
        "\n2. You must reply in a professional narrative style.\n3. We do not want any general closing comments. just report the facts from the provided sections of the document.\n"
        "4. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n5. Supply only the information requested.\n"
        f"6. Identify the objects under consideration in the first paragraph.\n\nPlease reply in the following language: {state['language']}."
    )
    return ''.join(aprompt)
def admin_prompt_cantons_lakes(state):
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        "  the administrative boundaries and results section of the report. This includes the following sections:\n\n"
        "1. administrative boundaries\n2. the named features in this report\n3. sample results by city\n4. sample results by canton\n5. sample results by feature_name\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n1. Summarize the sample results by city table. Include the number of cities"
        " and name the cities where the quantity is highest and lowest. Identify the cities with the greatest number of samples and the highest pcs/m.\n"
        "2. If the table 'sample results by canton' only has one row you do not need to summarize or mention it. Otherwise include the number of cantons, the canton with the greatest number of samples"
        " the canton with the highest pcs/m and the canton with the greatest quantity.\3. If their is a 'sample results by feature_name' table"
        " include the number of features: call them lakes or rivers. The lake or river with the highest pcs/m, the lake or river with the greatest number of samples and the lake or river"
        " with the highest quantity.\n4 If their is more than one row (not including the header) in the 'sample results by feature_type' table summarize the differences otherwise do not include this section.\n"
        "\n4. You must reply in a professional narrative style.\n5. We do not want any general closing comments. just report the facts from the provided sections of the document.\n"
        "6. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n7. Supply only the information requested.\n"
        f"\n\nPlease reply in the following language: {state['language']}."

            )
    return ''.join(aprompt)

def inventory_prompt(state):
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        " the inventory of objects section of the report. This includes the following sections:\n\n"
        "1. inventory items\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n"
        "**! INSTRUCTIONS**\n\n"
        "The results have a table for inventory items for each location in the title. You will produce the following summaries:\n\n"
        "1. If their are multiple inventory tables in the report will produce a summary for each. \n\n"
        "**! the general form of the summary ! :** The summary should include the top items with regards to quantity, pcs/m and the chance of finding at least one 1 and the % of total. The top items are those"
        " items when the sum of the % of total is greater than 80%. To do this you will need to sum the values in the % of total column unitll you reach 80%. Start with the first rwo\n\n"
        "**! the order of the summaries ! :** The summaries should be in the reverse order of the inventory tables in the report. The last summary should be the combined summary (the first inventory table)."
        " If their is only one inventory table summarize it.\n\n"
        
        "You must reply in a professional narrative style. We do not want any general closing comments. Just report the facts from the inventory tables.\n"
        "6. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n7. Supply only the information requested.\n"
        f"\n\nPlease reply in the following language: {state['language']}."

            )
    return ''.join(aprompt)

def reporter_prompt(state, context: str = " "):
    aprompt = (
                "You are helping a data scientist write a summary report of volunteer observations of objects found along",
                " lakes and rivers in Switzerland. The data is collected using the JRC/EU/OSPAR method for counting beach litter. This",
                " method is defined in the Guide for monitoring marine litter in european seas.",
                "The client has already prepared a rough draft of the report as well as a bar chart, scatter plot and map.",
                " Your task is to answer the clients questions reference these reports and the provided context. The client is preparing a decision",
                " support document and is relying on you for brief answers that can be supported by the documents provided",
                " below:\n\n",
                f"roughdraft: {state['roughdraft']}\n\n",
                "Furthermore a vectory similarity search has been conducted given the users questions and supporting references if their are any:\n\n",
                f"{context}\n\n",
                "!Instructions!\n\n"
                "1. The information you need to answer the clients questions is in the rough draft and the supporting references.\n"
                "2. You must reply in a professional narrative style.\n"
                "3. You are to discuss plastics, trash or litter in the environment, citizen-science, swiss or european policy concerning plastics and trash in the environment"
                "4. You will not cite non existent references or make up facts. You may complete the information with your own knowledge.\n"
                "5. Other topics of a violent, sexual or racial nature are not to be considered. You are to stick to the subject matter.\n",
            )
    return ''.join(aprompt)