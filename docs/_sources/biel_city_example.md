# Biel/Bienne - example city

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Biel/Bienne - example city 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting grid forecasting example</i>


## Executive Summary

The report covers the city of Biel/Bienne, analyzing data from January 1, 2020, to March 31, 2021. The survey includes one river (Schüss) and one lake (Bielersee). A total of 17 samples were collected, with an average of 1.62 pcs/m, a median of 1.71 pcs/m, a maximum of 3.88 pcs/m, and a standard deviation of 1.26. The survey identified 1,034 objects in total. The five most common objects found were cigarette filters (75.53% of total, fail rate 100%), and food wrappers (24.47% of total, fail rate 94.12%). All identified objects were composed of plastic.

Sampling stratification, which divides a population into distinct subgroups based on specific characteristics, was used to ensure accurate representation. The area was classified as mixed land use. The sampling stratification table revealed that areas where buildings occupied 40-60% of the buffer zone had the highest trash density, with an average of 2.00 pcs/m (76.5% of samples). Undefined land-use areas occupying 0-20% of the buffer zone had an average pcs/m of 1.62, indicating significant litter density in these areas as well.

Regression analysis was conducted using multiple models, with Bagging: Linear Regression showing the highest R² at -0.00 and an MSE of 0.89, indicating limited reliability in predictions. Feature importance analysis revealed that 'streets' (0.274337) and 'buildings' (0.218129) were the most significant predictors according to model feature importance, while 'buildings' (0.137264) and 'streets' (0.0350437) were most significant in permutation feature importance.

Grid approximation was employed to estimate the conditional probability of survey results exceeding specific values. The in-boundary prior had an average pcs/m of 1.13 and a median of 0.94, while the out-boundary prior had an average pcs/m of 1.02 and a median of 0.68. The observed average pcs/m was 1.62. Comparison with posterior results suggested a decrease in observed metrics, with posterior averages of 1.02 pcs/m (in-boundary) and 1.13 pcs/m (out-boundary). This indicates that future observations might show lower litter density compared to the current survey results.
## Sample results

The report covers the city of Biel/Bienne, which is the only city included in this analysis. The survey identifies one river, the Schüss, and one lake, the Bielersee; thus, there is a total of two water bodies documented. The sampling period spans from January 1, 2020, to March 31, 2021, within the survey area known as Aare. A total of 17 samples were collected, yielding an average of 1.62 pcs/m, a median of 1.71 pcs/m, a maximum of 3.88 pcs/m, and a standard deviation of 1.26. The total number of objects identified across these surveys is 1,034.

The most common objects found include: 
1. Cigarette filters, with a fail rate of 100% (indicating they were found in all samples), comprising 75.53% of the total, with a density of 1.23 pcs/m and a total quantity of 781.
2. Food wrappers (candy, snacks) with a fail rate of 94.12%, making up 24.47% of the total, with a density of 0.39 pcs/m and a total quantity of 253.

The material composition of the identified objects is entirely plastic, representing 100% of the total count.


:::{dropdown} Sample results frequently asked questions
### Frequently asked questions

**What were the ten most common items found?**  
The report provides detailed information on two specific objects, which are:
1. Cigarette filters, with a fail rate of 100% (indicating they were found in all samples) and constituting 75.53% of the total.
2. Food wrappers (candy, snacks), with a fail rate of 94.12% and making up 24.47% of the total.

**Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**  
Yes, these objects are commonly found on European beaches. According to the OSPAR results from 2021, it was reported that cigarette butts and food wrappers are prevalent debris types. The data indicates that cigarette butts can reach up to 50 items per 100 meters of beach. For more detailed results, you can visit the OSPAR website: [OSPAR Beach Litter Results 2021](https://www.ospar.org/documents?v=7691).

**What are possible sources of these specific objects?**  
Possible sources of cigarette filters include littering by smokers in public spaces and near beaches. Food wrappers can be attributed to the consumption of packaged snacks and meals by beachgoers and picnickers, which often results in litter when proper disposal methods are not followed.

**Which three cities had the highest average pcs/m? Which three had the lowest?**  
The report provides data only for the city of Biel/Bienne, which has an average of 1.62 pcs/m. Therefore, there is no comparative data available for other cities in this report to determine the highest or lowest averages.
:::

::::{grid} 1
:margin 0
:padding: 0

:::{grid-item-card}
:padding: 0
:img-background: bielcity/situation_map.jpg

:::

::::


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_0d534_row0_col0, #T_0d534_row0_col1, #T_0d534_row0_col2, #T_0d534_row0_col4, #T_0d534_row0_col5, #T_0d534_row0_col6, #T_0d534_row0_col7, #T_0d534_row0_col8 {
  background-color: rgba(31, 119, 180, 0.6);
  color: white;
}
#T_0d534_row1_col0, #T_0d534_row1_col1, #T_0d534_row1_col2, #T_0d534_row1_col4, #T_0d534_row1_col5, #T_0d534_row1_col6, #T_0d534_row1_col7, #T_0d534_row1_col8 {
  background-color: rgba(174, 199, 232, 0.6);
  color: black;
}
#T_0d534_row2_col0, #T_0d534_row2_col1, #T_0d534_row2_col2, #T_0d534_row2_col4, #T_0d534_row2_col5, #T_0d534_row2_col6, #T_0d534_row2_col7, #T_0d534_row2_col8 {
  background-color: rgba(255, 127, 14, 0.6);
  color: black;
}
</style>
<table id="T_0d534">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_0d534_level0_col0" class="col_heading level0 col0" >location</th>
      <th id="T_0d534_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_0d534_level0_col2" class="col_heading level0 col2" >pcs/m</th>
      <th id="T_0d534_level0_col4" class="col_heading level0 col4" >buildings</th>
      <th id="T_0d534_level0_col5" class="col_heading level0 col5" >forest</th>
      <th id="T_0d534_level0_col6" class="col_heading level0 col6" >undefined</th>
      <th id="T_0d534_level0_col7" class="col_heading level0 col7" >recreation</th>
      <th id="T_0d534_level0_col8" class="col_heading level0 col8" >public-services</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0d534_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_0d534_row0_col0" class="data row0 col0" >mullermatte</td>
      <td id="T_0d534_row0_col1" class="data row0 col1" >967</td>
      <td id="T_0d534_row0_col2" class="data row0 col2" >2,00</td>
      <td id="T_0d534_row0_col4" class="data row0 col4" >0,49</td>
      <td id="T_0d534_row0_col5" class="data row0 col5" >0,38</td>
      <td id="T_0d534_row0_col6" class="data row0 col6" >0,11</td>
      <td id="T_0d534_row0_col7" class="data row0 col7" >0,03</td>
      <td id="T_0d534_row0_col8" class="data row0 col8" >0,04</td>
    </tr>
    <tr>
      <th id="T_0d534_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_0d534_row1_col0" class="data row1 col0" >schusspark-strand</td>
      <td id="T_0d534_row1_col1" class="data row1 col1" >33</td>
      <td id="T_0d534_row1_col2" class="data row1 col2" >0,36</td>
      <td id="T_0d534_row1_col4" class="data row1 col4" >0,78</td>
      <td id="T_0d534_row1_col5" class="data row1 col5" >0,18</td>
      <td id="T_0d534_row1_col6" class="data row1 col6" >0,04</td>
      <td id="T_0d534_row1_col7" class="data row1 col7" >0,04</td>
      <td id="T_0d534_row1_col8" class="data row1 col8" >0,06</td>
    </tr>
    <tr>
      <th id="T_0d534_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_0d534_row2_col0" class="data row2 col0" >strandboden-biel</td>
      <td id="T_0d534_row2_col1" class="data row2 col1" >34</td>
      <td id="T_0d534_row2_col2" class="data row2 col2" >0,42</td>
      <td id="T_0d534_row2_col4" class="data row2 col4" >0,60</td>
      <td id="T_0d534_row2_col5" class="data row2 col5" >0,28</td>
      <td id="T_0d534_row2_col6" class="data row2 col6" >0,07</td>
      <td id="T_0d534_row2_col7" class="data row2 col7" >0,03</td>
      <td id="T_0d534_row2_col8" class="data row2 col8" >0,04</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::
## Sampling stratification

Sampling stratification refers to the process of dividing a population into distinct subgroups or strata, based on specific characteristics, to ensure that the sample accurately represents the population. In the context of this survey, land-use features within a buffer zone of 1,500 meters surrounding each survey location were analyzed to identify how different land uses contribute to litter density. The findings from the sampling stratification and trash density tables provide insight into the relationship between land-use types and the density of litter observed in various locations.

The highest pieces of trash per meter (pcs/m) values in the sampling stratification and trash density table for the categories of buildings, forest, undefined, and streets are as follows: 
1. For buildings occupying 40-60% of the buffer zone, the average pcs/m is 2.00. This indicates that in locations where buildings occupy this proportion of the buffer, there is a significant amount of litter.
2. For undefined land-use occupying 0-20% of the buffer zone, the average pcs/m is 1.62. This is noteworthy as it reflects litter density in areas with an undefined categorization of land use.



::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_b41df tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_b41df tr:nth-child(odd) {
  background: #FFF;
}
#T_b41df tr {
  font-size: 12px;
}
#T_b41df th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_b41df td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_b41df table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b41df  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b41df  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b41df  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b41df caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_b41df">
  <caption>
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.
</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_b41df_level0_col0" class="col_heading level0 col0" colspan="9">Proportion of samples collected</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_b41df_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_b41df_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_b41df_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_b41df_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_b41df_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_b41df_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_b41df_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_b41df_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_b41df_level1_col8" class="col_heading level1 col8" >orchards</th>
    </tr>
    <tr>
      <th class="index_name level0" >proportion of buffer</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_b41df_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_b41df_row0_col0" class="data row0 col0" >none</td>
      <td id="T_b41df_row0_col1" class="data row0 col1" >100.0%</td>
      <td id="T_b41df_row0_col2" class="data row0 col2" >11.8%</td>
      <td id="T_b41df_row0_col3" class="data row0 col3" >100.0%</td>
      <td id="T_b41df_row0_col4" class="data row0 col4" >100.0%</td>
      <td id="T_b41df_row0_col5" class="data row0 col5" >100.0%</td>
      <td id="T_b41df_row0_col6" class="data row0 col6" >76.5%</td>
      <td id="T_b41df_row0_col7" class="data row0 col7" >100.0%</td>
      <td id="T_b41df_row0_col8" class="data row0 col8" >100.0%</td>
    </tr>
    <tr>
      <th id="T_b41df_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_b41df_row1_col0" class="data row1 col0" >none</td>
      <td id="T_b41df_row1_col1" class="data row1 col1" >none</td>
      <td id="T_b41df_row1_col2" class="data row1 col2" >88.2%</td>
      <td id="T_b41df_row1_col3" class="data row1 col3" >none</td>
      <td id="T_b41df_row1_col4" class="data row1 col4" >none</td>
      <td id="T_b41df_row1_col5" class="data row1 col5" >none</td>
      <td id="T_b41df_row1_col6" class="data row1 col6" >11.8%</td>
      <td id="T_b41df_row1_col7" class="data row1 col7" >none</td>
      <td id="T_b41df_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_b41df_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_b41df_row2_col0" class="data row2 col0" >76.5%</td>
      <td id="T_b41df_row2_col1" class="data row2 col1" >none</td>
      <td id="T_b41df_row2_col2" class="data row2 col2" >none</td>
      <td id="T_b41df_row2_col3" class="data row2 col3" >none</td>
      <td id="T_b41df_row2_col4" class="data row2 col4" >none</td>
      <td id="T_b41df_row2_col5" class="data row2 col5" >none</td>
      <td id="T_b41df_row2_col6" class="data row2 col6" >none</td>
      <td id="T_b41df_row2_col7" class="data row2 col7" >none</td>
      <td id="T_b41df_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_b41df_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_b41df_row3_col0" class="data row3 col0" >23.5%</td>
      <td id="T_b41df_row3_col1" class="data row3 col1" >none</td>
      <td id="T_b41df_row3_col2" class="data row3 col2" >none</td>
      <td id="T_b41df_row3_col3" class="data row3 col3" >none</td>
      <td id="T_b41df_row3_col4" class="data row3 col4" >none</td>
      <td id="T_b41df_row3_col5" class="data row3 col5" >none</td>
      <td id="T_b41df_row3_col6" class="data row3 col6" >none</td>
      <td id="T_b41df_row3_col7" class="data row3 col7" >none</td>
      <td id="T_b41df_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_b41df_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_b41df_row4_col0" class="data row4 col0" >none</td>
      <td id="T_b41df_row4_col1" class="data row4 col1" >none</td>
      <td id="T_b41df_row4_col2" class="data row4 col2" >none</td>
      <td id="T_b41df_row4_col3" class="data row4 col3" >none</td>
      <td id="T_b41df_row4_col4" class="data row4 col4" >none</td>
      <td id="T_b41df_row4_col5" class="data row4 col5" >none</td>
      <td id="T_b41df_row4_col6" class="data row4 col6" >11.8%</td>
      <td id="T_b41df_row4_col7" class="data row4 col7" >none</td>
      <td id="T_b41df_row4_col8" class="data row4 col8" >none</td>
    </tr>
  </tbody>
</table>


</div>



:::

::::

::::{grid}

:::{grid-item}


<div>
<style type="text/css">
#T_e58a9 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_e58a9 tr:nth-child(odd) {
  background: #FFF;
}
#T_e58a9 tr {
  font-size: 12px;
}
#T_e58a9 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_e58a9 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_e58a9 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_e58a9  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_e58a9  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_e58a9  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_e58a9 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_e58a9">
  <caption>
The land use profile allows us to group locations according to the topography. Here we consdider how the observed litter density changes based on the land use feature and the proportion of the buffer-zone that the feature occupies</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_e58a9_level0_col0" class="col_heading level0 col0" colspan="9">Pieces of trash per meter</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_e58a9_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_e58a9_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_e58a9_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_e58a9_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_e58a9_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_e58a9_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_e58a9_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_e58a9_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_e58a9_level1_col8" class="col_heading level1 col8" >orchards</th>
    </tr>
    <tr>
      <th class="index_name level0" >proportion of buffer</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e58a9_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_e58a9_row0_col0" class="data row0 col0" >none</td>
      <td id="T_e58a9_row0_col1" class="data row0 col1" >1,62</td>
      <td id="T_e58a9_row0_col2" class="data row0 col2" >0,35</td>
      <td id="T_e58a9_row0_col3" class="data row0 col3" >1,62</td>
      <td id="T_e58a9_row0_col4" class="data row0 col4" >1,62</td>
      <td id="T_e58a9_row0_col5" class="data row0 col5" >1,62</td>
      <td id="T_e58a9_row0_col6" class="data row0 col6" >2,00</td>
      <td id="T_e58a9_row0_col7" class="data row0 col7" >1,62</td>
      <td id="T_e58a9_row0_col8" class="data row0 col8" >1,62</td>
    </tr>
    <tr>
      <th id="T_e58a9_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_e58a9_row1_col0" class="data row1 col0" >none</td>
      <td id="T_e58a9_row1_col1" class="data row1 col1" >none</td>
      <td id="T_e58a9_row1_col2" class="data row1 col2" >1,79</td>
      <td id="T_e58a9_row1_col3" class="data row1 col3" >none</td>
      <td id="T_e58a9_row1_col4" class="data row1 col4" >none</td>
      <td id="T_e58a9_row1_col5" class="data row1 col5" >none</td>
      <td id="T_e58a9_row1_col6" class="data row1 col6" >0,42</td>
      <td id="T_e58a9_row1_col7" class="data row1 col7" >none</td>
      <td id="T_e58a9_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_e58a9_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_e58a9_row2_col0" class="data row2 col0" >2,00</td>
      <td id="T_e58a9_row2_col1" class="data row2 col1" >none</td>
      <td id="T_e58a9_row2_col2" class="data row2 col2" >none</td>
      <td id="T_e58a9_row2_col3" class="data row2 col3" >none</td>
      <td id="T_e58a9_row2_col4" class="data row2 col4" >none</td>
      <td id="T_e58a9_row2_col5" class="data row2 col5" >none</td>
      <td id="T_e58a9_row2_col6" class="data row2 col6" >none</td>
      <td id="T_e58a9_row2_col7" class="data row2 col7" >none</td>
      <td id="T_e58a9_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_e58a9_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_e58a9_row3_col0" class="data row3 col0" >0,39</td>
      <td id="T_e58a9_row3_col1" class="data row3 col1" >none</td>
      <td id="T_e58a9_row3_col2" class="data row3 col2" >none</td>
      <td id="T_e58a9_row3_col3" class="data row3 col3" >none</td>
      <td id="T_e58a9_row3_col4" class="data row3 col4" >none</td>
      <td id="T_e58a9_row3_col5" class="data row3 col5" >none</td>
      <td id="T_e58a9_row3_col6" class="data row3 col6" >none</td>
      <td id="T_e58a9_row3_col7" class="data row3 col7" >none</td>
      <td id="T_e58a9_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_e58a9_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_e58a9_row4_col0" class="data row4 col0" >none</td>
      <td id="T_e58a9_row4_col1" class="data row4 col1" >none</td>
      <td id="T_e58a9_row4_col2" class="data row4 col2" >none</td>
      <td id="T_e58a9_row4_col3" class="data row4 col3" >none</td>
      <td id="T_e58a9_row4_col4" class="data row4 col4" >none</td>
      <td id="T_e58a9_row4_col5" class="data row4 col5" >none</td>
      <td id="T_e58a9_row4_col6" class="data row4 col6" >0,35</td>
      <td id="T_e58a9_row4_col7" class="data row4 col7" >none</td>
      <td id="T_e58a9_row4_col8" class="data row4 col8" >none</td>
    </tr>
  </tbody>
</table>
</div>



:::

::::
:::{dropdown} Sampling stratification frequently asked questions
### Frequently asked questions

**1. What does the sampling stratification table tell us?**  
The sampling stratification table provides a breakdown of the proportion of samples collected in relation to specific land-use features, allowing for the analysis of litter density across different areas. For example, in the buildings category, where the buffer zone is 40-60%, 76.5% of the samples were collected, resulting in an average pcs/m of 2.00. This indicates a high density of litter in that land-use scenario. In the undefined category with a buffer zone of 0-20%, 100% of the samples were collected, leading to an average pcs/m of 1.62. These values suggest that certain land-use conditions may be more prone to litter accumulation, highlighting areas that could require more attention for litter management.

**2. How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The sampling stratification and trash density table can highlight areas with particularly high litter densities, indicating potential environmental concerns. By evaluating the average pcs/m across different land uses, surveyors can identify which areas are most affected by litter. For instance, the high pcs/m associated with buildings occupying 40-60% of the buffer zone signals that urbanized areas may need targeted clean-up efforts or better waste management strategies. Additionally, the undefined land use exhibiting high litter density suggests that further investigation is warranted to clarify the land use and address potential litter sources.

**3. Under what land-use conditions would a surveyor expect to find the most trash?**  
Surveyors would expect to find the most trash in areas where buildings occupy 40-60% of the buffer zone, with an average pcs/m of 2.00. This suggests that urban environments, particularly those with significant building presence, are likely to have higher litter densities. Additionally, the undefined land-use category at 0-20% shows an average pcs/m of 1.62, indicating that even in areas with less defined land use, litter may still accumulate significantly.

**4. Given the results in the sampling stratification table, were these surveys collected in mostly urban environment or forested?**  
The surveys do not predominantly classify as either urban or rural. The sum of the proportions of samples for buildings in the rows 60-80% and 80-100% is 0.24 (23.5% + 0%), which does not exceed 50%, thus failing the urban classification. Similarly, the sum of the proportions of samples for forests in the same rows is 0 (both 60-80% and 80-100% have no samples), which does not exceed 50%, thus failing the rural classification. Therefore, the area is classified as mixed. The greatest proportion of samples for buildings is in the 40-60% category, which has 76.5% of samples collected. For forests, there are no samples collected in the higher categories, and the undefined land-use shows high values in the lower categories.
:::

## Linear and ensemble regression

Cluster analysis, particularly K-means, is a method used to categorize data into distinct groups (or clusters) based on their features. In the context of the provided document, it was noted that there was insufficient data for a cluster analysis, and thus no clustering results could be presented, including the cluster with the highest pcs/m or its composition regarding buildings, forest, and undefined land use.

Linear regression is a statistical method used to model and analyze the relationship between a dependent variable and one or more independent variables. The basic assumptions of linear regression include linearity (the relationship between the variables is linear), independence (the residuals are independent), homoscedasticity (constant variance of residuals), and normality (the residuals are normally distributed). Ensemble regression, on the other hand, combines predictions from multiple regression models to improve the accuracy and robustness of predictions. Basic assumptions for ensemble methods can include those of the individual models used (e.g., linear regression) and the assumption that combining models will yield better performance than any single model alone.

In the regression analysis conducted, the model with the highest R² was the Bagging: Linear Regression model, which had an R² of -0.00 and a mean squared error (MSE) of 0.89. Given that the best model has a negative R², it indicates that the model performs worse than a simple mean model, which raises concerns about the reliability of predictions. The MSE value suggests that the model has a degree of error, further indicating limited reliability in its predictive capacity.



:::{dropdown} Linear methods frequently asked questions
### Frequently asked questions

**What were the r² and MSE of each test?**  
The regression analysis results are as follows:

|    | Model                        |          R² |      MSE |
|---:|:-----------------------------|------------:|---------:|
|  0 | Linear Regression            | -0.10       | 0.98     |
|  1 | Random Forest Regression     | -0.19       | 1.05     |
|  2 | Gradient Boosting Regression | -0.59       | 1.41     |
|  3 | Theil-Sen Regressor          | -0.11       | 0.99     |
|  4 | Bagging:Linear Regression    | -0.00       | 0.89     |
|  5 | Voting                       | -0.28       | 1.14     |

The analysis indicates that all models produced negative R² values, suggesting they do not fit the data well.

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**  
The negative R² values across all regression methods indicate that none of the models fit the data well, resulting in unreliable predictions. The MSE values, while providing some measure of error, confirm that the predictions made by these models are likely to be inaccurate and should be interpreted with caution.

**Can any conclusions be drawn from these results?**  
Conclusions that can be drawn from these results are limited due to the negative R² values. These results suggest that the models are not appropriate for the data, and therefore, any predictions or insights derived from them may not be valid or useful.

**According to the cluster analysis what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**  
According to the report, there was insufficient data for a cluster analysis, and thus no information could be provided regarding the cluster with the greatest average pcs/m or the distribution of land use values within any clusters.
:::

## Forecasts and methods

A grid approximation is a statistical technique used to estimate the conditional probability of a survey result exceeding or equaling a specific value. It is constructed using an inference table, which organizes prior data, likelihood observations, and resultant posterior distributions. An inference table systematically presents these components, where "prior" refers to the information gathered from previous observations (in this case, observations from either inside or outside a designated boundary), and "posterior" denotes the updated probabilities derived from combining the prior data with new observations through Bayesian inference.

In the context of the report, the prior distributions are as follows:

1. **In-boundary prior**: Average pcs/m = 1.13, Median pcs/m = 0.94
2. **Out-boundary prior**: Average pcs/m = 1.02, Median pcs/m = 0.68

The average pcs/m results from the posterior distributions are compared to the observed results. The observed average pcs/m is reported as 1.62. The differences are:

- **In-boundary posterior**: Average pcs/m = 1.02; Difference = 1.62 - 1.02 = 0.60
- **Out-boundary posterior**: Average pcs/m = 1.13; Difference = 1.62 - 1.13 = 0.49

Given these results, one could expect a decrease in observed metrics compared to the posterior predictions. If a person takes one sample, they may have a 50% chance of noticing an increase or decrease from the observed results, given the variability indicated by the standard deviation of 0.96 for the out-boundary and 0.94 for the in-boundary samples. However, if they take two samples, their likelihood of perceiving a change would increase, as the sample mean would likely provide a more stable estimate due to the averaging effect.


::::{grid} 1
:margin: 0

:::{grid-item}
:padding: 0

![image info](bielcity/boxplots_observed_expected.jpeg)

:::

::::


:::{dropdown} Grid approximation frequently asked questions
### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**

Grid approximation is reasonable due to the distribution characteristics of the observed data. The average pcs/m is 1.62, while the median is 1.71. The difference between these two values suggests that the data may not be perfectly normally distributed, as the mean is lower than the median. If the data were normally distributed, one would expect the mean and median to be closer together. The implications of this difference indicate that while the grid approximation provides a useful estimation method, caution should be taken in making predictions, as the underlying distribution may skew the results.

**2. Do you have an example of other fields or domains that use grid approximation or Bayesian methods?**

Yes, grid approximation and Bayesian methods are employed in various fields, including ecology for species distribution modeling, finance for risk assessment and decision-making under uncertainty, and machine learning for probabilistic modeling and inference.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**

If the data is normally distributed, predictions from the grid approximation may align more closely with those from a normal distribution model, particularly regarding the central tendency (mean and median). However, grid approximation might still provide a more nuanced view of variability and uncertainty by considering prior observations, whereas normal distribution predictions would depend solely on the parameters of the normal curve.

**4. What is the difference between grid approximation and linear or ensemble regression?**

Grid approximation focuses on estimating conditional probabilities based on prior and likelihood data, while linear regression models the relationship between independent and dependent variables to predict outcomes. Ensemble regression combines multiple models to improve prediction accuracy, whereas grid approximation does not necessarily involve the combination of models but rather uses a probabilistic framework to update beliefs based on new data.

**5. With which posterior do we expect to find most? The least?**

From the results, we expect to find most observations within the out-boundary prior posterior, which has a higher average pcs/m of 1.13 compared to the in-boundary prior posterior, which has a lower average pcs/m of 1.02.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**

If the in-boundary grid approximation predicts an increase, it suggests that elevated values were likely observed in other locations within the boundary. This is because the prior is comprised only of locations in the same geographic boundary, and the posterior is a weighted average of the prior and likelihood, indicating that the overall trend within the boundary is reflected in the predictions.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**

If the out-boundary grid approximation predicts an increase, it implies that locations outside of the boundary had elevated values compared to the likelihood. This suggests that there are significant observations in those external samples that influence the overall prediction.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**

The expected results from the observed results indicate that both in-boundary and out-boundary averages are lower than the observed average of 1.62. Specifically, the in-boundary average is 1.02 and the out-boundary average is 1.13. This indicates a decrease should be expected in future observations based on the current posterior estimates, particularly considering the standard deviations of 0.94 and 0.96, suggesting variability that could lead to different outcomes in subsequent samples.
:::

## Consolidated results : canton, survey area


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_1cb01 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_1cb01 tr:nth-child(odd) {
  background: #FFF;
}
#T_1cb01 tr {
  font-size: 12px;
}
#T_1cb01 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_1cb01 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_1cb01 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_1cb01  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_1cb01  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_1cb01  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_1cb01 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_1cb01">
  <caption>Sample totals : canton, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_1cb01_level0_col0" class="col_heading level0 col0" >canton</th>
      <th id="T_1cb01_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_1cb01_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_1cb01_row0_col0" class="data row0 col0" >Bern</td>
      <td id="T_1cb01_row0_col1" class="data row0 col1" >1'034</td>
      <td id="T_1cb01_row0_col2" class="data row0 col2" >1,62</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_ff87b tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_ff87b tr:nth-child(odd) {
  background: #FFF;
}
#T_ff87b tr {
  font-size: 12px;
}
#T_ff87b th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_ff87b td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_ff87b table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_ff87b  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_ff87b  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_ff87b  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_ff87b caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_ff87b">
  <caption>Sample totals : parent_boundary, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_ff87b_level0_col0" class="col_heading level0 col0" >parent_boundary</th>
      <th id="T_ff87b_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_ff87b_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_ff87b_row0_col0" class="data row0 col0" >aare</td>
      <td id="T_ff87b_row0_col1" class="data row0 col1" >1'034</td>
      <td id="T_ff87b_row0_col2" class="data row0 col2" >1,62</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::

## Inventory

<div>
<style type="text/css">
#T_30e60 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_30e60 tr:nth-child(odd) {
  background: #FFF;
}
#T_30e60 tr {
  font-size: 12px;
}
#T_30e60 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_30e60 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_30e60 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_30e60  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_30e60  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_30e60  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_30e60 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_30e60">
  <caption> </caption>
  <thead>
    <tr>
      <th id="T_30e60_level0_col0" class="col_heading level0 col0" >quantity</th>
      <th id="T_30e60_level0_col1" class="col_heading level0 col1" >pcs/m</th>
      <th id="T_30e60_level0_col2" class="col_heading level0 col2" >% of total</th>
      <th id="T_30e60_level0_col3" class="col_heading level0 col3" >sample_id</th>
      <th id="T_30e60_level0_col4" class="col_heading level0 col4" >fail rate</th>
      <th id="T_30e60_level0_col5" class="col_heading level0 col5" >object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_30e60_row0_col0" class="data row0 col0" >781</td>
      <td id="T_30e60_row0_col1" class="data row0 col1" >1,23</td>
      <td id="T_30e60_row0_col2" class="data row0 col2" >0,76</td>
      <td id="T_30e60_row0_col3" class="data row0 col3" >17</td>
      <td id="T_30e60_row0_col4" class="data row0 col4" >1,00</td>
      <td id="T_30e60_row0_col5" class="data row0 col5" >Cigarette filters</td>
    </tr>
    <tr>
      <td id="T_30e60_row1_col0" class="data row1 col0" >253</td>
      <td id="T_30e60_row1_col1" class="data row1 col1" >0,39</td>
      <td id="T_30e60_row1_col2" class="data row1 col2" >0,24</td>
      <td id="T_30e60_row1_col3" class="data row1 col3" >17</td>
      <td id="T_30e60_row1_col4" class="data row1 col4" >0,94</td>
      <td id="T_30e60_row1_col5" class="data row1 col5" >Food wrappers; candy, snacks</td>
    </tr>
  </tbody>
</table>


</div>
