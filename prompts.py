language_column_map = {"English": "en", "French": "fr", "German": "de"}
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
        " These observations are given in pieces per meter per sample. A sample is defined by a location and a date",
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


def barchart_prompt(data, grouped_data, x_axis, y_axis, language):
    """Creates a prompt for a barchart given the data and the x and y axis labels"""

    # grouped_data = handle_grouped_data_for_barchart(data, x_axis, y_axis)
    feature_type = data['feature_type'].unique()
    if len(feature_type) > 1:
        lakes_or_rivers = "lakes and rivers"
    elif feature_type[0] == 'l':
        lakes_or_rivers = "lakes"
    else:
        lakes_or_rivers = "rivers"
    c_selected = data['canton'].unique()
    description_column = language_column_map[language]
    objects = data[description_column].unique()
    prompt = (
        f"You are a data scientist. You are writing the description of the data from a bar plot. The data is  from"
        f" observations of {', '.join(objects)} found along {lakes_or_rivers} in {', '.join(c_selected)}. The data has been selected by the client."
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

def reporter_prompt(summary, scatterplot, barchart, inventory, rough_draft):
    aprompt = (
                "You are helping a data scientist write a summary report of volunteer observations of objects found along",
                " lakes and rivers in Switzerland. The data is collected using the JRC/EU method counting beach litter. This",
                " method is defined in the _Guide for monitoring marine litter in european seas. Your other reference document",
                " is the federal report on litter density of swiss lakes (IQAASL) published in 2021 and available here:\n\n",
                "[IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n\n",
                "The client has already prepared a rough draft of the report as well as a bar chart, scatter plot and map.",
                " Your task is to answer the clients questions reference these reports. The client is preparing a decision",
                " support document and is relying on your for brief answers that can be supported by the documents provided",
                " below or the previously mentioned references. The client has provided the following documents:\n\n",
                f"summary: {summary}\n\n",
                f"scatterplot: {scatterplot}\n\n",
                f"barchart: {barchart}\n\n",
                f"inventory: {inventory}\n\n",
                f"rough draft: {rough_draft}\n\n",
                "!Instructions!\n\n"
                "The column names and descriptions for inventory items:\n1. object: the use or plain language description"
                "\n2. code: the MLW code for the item\n3. quantity: the total number of items found\n4. pcs/m: the average number"
                " of items per meter of shoreline.\n5 % of total: the proportion of the current set of data.\n6. number of samples:"
                " the number of samples collected\n7. fail rate: the proportion of samples that contained the objects\n\n",
                "You are to discuss plastics, trash or litter in the environment, citizen-science, swiss or european policy",
                " concerning plastics and trash in the environment, probability and statistics, calculus, bayes theorem, bayesian statistics",
                " other topics of a sensitive or sexual nature are not to be considered.",
            )
    return ''.join(aprompt)