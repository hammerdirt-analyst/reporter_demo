import re
import unicodedata
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from typing import List,Optional
# import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

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

# css formatting for tables
format_kwargs = dict(precision=2, thousands="'", decimal=",")

header_row = {'selector':'th', 'props': 'background-color: #FFF; font-size:14px; text-align:left; width: auto; word-break: keep-all;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': 'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 12px;'}
table_data = {'selector': 'td', 'props': 'padding:4px; font-size:12px;text-align: center;'}
table_caption_top = {'selector': 'caption', 'props': 'caption-side: top; font-size:1em; text-align: left; margin-bottom: 10px;'}
table_border = {'selector': 'table, th, tr, td', 'props': 'border: 1px solid black; border-collapse: collapse;'}

table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data, table_border, table_caption_top]

def extract_roughdraft_text(aresult):
    """Utility tool for extracting text results from collections"""

    rough = ''
    for theresult in aresult:
        label = theresult['prompt']['section_label']
        description = theresult['prompt']['section_description']
        rough += label.capitalize() +'\n\n'+ description + '\n\n'
    return rough

def clean_string(text):
    """Removes accents special characters and spaces from a string"""

    # normalize to decompose accents
    text = unicodedata.normalize("NFD", text)

    # remove accents by keeping only ASCII characters
    text = text.encode("ascii", "ignore").decode("utf-8")

    # remove special characters and spaces
    text = re.sub(r"[^a-zA-Z0-9]", "", text)

    return text

class ReportMeta(BaseModel):
    """The meta-data needed to build a report"""

    start: Optional[str] = Field(None,
                                 description="The start of the requested date range, string date in format YYYY-mm, e.g., 2020-01")
    end: Optional[str] = Field(None,
                               description="The end of the requested date range, string date in format YYYY-mm, e.g., 2020-01")
    name: Optional[str] = Field(None,
                                description="The name of the directory where the report components will be stored")
    report_codes: Optional[List[str]] = Field(None,
                                              description='The obects of interest in OSPAR or JRC code, list of strings, e.g., ["G1", "G2"]')
    code_types: Optional[List[str]] = Field(None,
                                            description='The use category of the objects ie. personal-hygiene, construction, list of strings, e.g., ["personal", "profesional"]')
    columns_of_interest: Optional[List[str]] = Field(None,
                                                     description='The feature columns for analysis list of strings, e.g., ["column", "names"]')
    info_columns: Optional[List[str]] = Field(None,
                                              description='The possible subsets in a report, list of strings, e.g., ["column", "names"]')
    feature_name: Optional[str] = Field(None,
                                        description="If the report is about a lake or river this is the name of the lake or river")
    feature_type: Optional[str] = Field(None, description="Designates the report as either river, lake or both")
    boundary: Optional[str] = Field(None,
                                    description="If the report is limited by adminstinstrative boundaries: canton, city or survey area")
    boundary_name: Optional[str] = Field(None, description="The name of the canton, city or survey area")
    title_notes: Optional[str] = Field('This is the default value of titles notes',
                                       description="String for title notes")
    code_group_category: Optional[str] = Field(None,
                                               description="The family descriptive name of the objects under consideration")
    roughdraft_name: Optional[str] = Field('rough_draft.md', description="String for rough draft name")
    report_subtitle: str = Field(
        "This the roughdraft report of the observations of trash density along rivers and lakes",
        description="String for report subtitle")
    author: str = "AI reporter from hammerdirt"
    local_directory: str = Field(None, description="The parent directory of the reports")

    @property
    def file_name(self) -> Optional[str]:
        """Defines the local directory for report components"""

        if self.name and self.code_group_category and self.local_directory:
            the_directory = clean_string(self.name + self.code_group_category)
            the_location = f'{self.local_directory}/{the_directory}/'
            return the_location
        else:
            return None

    @property
    def report_title(self) -> Optional[str]:
        """Builds the rough draft title from meta-data attributes"""

        if self.name and self.code_group_category:
            aname = self.name.capitalize()
            return f'{aname} {self.feature_type}'
        else:
            return None

    def get(self, attribute: str, default=None):
        """Retrieve the value of an attribute by name.

        Args:
            attribute (str): The name of the attribute to retrieve.
            default: The value to return if the attribute does not exist or is None.

        Returns:
            The value of the attribute or the default value if not found.
        """
        return getattr(self, attribute, default)

class SurveyReport:
    """
    The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.

    The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
    charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
    of the calculations necessary to forecast values.

    Args
    ----------
    dfc : pd.DataFrame
        The DataFrame containing the survey data.

    Methods
    -------
    administrative_boundaries() -> tuple[pd.DataFrame, dict[str, np.ndarray]]
        Returns the name and number of unique Cantons and Cities in a report.
    feature_inventory() -> tuple[pd.DataFrame, dict[str, np.ndarray]]
        Returns the name and number of geographic boundaries in a report.
    date_range() -> dict
        The date range of the selected results.
    inventory() -> pd.DataFrame
        Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report.
    total_quantity() -> int
        Returns the total quantity of the report.
    number_of_samples() -> int
        Returns the number of unique sample_ids in the report.
    number_of_locations() -> int
        Returns the number of unique locations in the report.
    material_report() -> pd.DataFrame
        Generate a report on the material composition of the samples.
    fail_rate(threshold: int = 1) -> pd.DataFrame
        Calculate the fail rate for each object of interest.
    sample_results(df: pd.DataFrame = None, sample_id: str = index_label, labels: str = location_label,
                   info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame
        Calculate the sample totals by grouping the data based on sample ID, labels, and date.
    sampling_results_summary() -> pd.DataFrame
        Generate a summary of the sample totals.
    object_summary() -> pd.DataFrame
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

        Returns
        -------
        tuple
            A tuple containing:
            - A DataFrame with the count of unique Cantons and Cities.
            - A dictionary with the names of the unique Cantons and Cities.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
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

        # result = survey_report.administrative_boundaries()[0]
        result.loc['survey areas', 'count'] = result.loc['parent_boundary', 'count']
        result.drop('parent_boundary', inplace=True)

        # d_names = survey_report.administrative_boundaries()[1]
        boundary_names['survey_area'] = boundary_names['parent_boundary']
        boundary_names.pop('parent_boundary')
        section_label = f"**Administrative boundaries**"
        section_description = "The names of the cities, cantons and survey areas included in this report:\n\n"

        place_names = ""
        for a_label, a_list in boundary_names.items():
            if a_label != location_label:
                place_names += f"{a_label.capitalize()}: {', '.join(a_list)}\n"
        section_description = section_description + place_names

        return [{'dataframe': result, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def feature_inventory(self) -> list[dict]:
        """
        Returns the name and number of geographic boundaries in a report.

        This method calculates the number of unique geographic boundaries (e.g., river basins, lakes, parks) in the survey data
        and returns a DataFrame with the counts and a dictionary with the names of the unique features.

        Returns
        -------
        List
            containing:
            - A DataFrame with the count of unique geographic boundaries.
            - A plain text interpretation and label.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
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

        section_label = "**The named features in this report**"
        section_description = "The lakes, rivers or parks included in this report\n\n"

        place_names = ""
        for a_label, a_list in feature_names.items():
            if a_label != location_label:
                place_names += f"{a_label.capitalize()}: {', '.join(a_list)}\n"
        section_description = section_description + place_names.title()
        return [{'dataframe': result,
                 'prompt': {'section_label': section_label, 'section_description': section_description}}]



    @property
    def date_range(self) -> dict:
        """The date range of the selected results"""
        start = self.df['date'].min()
        end = self.df['date'].max()
        return {'start': start, 'end': end}

    def inventory(self) -> pd.DataFrame:
        """Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report"""
        tq = self.total_quantity
        # print(self.df.columns)
        object_totals = self.df.groupby([object_of_interest, 'en'], as_index=False).agg(agg_groups)
        object_totals['% of total'] = object_totals[Q] / tq
        object_totals.rename(columns={'en': 'object'}, inplace=True)

        return object_totals

    @property
    def total_quantity(self) -> int:
        """Returns the total quantity of the report"""
        return self.df[Q].sum()

    @property
    def number_of_samples(self) -> int:
        """Returns the number of unique sample_ids in the report"""
        return self.df['sample_id'].nunique()

    @property
    def number_of_locations(self) -> int:
        """Returns the number of unique locations in the report"""
        return self.df.location.nunique()

    def material_report(self, code_material) -> list[dict]:
        """
        Generate a report on the material composition of the samples.

        This method calculates the material composition of the samples in the survey data. It groups the data by material,
        calculates the total quantity for each material, and returns a DataFrame with the percentage of the total for each material.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the percentage of the total for each material.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """

        print("Getting inventory")
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        inv = self.inventory()

        inv.set_index(object_of_interest, drop=True, inplace=True)

        inv = inv.merge(code_material, right_index=True, left_index=True)

        material_report = inv.groupby(['material']).quantity.sum()
        mr = material_report / sum(material_report)
        mr = (mr * 100).astype(int)
        mr = pd.DataFrame(mr[mr >= 1])
        mr['% of total'] = mr.quantity.apply(lambda x: f'{x}%')
        mr = mr[['% of total']]
        section_label = "Material composition"
        section_description = "The proportion of each material type according to the material classification of the object\n\n"
        section_description = section_description + mr.to_markdown()

        return [
            {'dataframe': mr, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def fail_rate(self, threshold: int = 1) -> pd.DataFrame:
        """
        Calculate the fail rate for each object of interest.

        This method calculates the fail rate for each object of interest in the survey data. The fail rate is defined as the
        number of samples where the quantity of the object is greater than or equal to the threshold, divided by the total
        number of samples for that object.

        Parameters
        ----------
        threshold : int, optional
            The quantity threshold to consider a sample as a fail. Default is 1.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the fail rate for each object of interest.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
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

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the survey data. If not provided, the method uses the instance's DataFrame. Default is None.
        sample_id : str, optional
            The column name representing the sample ID. Default is `index_label`.
        labels : str, optional
            The column name representing the location labels. Default is `location_label`.
        info_columns : list of str, optional
            Additional columns to include in the grouping. Default is None.
        afunc : dict, optional
            The aggregation function to apply to the grouped data. Default is `unit_agg`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the aggregated sample totals.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
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

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the summary of the sample totals.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        data = self.sample_results()[Y].values
        qtiles = np.quantile(data, report_quantiles)
        q_labels = {quantile_labels[i]: qtiles[i] for i in range(len(qtiles))}

        asummary = {
            'quantity': self.total_quantity,
            'nsamples': self.number_of_samples,
            'average': np.mean(data),
            **q_labels,
            'std': np.std(data),
            'max': self.sample_results()[Y].max(),
            'start': self.date_range['start'],
            'end': self.date_range['end']
        }
        result = pd.DataFrame(asummary.values(), index=list(asummary.keys()), columns=['result'])

        section_label = "**Summary statistics**"
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

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the summary of object quantities and fail rates.

        Raises
        ------
        ValueError
            If the input DataFrame is empty.
        """
        if self.df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        qtys = self.inventory()
        qtys = qtys[qtys[Q] > 0]
        qtys = qtys.sort_values(Q, ascending=False)
        qtys.rename(columns={'sample_id': 'nsamples'}, inplace=True)
        df = qtys.merge(self.fail_rate(), right_on=object_of_interest, left_on=object_of_interest)
        df = df.rename(columns={'rate': 'fail rate'})
        df.drop(columns=['fails'], inplace=True)
        section_label = "**Inventory items**"
        section_description = "The quantity, average density, % of total and fail rate per object category\n\n"
        section_description = section_description + df.to_markdown()

        return [
            {'dataframe': df, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

def survey_totals_boundary(survey_report, info_columns: list) -> dict:
    d = survey_report.sample_results(info_columns=info_columns)
    dt = d.groupby(info_columns, as_index=False).agg(agg_groups)
    dt = dt.sort_values(Y, ascending=False)
    string_columns = dt.select_dtypes(include='object').columns

    # Apply str.capitalize to all string columns
    dt[string_columns] = dt[string_columns].apply(lambda col: col.str.capitalize())
    the_theme = info_columns[0]
    if the_theme == 'parent_boundary':
        the_theme = 'survey area'
    section_label = f"**Sample results by {the_theme}**"
    section_description = f"The average sample total in pcs/m\n\n"
    section_description = section_description + dt.to_markdown()

    return {'dataframe': d, 'prompt': {'section_label': section_label, 'section_description': section_description}}

def survey_totals_for_all_info_cols(report_meta: ReportMeta, survey_report: SurveyReport) -> list[dict]:
    if 'boundary' in report_meta:
        these_cols = [x for x in report_meta.info_columns if x != report_meta['boundary']]
    else:
        these_cols = report_meta.info_columns

    results = []
    for col in these_cols:
        results.append(survey_totals_boundary(survey_report, [col]))

    return results

def translate_state_to_meta(state: dict, code_groups: pd.DataFrame, location: str, boundary: str = None) -> ReportMeta:
    """
    Converts the form state into a ReportMeta object. The ReportMeta object is used to filter the data and generate reports.

    Parameters
    ----------
    state : dict
        A dictionary containing the form state with keys such as 'start_date', 'end_date', 'feature_type', and 'codes'.
    code_groups : pd.DataFrame
        A DataFrame containing code group information.
    location : str
        The location name.
    boundary : str
        The boundary type (e.g., canton, city).

    Returns
    -------
    reporting_methods.ReportMeta
        A ReportMeta object with the necessary metadata for generating reports.
    """
    meta = {
        "name": location,
        "start": state['date_range']['start'].strftime('%Y-%m-%d'),
        "end": state['date_range']['end'].strftime('%Y-%m-%d'),
        "feature_type": state['feature_type'],
        "code_group_category": "Selected Codes",
        "boundary": boundary,
        "boundary_name": location if boundary else None,
        "feature_name": location if not boundary else None,
        "report_codes": state['selected_objects'],
        "info_columns": info_columns,
        "columns_of_interest": feature_variables
    }

    meta['report_title'] = f"{meta['name']} {meta['feature_type']}"
    meta['report_subtitle'] = f"Codes: {meta['code_group_category']}"
    meta['title_notes'] = "Proof of concept AI assisted reporting"
    meta['author'] = "hammerdirt analyst"
    meta['code_types'] = code_groups.loc[meta['report_codes']].groupname.unique().tolist()

    return ReportMeta(**meta)

def filter_dataframe_with_reportmeta(report_meta: ReportMeta, data: pd.DataFrame):
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

    if report_meta.get('start'):
        f_data = f_data[f_data['date'] >= f"{report_meta.start}"]

    if report_meta.get('end'):
        f_data = f_data[f_data['date'] <= f"{report_meta.end}"]

    if report_meta.get('boundary') and report_meta.boundary_name:
        boundary = report_meta.boundary
        boundary_name = report_meta.boundary_name
        f_data = f_data[f_data[boundary] == boundary_name]

    if report_meta.get('feature_type'):
        if report_meta.feature_type == 'lake':
            f_data = f_data[f_data['feature_type'] == 'l']
        elif report_meta.feature_type == 'river':
            f_data = f_data[f_data['feature_type'] == 'r']

    if report_meta.get('feature_name'):
        f_data = f_data[f_data['feature_name'] == report_meta.feature_name]

    if report_meta.get('report_codes'):
        codes = report_meta.report_codes
        f_data = f_data[f_data['code'].isin(codes)]

    return f_data

def baseline_report_and_data(report_meta: ReportMeta, data, material_spec):
    """Produces a rough draft report from the survey data and report meta-data"""

    df = filter_dataframe_with_reportmeta(report_meta, data)
    survey_report = SurveyReport(df)
    # baseline report sections
    admin_boundaries = extract_roughdraft_text(survey_report.administrative_boundaries())
    features = extract_roughdraft_text(survey_report.feature_inventory())
    summary_stats = extract_roughdraft_text(survey_report.sampling_results_summary)
    materials = extract_roughdraft_text(survey_report.material_report(material_spec))
    survey_totals = extract_roughdraft_text(survey_totals_for_all_info_cols(report_meta, survey_report))
    inventory = extract_roughdraft_text(survey_report.object_summary())

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

