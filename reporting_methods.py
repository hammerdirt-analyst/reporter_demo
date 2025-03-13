"""
reporting_methods.py
author: roger erismann
purpose: submission to prototypefund.opendata.ch

This module contains the methods used to generate a report from beach litter observations. This includes filter methods,
map generation and scatter plot generation. The data used is from beach litter observtions using the MLW/OSPAR method of
object categorization.

This is a prototype that is/was (depending on when you are reading this) being developed for the prototype fund competition.

The purpose or use case for this module is to create quick summaries and comparisons of beach litter observations. The use
case is for researchers as a 'kick start' to their analysis and for stakeholders to get a quick summary of the data.

The vector database is for the rag application.
"""
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px
import prompts_labels
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
import os
from dotenv import load_dotenv

load_dotenv()

# The following are the default values for the report
report_quantiles = [.05, .25, .5, .75, .95]
quantile_labels = ['5th', '25th', '50th', '75th', '95th']
object_of_interest = 'code'
location_label = 'location'
feature_variables = ['buildings', 'forest', 'public-services', 'recreation', 'undefined', 'streets']
info_columns = ['canton', 'city', 'feature_name', 'feature_type']

# indentify target variable and type
Y = 'pcs/m'
Q = 'quantity'

# distribution point estimate
tendencies = 'mean'
# these are the columns and methods used to aggregate the data at the sample level
# the sample level is the lowest level of aggregation. The sample level is the collection of all
# the records that share the same sample_id or loc_date. The loc_date is the unique identifier for each survey.
unit_agg = {
    Q: "sum",
    Y: "sum"
}

# Once the data is aggregated at the sample level, it is aggregated at the feature level. The pcs/m or pcs_m
# column can no longer be summed. We can only talk about the median, average or distribution of the pcs/m for the
# samples contained in each feature. The quantity column can still be summed. The median is used for reporting
# purposes. The median is less sensitive to outliers than the average. The median is also more intuitive than the
# average.
agg_groups = {
    Q: "sum",
    Y: tendencies
}

# connection to vector store
query_embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
consumer = os.getenv("MONGO_DB_CONSUMER_URI")
def langchain_receiver(message: str) -> []:

    vectorstore = MongoDBAtlasVectorSearch.from_connection_string(
        connection_string=consumer,
        namespace = "ragtest.textchunks",
        embedding = query_embedding,
        index_name = "vector_index_rag",
        embedding_key = "embeddings",
        text_key = "content"
        )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5}, search_type='similarity')
    docs = retriever.invoke(message)
    content = [x.page_content for x in docs]
    sources = list(set([x.metadata['source'] for x in docs]))
    context = '\n\n'.join(content)

    return context, sources

def create_regional_options(data, region):
    if region in ['Canton', 'City']:
        label = region.lower()
        options = data[label].unique()
        return options
    if region in ['Lake', 'River']:
        label = region.lower()[0]
        options = data[data.feature_type == label]['feature_name'].unique()
        return options

def location_filter_data(data, state):
    if state.region in ['Canton', 'City']:
        label = state.region.lower()
        region_mask = data[label].isin(state.selected_regions)
        if state.feature_type in ['Lake', 'River']:
            feature_type = state.feature_type.lower()[0]
            mask = (data.feature_type == feature_type) & region_mask
        else:
            mask = region_mask
        return data[mask]
    if state.region in ['Lake', 'River']:
        mask = data.feature_name.isin(state.selected_regions)
        return data[mask]

def extract_roughdraft_text(aresult: list[dict]) -> str:
    """
    Extracts text results from a collection of dictionaries.

    This utility function iterates through a list of dictionaries, extracting the 'section_label' and 'section_description' from each dictionary's 'prompt' key. The extracted text is concatenated into a single string.

    Args:
        aresult (list[dict]): A list of dictionaries containing the text results to be extracted.

    Returns:
        str: A concatenated string of the extracted text results.
    """

    rough = ''
    for theresult in aresult:
        label = theresult['prompt']['section_label']
        description = theresult['prompt']['section_description']
        rough += label.capitalize() +'\n\n'+ description + '\n\n'
    return rough

class SurveyReport:
    """
    The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.

    The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
    charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
    of the calculations necessary to forecast values.

    Args:
        dfc (pd.DataFrame): The DataFrame containing the survey data.

    Methods:
        administrative_boundaries() -> list[dict]:
            Returns the name and number of unique Cantons and Cities in a report.
        feature_inventory() -> list[dict]:
            Returns the name and number of geographic boundaries in a report.
        date_range() -> dict:
            The date range of the selected results.
        inventory() -> pd.DataFrame:
            Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report.
        total_quantity() -> int:
            Returns the total quantity of the report.
        number_of_samples() -> int:
            Returns the number of unique sample_ids in the report.
        number_of_locations() -> int:
            Returns the number of unique locations in the report.
        material_report(code_material) -> list[dict]:
            Generate a report on the material composition of the samples.
        fail_rate(threshold: int = 1) -> pd.DataFrame:
            Calculate the fail rate for each object of interest.
        sample_results(df: pd.DataFrame = None, sample_id: str = None, labels: str = None, info_columns: list[str] = None, afunc: dict = None) -> pd.DataFrame:
            Calculate the sample totals by grouping the data based on sample ID, labels, and date.
        sampling_results_summary() -> list[dict]:
            Generate a summary of the sample totals.
        object_summary() -> list[dict]:
            Generate a summary of the object quantities and fail rates.
    """

    def __init__(self, dfc):
        self.df = dfc
        self.administrative = [location_label, 'city', 'canton', 'parent_boundary']

    def administrative_boundaries(self) -> list[dict]:
        """
        Returns the name and number of unique Cantons and Cities in a report.

        This method calculates the number of unique Cantons and Cities in the survey data and returns a DataFrame
        with the counts and a dictionary with the names of the unique Cantons and Cities.

        Returns:
            list[dict]: A list containing a dictionary with a DataFrame of the count of unique Cantons and Cities,
                        and a dictionary with the names of the unique Cantons and Cities.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        result = {}
        boundary_names = {}
        for boundary in self.administrative:
            names = self.df[boundary].unique()
            boundary_names[boundary] = names
            if names.size == 0:
                result[boundary] = {'count': 0}
            else:
                result[boundary] = {'count': len(names)}
        result = pd.DataFrame(result).T

        result.loc['survey areas', 'count'] = result.loc['parent_boundary', 'count']
        result.drop('parent_boundary', inplace=True)

        # boundary_names['survey_area'] = boundary_names['parent_boundary']
        boundary_names.pop('parent_boundary')
        section_label = f"### Administrative boundaries"
        section_description = "The names of the cities, cantons and survey areas included in this report:\n\n"

        place_names = ""
        for a_label, a_list in boundary_names.items():
            if a_label != location_label:
                place_names += f"{a_label.capitalize()}: {', '.join(a_list)}\n\n"
        section_description = section_description + place_names

        return [{'dataframe': result, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def feature_inventory(self) -> list[dict]:
        """
        Returns the name and number of geographic boundaries in a report.

        This method calculates the number of unique geographic boundaries (e.g., river basins, lakes, parks) in the survey data
        and returns a DataFrame with the counts and a dictionary with the names of the unique features.

        Returns:
            list[dict]: A list containing a dictionary with a DataFrame of the count of unique geographic boundaries,
                        and a dictionary with the names of the unique features.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        result = {}
        feature_names = {}
        feature_type_labels = {'l': 'lake', 'r': 'river', 'p': 'park'}
        for feature_type in self.df.feature_type.unique():
            unique_features = self.df[self.df['feature_type'] == feature_type]['feature_name'].unique()
            ftype_label = feature_type_labels[feature_type]
            feature_names[ftype_label] = unique_features
            if unique_features.size > 0:
                result[feature_type] = {'count': len(unique_features)}
        result = pd.DataFrame(result)
        result.rename(columns={'l': 'lake', 'r': 'river', 'p': 'park'}, inplace=True)

        section_label = "### The named features in this report"
        section_description = "The lakes, rivers or parks included in this report\n\n"

        place_names = ""
        for a_label, a_list in feature_names.items():
            if a_label != location_label:
                place_names += f"**{a_label.capitalize()}:** {', '.join(a_list)}\n\n"
        section_description = section_description + place_names.title()
        return [{'dataframe': result,
                 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    @property
    def date_range(self) -> dict:
        """
        The date range of the selected results.

        Returns:
            dict: A dictionary with the start and end dates of the selected results.
        """
        start = self.df['date'].min()
        end = self.df['date'].max()
        return {'start': start, 'end': end}

    def inventory(self) -> pd.DataFrame:
        """
        Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report.

        Returns:
            pd.DataFrame: A DataFrame containing the total quantity, median pcs/m, % of total and fail rate for each object code.
        """
        tq = self.total_quantity
        object_totals = self.df.groupby([object_of_interest, 'en'], as_index=False).agg(agg_groups)
        object_totals['% of total'] = object_totals[Q] / tq
        object_totals.rename(columns={'en': 'object'}, inplace=True)

        return object_totals

    @property
    def total_quantity(self) -> int:
        """
        Returns the total quantity of the report.

        Returns:
            int: The total quantity of the report.
        """
        return self.df[Q].sum()

    @property
    def number_of_samples(self) -> int:
        """
        Returns the number of unique sample_ids in the report.

        Returns:
            int: The number of unique sample_ids in the report.
        """
        return self.df['sample_id'].nunique()

    @property
    def number_of_locations(self) -> int:
        """
        Returns the number of unique locations in the report.

        Returns:
            int: The number of unique locations in the report.
        """
        return self.df.location.nunique()

    def material_report(self, code_material) -> list[dict]:
        """
        Generate a report on the material composition of the samples.

        This method calculates the material composition of the samples in the survey data. It groups the data by material,
        calculates the total quantity for each material, and returns a DataFrame with the percentage of the total for each material.

        Args:
            code_material (pd.DataFrame): A DataFrame containing the material classification of the objects.

        Returns:
            list[dict]: A list containing a dictionary with a DataFrame of the material composition,
                        and a dictionary with the section label and description.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        inv = self.inventory()
        inv.set_index(object_of_interest, drop=True, inplace=True)
        inv = inv.merge(code_material, right_index=True, left_index=True)
        print('this is an m report\n')
        m_report = inv.groupby(['material']).quantity.sum()
        if sum(m_report) > 0:
            mr = m_report / sum(m_report)
        else:
            mr = m_report
        print('this is an mr\n')
        print(mr)
        mr = (mr * 100).astype(int)
        mr = pd.DataFrame(mr[mr >= 1])
        mr['% of total'] = mr.quantity.apply(lambda x: f'{x}%')
        mr = mr[['% of total']]
        section_label = "### Material composition"
        section_description = "The proportion of each material type according to the material classification of the object\n\n"
        section_description = section_description + mr.to_markdown()

        return [{'dataframe': mr, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def fail_rate(self, threshold: int = 1) -> pd.DataFrame:
        """
        Calculate the fail rate for each object of interest.

        This method calculates the fail rate for each object of interest in the survey data. The fail rate is defined as the
        number of samples where the quantity of the object is greater than or equal to the threshold, divided by the total
        number of samples for that object.

        Args:
            threshold (int, optional): The quantity threshold to consider a sample as a fail. Default is 1.

        Returns:
            pd.DataFrame: A DataFrame containing the fail rate for each object of interest.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        rates = self.df.groupby([object_of_interest])['sample_id'].nunique().reset_index()
        for anobject in rates[object_of_interest].unique():
            nfails = sum((self.df[object_of_interest] == anobject) & (self.df[Q] >= threshold))
            n_anobject = rates.loc[rates[object_of_interest] == anobject, 'sample_id'].values[0]
            rates.loc[rates[object_of_interest] == anobject, ['fails', 'rate']] = [nfails, nfails / n_anobject]

        return rates.set_index(object_of_interest, drop=True)

    def sample_results(self, df: pd.DataFrame = None, sample_id: str = None, labels: str = None,
                       info_columns: list[str] = None, afunc: dict = None) -> pd.DataFrame:
        """
        Calculate the sample totals by grouping the data based on sample ID, labels, and date.

        This function groups the data by sample ID, labels, and date, and applies the aggregation function to calculate
        the sample totals. If additional information columns are provided, they are included in the grouping.

        Args:
            df (pd.DataFrame, optional): The DataFrame containing the survey data. If not provided, the method uses the instance's DataFrame. Default is None.
            sample_id (str, optional): The column name representing the sample ID. Default is `index_label`.
            labels (str, optional): The column name representing the location labels. Default is `location_label`.
            info_columns (list[str], optional): Additional columns to include in the grouping. Default is None.
            afunc (dict, optional): The aggregation function to apply to the grouped data. Default is `unit_agg`.

        Returns:
            pd.DataFrame: A DataFrame containing the aggregated sample totals.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if df is None:
            df = self.df
        if labels is None:
            labels = location_label
        if sample_id is None:
            sample_id = "sample_id"
        if afunc is None:
            afunc = unit_agg


        if df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        if not info_columns:
            return df.groupby([sample_id, labels, 'date'], as_index=False).agg(afunc)
        else:
            return df.groupby([sample_id, labels, 'date', *info_columns], as_index=False).agg(afunc)

    @property
    def sampling_results_summary(self) -> list[dict]:
        """
        Generate a summary of the sample totals.

        This property calculates the summary of the sample totals, including total quantity, number of samples, average,
        quantiles, standard deviation, maximum value, and date range.

        Returns:
            list[dict]: A list containing a dictionary with a DataFrame of the summary of the sample totals,
                        and a dictionary with the section label and description.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        data = self.sample_results()[Y].values
        qtiles = np.quantile(data, report_quantiles)
        q_labels = {quantile_labels[i]: qtiles[i] for i in range(len(qtiles))}

        asummary = {
            'quantity': self.total_quantity,
            'nsamples': self.number_of_samples,
            'nlocations': self.number_of_locations,
            'average': np.mean(data),
            **q_labels,
            'std': np.std(data),
            'max': self.sample_results()[Y].max(),
            'start': self.date_range['start'],
            'end': self.date_range['end']
        }
        result = pd.DataFrame(asummary.values(), index=list(asummary.keys()), columns=['result'])

        section_label = "### Summary statistics"
        section_description = ("The average pcs/m (objects per meter or trash per meter), standard deviation, "
                               "number of samples, date range, and the percentile distribution of the survey totals.\n\n")
        section_description = section_description + result.to_markdown() + '\n'

        return [{'dataframe': result,
                 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def object_summary(self) -> list[dict]:
        """
        Generate a summary of the object quantities and fail rates.

        This method calculates the total quantity and fail rate for each object of interest in the survey data. It filters
        out objects with zero quantity, sorts the objects by quantity in descending order, and merges the fail rate data.

        Returns:
            list[dict]: A list containing a dictionary with a DataFrame of the summary of object quantities and fail rates,
                        and a dictionary with the section label and description.

        Raises:
            ValueError: If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        qtys = self.inventory()
        qtys = qtys[qtys[Q] > 0]
        qtys = qtys.sort_values(Q, ascending=False)
        qtys.rename(columns={'sample_id': 'nsamples'}, inplace=True)
        df = qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
        df = df.rename(columns={'rate': 'chance of finding at least 1'})
        df.drop(columns=['fails', 'sample_id'], inplace=True)
        section_label = "### Inventory items"
        section_description = "The quantity, average density, % of total and fail rate per object category\n\n"
        section_description = section_description + df.to_markdown()

        return [{'dataframe': df, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

def survey_totals_boundary(survey_report: SurveyReport, info_columns: list) -> dict:
    """
    Generates a summary of sample results grouped by specified information columns.

    This function groups the survey data by the specified information columns, calculates the total quantity and pcs/m for each group, and sorts the results in descending order of pcs/m. It also capitalizes string columns and generates a section label and description for the report.

    Args:
        survey_report (SurveyReport): An instance of `SurveyReport` containing the survey data.
        info_columns (list): A list of column names to group the data by.

    Returns:
        dict: A dictionary containing the DataFrame of grouped sample results and a dictionary with the section label and description.
    """
    d = survey_report.sample_results(info_columns=info_columns)
    agg_groups.update({'sample_id': 'nunique'})
    dt = d.groupby(info_columns, as_index=False).agg(agg_groups)
    dt.rename(columns={'sample_id': 'nsamples'}, inplace=True)
    dt = dt.sort_values(Y, ascending=False)
    dt.reset_index(drop=True, inplace=True)
    string_columns = dt.select_dtypes(include='object').columns

    # Apply str.capitalize to all string columns
    dt[string_columns] = dt[string_columns].apply(lambda col: col.str.capitalize())
    the_theme = info_columns[0]
    section_label = f"### Sample results by {the_theme}"
    section_description = f"The average sample total in pcs/m\n\n"
    section_description = section_description + dt.to_markdown()

    return {'dataframe': d, 'prompt': {'section_label': section_label, 'section_description': section_description}}

def survey_totals_for_all_info_cols(survey_report: SurveyReport, topic: str = None) -> list[dict]:
    """
    Generates a summary of sample results for all specified information columns.

    This function iterates through the information columns specified in the `ReportMeta` object, groups the survey data by each column, calculates the total quantity and pcs/m for each group, and generates a section label and description for the report.

    Args:
        report_meta (ReportMeta): An instance of `ReportMeta` containing the metadata for filtering and generating the report.
        survey_report (SurveyReport): An instance of `SurveyReport` containing the survey data.

    Returns:
        list[dict]: A list of dictionaries, each containing a DataFrame of grouped sample results and a dictionary with the section label and description.
    """
    these_cols = []
    if topic == 'Canton':
        these_cols = ['city', 'feature_name', 'feature_type']
    if topic in ['Lake', 'River']:
        these_cols = ['canton', 'city', 'feature_type']
    if topic == 'City':
        these_cols = ['feature_type', 'feature_name']

    results = []
    for col in these_cols:
        results.append(survey_totals_boundary(survey_report, [col]))

    return results

def baseline_report_and_data(data: pd.DataFrame, state: dict = None) -> str:
    """
    Produces a rough draft report from the survey data and report meta-data.

    This function filters the survey data based on the conditions provided in the `ReportMeta` object, generates various sections of the report, and concatenates them into a rough draft report.

    Args:
        report_meta (ReportMeta): An instance of `ReportMeta` containing the metadata for filtering and generating the report.
        data (pd.DataFrame): The DataFrame containing the survey data.
        material_spec (pd.DataFrame): A DataFrame containing the material classification of the objects.

    Returns:
        str: A concatenated string representing the rough draft report.
    """
    # report title section
    title_labels = ', '.join(state['selected_regions'])
    date_min, date_max = data['date'].min(), data['date'].max()
    title = ""
    if len(state['selected_regions']) == 1:
        title += f"## Beach litter survey report for {state['region']}: {title_labels}\n"
    else:
        title += f"## Combined beach litter survey report for {state['region']}(s): {title_labels}\n"

    if state["object_group"] == "All":
        objects = "all objects found, see inventory for complete list"
    if state["object_group"] == "Specific objects":
        descriptions = [state['code_description'][x].lower() for x in state['selected_objects']]
        objects = ', '.join(descriptions)
    if state["object_group"] == "Object group":
        objects = f"objects from {state['selected_group']}"

    subject = "**Subject:** " + 'shoreline litter observations of' + " " + objects + "\n\n"
    dates = f"**Date range:** {date_min} to {date_max}\n\n"
    author = "**Author:** " + "hammerdirt analyst" + "\n\n"
    intro = f'{title}{subject}{dates}{author}'

    survey_report = SurveyReport(data)
    # baseline report sections
    admin_boundaries = extract_roughdraft_text(survey_report.administrative_boundaries())
    features = extract_roughdraft_text(survey_report.feature_inventory())
    summary_stats = extract_roughdraft_text(survey_report.sampling_results_summary)
    materials = extract_roughdraft_text(survey_report.material_report(state['code_material']))
    survey_totals = extract_roughdraft_text(survey_totals_for_all_info_cols(survey_report, state['region']))
    inventory = extract_roughdraft_text(survey_report.object_summary())

    sections = [intro, summary_stats, admin_boundaries, features, materials, survey_totals, inventory]

    doc = " "
    for section in sections:
        doc += section + "\n"

    return doc, sections

def compute_similarity_matrix(dataframe, columns, id_column, column_to_normalize):
    """
    Computes a cosine similarity matrix for specified columns in a DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame containing data.
        columns (list): List of columns to compute similarity on.
        id_column (str): Column name to use as row and column labels in the output matrix.
        column_to_normalize (str): Column that needs to be separately normalized.

    Returns:
        pd.DataFrame: A DataFrame representing the cosine similarity matrix.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df = dataframe.copy()

    # Normalize the specified column separately
    scaler = MinMaxScaler()
    df[column_to_normalize] = scaler.fit_transform(df[[column_to_normalize]])

    # Use the specified columns for similarity calculation
    features = df[columns]

    # Compute cosine similarity
    similarity_matrix = cosine_similarity(features)

    # Convert the matrix to a DataFrame for better readability
    similarity_df = pd.DataFrame(similarity_matrix,
                                 index=df[id_column],
                                 columns=df[id_column])
    return similarity_df

def map_markers(f_data: pd.DataFrame, map_coords: pd.DataFrame) -> pd.DataFrame:
    """
    Generates the data for the map markers. Includes, number of samples, quantity, pcs/m, and last sample date.
    for each location.

    Args:
        f_data (pd.DataFrame): Filtered data containing survey results.
        map_coords (pd.DataFrame): DataFrame containing the coordinates (latitude and longitude).

    Returns:
        pd.DataFrame: DataFrame containing the merged data with map markers.
    """
    nsamples = f_data.groupby('location', observed=True)['sample_id'].nunique()
    qty_location = f_data.groupby('location', observed=True)['quantity'].sum()
    rate_location = f_data.groupby('location', observed=True)['pcs/m'].mean().round(2)
    last_sample = f_data.groupby('location', observed=True)['date'].max()

    df = pd.concat([nsamples, qty_location, rate_location, last_sample], axis=1)
    df = df.merge(map_coords[['longitude', 'latitude']], left_index=True, right_index=True)
    df['location'] = df.index
    df.rename(columns={'sample_id': 'nsamples', 'date': 'last sample'}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def scatter_map(f_data: pd.DataFrame, map_coords: pd.DataFrame) -> tuple[px.scatter_map, pd.DataFrame]:
    """
    Generates a map with markers using Plotly's scatter_map.
    - Markers use lat/lon from map_markers.
    - Hover information includes samples, quantity, pcs/m, and last sample date.

    Args:
        f_data (pd.DataFrame): Filtered data containing survey results.
        map_coords (pd.DataFrame): DataFrame containing the coordinates (latitude and longitude).

    Returns:
        tuple: A tuple containing the Plotly scatter map figure and the DataFrame with map markers.
    """
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

def scatterplot(data: pd.DataFrame, color_by: [], language: str) -> px.scatter:
    """
    Creates a scatter plot.

    Returns:
        px.scatter: The generated Plotly scatter plot figure.
    """

    fig = px.scatter(
        data,
        x="date",
        y="pcs/m",
        color=color_by,
        labels={"date": "", "pcs/m": prompts_labels.labels["pieces_per_meter"][language]},
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