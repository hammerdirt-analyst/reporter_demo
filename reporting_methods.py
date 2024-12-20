import re
import unicodedata
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pydantic import BaseModel, Field
from typing import List,Optional
report_quantiles = [.05, .25, .5, .75, .95]
quantile_labels = ['5th', '25th', '50th', '75th', '95th']
bin_labels = [1, 2, 3, 4, 5]


color_style = {'prior':'#daa520', 'likelihood':'#1e90ff'}
palette = {'prior':'goldenrod', 'likelihood':'dodgerblue'}

format_kwargs = dict(precision=2, thousands="'", decimal=",")

# this defines the css rules for the table displays
header_row = {'selector':'th', 'props': 'background-color: #FFF; font-size:14px; text-align:left; width: auto; word-break: keep-all;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': 'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 12px;'}
table_data = {'selector': 'td', 'props': 'padding:4px; font-size:12px;text-align: center;'}
table_caption = {'selector': 'caption', 'props': 'caption-side: bottom; font-size:1em; text-align: left;'}
table_caption_top = {'selector': 'caption', 'props': 'caption-side: top; font-size:1em; text-align: left; margin-bottom: 10px;'}
caption_css = {'selector': 'caption', 'props': 'caption-side: top; font-size:.9em; text-align: left; font-style: italic; color: #000;'}
table_first_column_left = {'selector': 'td:nth-child(1)', 'props': 'text-align: left;'}
table_border = {'selector': 'table, th, tr, td', 'props': 'border: 1px solid black; border-collapse: collapse;'}

table_css_styles = [even_rows, odd_rows, table_font, header_row, table_data, table_border, table_caption_top]
highlight_props = 'background-color:#FAE8E8'

def style_negative(v, props=''):
    """from panaas docs: pandas-docs/version/0.24.2/reference/api/pandas.io.formats.style.Styler.applymap.html"""
    return props if v < 0 else None

def highlight_max(s, props: str = highlight_props):
    return np.where((s == np.max(s.values)) & (s != 1), props, '')

land_use_rates_description = (
    "\nThe sampling stratification and trash density table quantifies the change in trash density based on the proportion of the buffer " 
    "zone that is dedicated to a particular land use feature. Each survey location is surrounded by a buffer zone of radius = 1 500 meters. "
    "The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). "
    "The sampling stratification and trash density table quantifies the change in trash density based on the proportion of the "
    "buffer zone that is dedicated to a particular land use feature.\n"
)
land_use_description = (
    "\nEach survey location is surrounded by a buffer zone of radius = 1 500 meters. "
    "The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). "
    "The land-use-profile is measured by considering the dry land proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. "
    "Each location has the same size buffer zone. For lakeside locations the surface area of the water feature is substracted from the buffer surface area. "
    "What changes is how the land use features are distributed within the buffer zone. We assume that locations that have a similar distribution of features in "
    "the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and "
    "what proportions of the samples were taken according to those conditions.\n"
)
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
    Y: "median"
}

report_quantiles = [.05, .25, .5, .75, .95]
quantile_labels = ['5th', '25th', '50th', '75th', '95th']
object_of_interest = 'code'
location_label = 'location'
feature_variables = ['buildings', 'forest', 'public-services', 'recreation', 'undefined', 'streets']
info_columns = ['canton', 'city', 'feature_name', 'feature_type']


def make_report_objects(df: pd.DataFrame, feature_variables: list[str] = None, info_columns: list[str] = None) -> tuple:
    """
    Create SurveyReport and LandUseReport objects from the given DataFrame.

    This function creates a SurveyReport object and a LandUseReport object from the provided DataFrame.
    It first generates the parameters for the LandUseReport and then creates the LandUseReport using
    the target DataFrame and features.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the survey data.
    connection_string : str
        The connection string for the database.
    info_columns : list[str], optional
        Additional columns to include in the sample results. Default is None.

    Returns
    -------
    tuple
        A tuple containing the SurveyReport and LandUseReport objects.

    Raises
    ------
    ValueError
        If the input DataFrame is empty.
    """
    if df.empty:
        raise ValueError("No data in the DataFrame. Please check the query parameters and try again.")

    this_report = SurveyReport(dfc=df)

    target_df = this_report.sample_results(info_columns=info_columns)

    landuse_df = target_df.merge(df[[*feature_variables, 'location']], left_on='location', right_on='location')

    this_land_use = LandUseReport(landuse_df, feature_variables)

    return this_report, this_land_use

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

class SurveyReport:
    """
    The SurveyReport class is a container for the data and methods that are used to generate a report from a survey data set.

    The report is a summary of the data in the survey. The exact contents of the report should be defined by the stakeholders
    charged with the responsibility of interpreting the data. This has not happened. Therefore, this report is the byproduct
    of the calculations necessary to forecast values.

    Combined with the LandUseReport class, it is possible to describe the sampling conditions of a survey in a quantitative
    scale. Therefore, if the data in the report is a collection of like items, the report can be used to describe the
    concentration of the items per meter given the environmental conditions of the survey.

    Args
    ----------
    df : pd.DataFrame
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
        self.administrative = ['location', 'city', 'canton', 'parent_boundary']

    def administrative_boundaries(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
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

        administrative = ['location', 'city', 'canton', 'parent_boundary']

        result = {}
        boundary_names = {}
        for boundary in administrative:
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
            if a_label != 'location':
                place_names += f"{a_label.capitalize()}: {', '.join(a_list)}\n"
        section_description = section_description + place_names

        return [{'dataframe': result, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def feature_inventory(self) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
        """
        Returns the name and number of geographic boundaries in a report.

        This method calculates the number of unique geographic boundaries (e.g., river basins, lakes, parks) in the survey data
        and returns a DataFrame with the counts and a dictionary with the names of the unique features.

        Returns
        -------
        tuple
            A tuple containing:
            - A DataFrame with the count of unique geographic boundaries.
            - A dictionary with the names of the unique geographic boundaries.

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

        # d = survey_report.feature_inventory()[0]
        # d_names = survey_report.feature_inventory()[1]
        section_label = "**The named features in this report**"
        section_description = "The lakes, rivers or parks included in this report\n\n"

        place_names = ""
        for a_label, a_list in feature_names.items():
            if a_label != 'location':
                place_names += f"{a_label.capitalize()}: {', '.join(a_list)}\n"
        section_description = section_description + place_names.title()
        return [{'dataframe': result,
                 'prompt': {'section_label': section_label, 'section_description': section_description}}]

        # return result, feature_names

    @property
    def date_range(self):
        """The date range of the selected results"""
        start = self.df['date'].min()
        end = self.df['date'].max()
        return {'start': start, 'end': end}

    def inventory(self):
        """Returns the total quantity, median pcs/m, % of total and fail rate for each object code in the report"""
        tq = self.total_quantity
        # print(self.df.columns)
        object_totals = self.df.groupby([object_of_interest, 'en'], as_index=False).agg(agg_groups)
        object_totals['% of total'] = object_totals[Q] / tq
        object_totals.rename(columns={'en': 'object'}, inplace=True)

        return object_totals

    @property
    def total_quantity(self):
        """Returns the total quantity of the report"""
        return self.df[Q].sum()

    @property
    def number_of_samples(self):
        """Returns the number of unique sample_ids in the report"""
        return self.df['sample_id'].nunique()

    @property
    def number_of_locations(self):
        """Returns the number of unique locations in the report"""
        return self.df.location.nunique()

    def material_report(self, code_material) -> pd.DataFrame:
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

        inv.set_index('code', drop=True, inplace=True)

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
                       info_columns: list[str] = None, afunc: dict = unit_agg) -> pd.DataFrame:
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
            labels = "location"

        if sample_id is None:
            sample_id = "sample_id"

        if df.empty:
            raise ValueError("The input DataFrame is empty. Please provide a valid DataFrame.")

        if not info_columns:
            return df.groupby([sample_id, labels, 'date'], as_index=False).agg(afunc)
        else:
            return df.groupby([sample_id, labels, 'date', *info_columns], as_index=False).agg(afunc)

    @property
    def sampling_results_summary(self) -> pd.DataFrame:
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

    def object_summary(self) -> pd.DataFrame:
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

def survey_totals_for_all_info_cols(report_meta: dict, survey_report: SurveyReport) -> dict:
    if 'boundary' in report_meta:
        these_cols = [x for x in report_meta['info_columns'] if x != report_meta['boundary']]
    else:
        these_cols = report_meta.info_columns

    results = []
    for col in these_cols:
        results.append(survey_totals_boundary(survey_report, [col]))

    return results

def categorize_features(df: pd.DataFrame, feature_columns: list[str] = None) -> pd.DataFrame:
    """
    Categorize the feature columns in the DataFrame.

    This function scales the 'streets' column and categorizes the specified feature columns into bins.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the feature data.
    feature_columns : list of str, optional
        The list of feature columns to categorize. Default is `feature_variables`.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the categorized feature columns.

    Raises
    ------
    ValueError
        If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
    """
    if df.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    bins = [-1, 0.2, 0.4, 0.6, 0.8, 1]
    bin_labels = [1, 2, 3, 4, 5]

    scaler = MinMaxScaler()

    if 'streets' not in df.columns:
        raise ValueError("'streets' column not found in the DataFrame.")

    df['streets'] = scaler.fit_transform(df[['streets']])

    for column in feature_columns:
        if column not in df.columns:
            raise ValueError(f"Feature column '{column}' not found in the DataFrame.")
        df[column] = pd.cut(df[column], bins=bins, labels=bin_labels)

    return df

class LandUseReport:
    """
    A class to generate a report from survey data with respect to land use features.

    The `LandUseReport` class is a container for the data and methods used to generate a report from a survey data set.
    The report summarizes the data in the survey with respect to the land use features of the survey locations.

    Attributes
    ----------
    target : pd.DataFrame
        The DataFrame containing the target data.
    features : pd.DataFrame
        The DataFrame containing the feature data.
    feature_variables : list of str
        A list of feature variables extracted from the features DataFrame.
    intersects : pd.DataFrame or None
        A DataFrame containing the intersects data, if available.
    df_cont : pd.DataFrame
        A DataFrame containing the continuous data after merging the target and features DataFrames.
    df_cat : pd.DataFrame
        A DataFrame containing the categorized feature columns.

    Methods
    -------
    merge_land_use_to_survey_data()
        Merge the land use data with the survey data.
    categorize_columns(df: pd.DataFrame, feature_columns: list[str] = feature_variables) -> pd.DataFrame
        Categorize the feature columns in the DataFrame.
    n_samples_per_feature(df: pd.DataFrame = None, features: list[str] = None) -> pd.DataFrame
        Calculate the number of samples per feature.
    n_pieces_per_feature() -> pd.DataFrame
        Calculate the number of pieces per feature.
    locations_per_feature() -> pd.DataFrame
        Calculate the number of unique locations per feature.
    rate_per_feature(df: pd.DataFrame = None) -> pd.DataFrame
        Calculate the average rate per feature.
    correlation_matrix() -> pd.DataFrame
        Calculate the correlation matrix for the feature variables.
    """

    def __init__(self, df_target, features):
        self.df_cont = df_target
        self.feature_variables = features
        self.df_cat = self.categorize_columns(self.df_cont.copy())

    def categorize_columns(self, df: pd.DataFrame, feature_variables: list[str] = None) -> pd.DataFrame:
        """
        Categorize the feature columns in the DataFrame.

        This method scales the 'streets' column and categorizes the specified feature columns into bins.

        Parameters
        ----------
        df : pd.DataFrame
            The DataFrame containing the feature data.
        feature_columns : list of str, optional
            The list of feature columns to categorize. Default is `feature_variables`.

        Returns
        -------
        pd.DataFrame
            A DataFrame with the categorized feature columns.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        return categorize_features(df, feature_columns=self.feature_variables)

    def n_samples_per_feature(self, df: pd.DataFrame = None, features: list[str] = None) -> pd.DataFrame:
        """
        Calculate the number of samples per feature.

        This method calculates the number of samples for each specified feature in the DataFrame.

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the feature data. If not provided, the method uses `self.df_cat`.
        features : list of str, optional
            The list of features to calculate the number of samples for. If not provided, the method uses `session_config.feature_variables`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of samples per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()

        if features is None:
            features = self.feature_variables

        if df.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: df[feature].value_counts() for feature in features}

        df_concat = pd.concat(df_feature, axis=1)

        df_concat = df_concat.fillna(0).astype('int')

        d  = df_concat.sort_index()
        new_columns = pd.MultiIndex.from_product([["Proportion of samples collected"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        d.replace(0, 'none', inplace=True)
        d = d.map(lambda x: f"{x * 100:.1f}%" if isinstance(x, (int, float)) else x)
        section_label = "Land use sampling stratification: proportion of buffer and proportion of samples"
        section_description = land_use_description + '\n' + d.to_markdown()

        return [{'dataframe': d, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def n_pieces_per_feature(self) -> pd.DataFrame:
        """
        Calculate the number of pieces per feature.

        This method calculates the sum of pieces for each specified feature in the DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of pieces per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cat.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[Q].sum() for feature in
                      self.feature_variables}
        df_concat = pd.concat(df_feature, axis=1)


        return df_concat.fillna(0).astype('int')

    def locations_per_feature(self) -> pd.DataFrame:
        """
        Calculate the number of unique locations per feature.

        This method calculates the number of unique locations for each specified feature in the DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the number of unique locations per feature.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cat.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        df_feature = {feature: self.df_cat.groupby(feature, observed=True)[location_label].nunique() for feature in
                      self.feature_variables}
        df_concat = pd.concat(df_feature, axis=1)

        return df_concat.fillna(0).astype('int')

    def rate_per_feature(self, df: pd.DataFrame = None) -> pd.DataFrame:
        """
        Calculate the average rate per feature.

        This method calculates the mean rate of the target variable for each category in the specified features.

        Parameters
        ----------
        df : pd.DataFrame, optional
            The DataFrame containing the feature data. If not provided, the method uses `self.df_cat`.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the average rates per feature category.

        Raises
        ------
        ValueError
            If the input DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if df is None:
            df = self.df_cat.copy()
        else:
            df = df.copy()

        if df.empty:
            raise ValueError("Input DataFrame cannot be empty.")

        avg_matrix = pd.DataFrame(index=feature_variables, columns=bin_labels)

        for column in self.feature_variables:
            for category in bin_labels:
                filtered = df[df[column] == category]
                avg_matrix.at[column, category] = filtered[Y].mean() if not filtered.empty else 0


        d = avg_matrix.round(2).T
        # d = d.round(2)
        new_columns = pd.MultiIndex.from_product([["Pieces of trash per meter"], d.columns])
        d.columns = new_columns
        d['proportion of buffer'] = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
        d.set_index('proportion of buffer', inplace=True, drop=True)
        # d = d.round(2)
        d.replace(0, 'none', inplace=True)
        section_label = "Lamd use sampling stratification: proportion of buffer and pcs/m"
        section_description = land_use_rates_description + '\n' + d.to_markdown()

        return [
            {'dataframe': d, 'prompt': {'section_label': section_label, 'section_description': section_description}}]

    def correlation_matrix(self) -> pd.DataFrame:
        """
        Calculate the correlation matrix for the feature variables.

        This method calculates the correlation matrix for the feature variables in the continuous DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the correlation matrix of the feature variables.

        Raises
        ------
        ValueError
            If the continuous DataFrame is empty or if the feature columns are not found in the DataFrame.
        """
        if self.df_cont.empty:
            raise ValueError("Continuous DataFrame cannot be empty.")

        missing_columns = [col for col in self.feature_variables if col not in self.df_cont.columns]
        if missing_columns:
            raise ValueError(f"Feature columns {missing_columns} not found in the DataFrame.")

        return self.df_cont[[*feature_variables, 'pcs/m']].corr()


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
