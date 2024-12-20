# Bern - example canton

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes and rivers. <i>Report number: Bern - example canton 2020-01-01 2021-05-31</i>




 <i>Proof of concept: llm assissted reporting grid forecasting example</i>


## Executive Summary

The report covers data collected from 21 cities within the canton of Bern from January 26, 2020, to April 23, 2021. The surveyed areas include four rivers (Aare, Aarenidau-Buren-Kanal, Emme, Schuss) and three lakes (Bielersee, Brienzersee, Thunersee). A total of 89 samples were analyzed, yielding an average density of 0.61 pcs/m, a median of 0.27 pcs/m, a maximum of 3.88 pcs/m, and a standard deviation of 0.84. A total of 2,260 objects were identified, with the most common items being cigarette filters (fail rate of 81%, 73.94% of total) and food wrappers (fail rate of 80%, 26.06% of total).

Sampling stratification is a method to ensure sample representation across various land-use features surrounding a survey location. The survey areas were classified as mixed land use environments since neither the urban nor rural criteria were met. The sampling stratification table indicated that the highest pcs/m was observed in areas where buildings occupied 40-60% of the buffer zone, with an average density of 1.33 pcs/m and 25.8% of samples collected in that range. This table helps in understanding how different land-use features influence litter density.

Regression analyses were conducted using various models, with the Bagging: Random Forest Regression model demonstrating the highest R² value of 0.62 and an MSE of 0.48. This suggests a moderate level of reliability in predictions. Feature importance, as determined by model feature importance, highlighted streets (0.274), buildings (0.218), and forest (0.116) as key predictive variables. Permutation feature importance further supported these findings, with buildings (0.137) and streets (0.035) being significant.

Grid approximation was utilized to estimate the likelihood of survey results exceeding given thresholds based on prior and new data. The observed average pcs/m was 0.61, while the posterior averages were 0.96 (in-boundary), 0.98 (out-boundary), and 0.62 (combined). These results indicate a potential increase in trash density within the surveyed boundaries. Comparing the posteriors to observed results suggests a likelihood of encountering higher trash densities in future observations.
## Sample results

The report encompasses a total of 21 cities located within the canton of Bern. Among them, the cities include Kallnach, Biel/Bienne, Vinelz, Brienz (BE), Spiez, Lüscherz, Nidau, Walperswil, Köniz, Bern, Brügg, Gals, Port, Burgdorf, Unterseen, Rubigen, Erlach, Thun, Beatenberg, Ligerz, and Bönigen. The survey also identifies a total of 4 rivers (Aare, Aarenidau-Buren-Kanal, Emme, Schuss) and 3 lakes (Bielersee, Brienzersee, Thunersee) in the named features section.

The data collection took place from January 26, 2020, to April 23, 2021, with the survey area designated as Aare. A total of 89 samples were analyzed, revealing an average of 0.61 pcs/m (objects per meter), a median of 0.27 pcs/m, a maximum of 3.88 pcs/m, and a standard deviation of 0.84. The total number of identified objects amounted to 2,260.

The most common objects found in the survey, characterized by their greatest quantity, include:
1. Cigarette filters: Fail rate of 81%, representing 73.94% of the total (1,671 pcs).
2. Food wrappers; candy, snacks: Fail rate of 80%, comprising 26.06% of the total (589 pcs).

The material composition of the identified objects is exclusively plastic, comprising 100% of the total objects.


:::{dropdown} Sample results frequently asked questions
### Frequently asked questions

**1. What were the ten most common items found?**  
The report primarily identifies two objects with significant quantities and fail rates:
1. Cigarette filters: Fail rate of 81% (indicating that at least one was found in 81% of the samples), comprising 73.94% of the total (1,671 pcs).
2. Food wrappers; candy, snacks: Fail rate of 80% (indicating that at least one was found in 80% of the samples), comprising 26.06% of the total (589 pcs).

**2. Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**  
Yes, many of these objects, particularly cigarette butts and food wrappers, are commonly found on European beaches. According to the OSPAR (Oslo and Paris Conventions for the Protection of the Marine Environment of the North-East Atlantic) results from 2021, cigarette butts were reported at an average density of 37.6 items per 100 meters of beach. For more detailed information, you can visit the OSPAR website: [OSPAR 2021 Report](https://www.ospar.org/documents?v=38759).

**3. What are possible sources of these specific objects?**  
The specific objects identified, such as cigarette filters and food wrappers, primarily originate from human activities. Cigarette filters are often discarded carelessly in public spaces, including beaches and parks, while food wrappers typically come from take-out food, snacks, and picnics. Littering and inadequate waste disposal methods significantly contribute to the presence of these items in natural environments.

**4. Which three cities had the highest average pcs/m? Which three had the lowest?**  
The three cities with the highest average pcs/m are:
1. Biel/Bienne: 1.62 pcs/m
2. Ligerz: 1.55 pcs/m
3. Bönigen: 1.25 pcs/m

The three cities with the lowest average pcs/m are:
1. Walperswil: 0.00 pcs/m
2. Kallnach: 0.09 pcs/m
3. Köniz: 0.09 pcs/m
:::

::::{grid} 1
:margin 0
:padding: 0

:::{grid-item-card}
:padding: 0
:img-background: bern/situation_map.jpg

:::

::::


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_16a78_row0_col0, #T_16a78_row0_col1, #T_16a78_row0_col2, #T_16a78_row0_col3, #T_16a78_row0_col4, #T_16a78_row0_col5, #T_16a78_row0_col6 {
  background-color: rgba(31, 119, 180, 0.6);
  color: white;
}
#T_16a78_row1_col0, #T_16a78_row1_col1, #T_16a78_row1_col2, #T_16a78_row1_col3, #T_16a78_row1_col4, #T_16a78_row1_col5, #T_16a78_row1_col6 {
  background-color: rgba(174, 199, 232, 0.6);
  color: black;
}
#T_16a78_row2_col0, #T_16a78_row2_col1, #T_16a78_row2_col2, #T_16a78_row2_col3, #T_16a78_row2_col4, #T_16a78_row2_col5, #T_16a78_row2_col6 {
  background-color: rgba(255, 127, 14, 0.6);
  color: black;
}
</style>
<table id="T_16a78">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_16a78_level0_col0" class="col_heading level0 col0" >pcs/m</th>
      <th id="T_16a78_level0_col1" class="col_heading level0 col1" >buildings</th>
      <th id="T_16a78_level0_col2" class="col_heading level0 col2" >forest</th>
      <th id="T_16a78_level0_col3" class="col_heading level0 col3" >undefined</th>
      <th id="T_16a78_level0_col4" class="col_heading level0 col4" >streets</th>
      <th id="T_16a78_level0_col5" class="col_heading level0 col5" >public-services</th>
      <th id="T_16a78_level0_col6" class="col_heading level0 col6" >recreation</th>
    </tr>
    <tr>
      <th class="index_name level0" >cluster</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_16a78_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_16a78_row0_col0" class="data row0 col0" >0,39</td>
      <td id="T_16a78_row0_col1" class="data row0 col1" >0,04</td>
      <td id="T_16a78_row0_col2" class="data row0 col2" >0,21</td>
      <td id="T_16a78_row0_col3" class="data row0 col3" >0,75</td>
      <td id="T_16a78_row0_col4" class="data row0 col4" >0,09</td>
      <td id="T_16a78_row0_col5" class="data row0 col5" >0,00</td>
      <td id="T_16a78_row0_col6" class="data row0 col6" >0,00</td>
    </tr>
    <tr>
      <th id="T_16a78_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_16a78_row1_col0" class="data row1 col0" >0,06</td>
      <td id="T_16a78_row1_col1" class="data row1 col1" >0,17</td>
      <td id="T_16a78_row1_col2" class="data row1 col2" >0,56</td>
      <td id="T_16a78_row1_col3" class="data row1 col3" >0,13</td>
      <td id="T_16a78_row1_col4" class="data row1 col4" >0,05</td>
      <td id="T_16a78_row1_col5" class="data row1 col5" >0,04</td>
      <td id="T_16a78_row1_col6" class="data row1 col6" >0,00</td>
    </tr>
    <tr>
      <th id="T_16a78_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_16a78_row2_col0" class="data row2 col0" >1,02</td>
      <td id="T_16a78_row2_col1" class="data row2 col1" >0,46</td>
      <td id="T_16a78_row2_col2" class="data row2 col2" >0,33</td>
      <td id="T_16a78_row2_col3" class="data row2 col3" >0,21</td>
      <td id="T_16a78_row2_col4" class="data row2 col4" >0,61</td>
      <td id="T_16a78_row2_col5" class="data row2 col5" >0,05</td>
      <td id="T_16a78_row2_col6" class="data row2 col6" >0,01</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::
## Sampling stratification

Sampling stratification refers to the systematic method of collecting samples in a way that ensures representation across various land-use features surrounding a survey location. In this context, land-use features include categories such as buildings, forests, wetlands, public services, and recreation areas. Each survey location is surrounded by a buffer zone of radius 1,500 meters, and the proportion of this buffer dedicated to each land-use feature is measured to understand how it influences the results of the survey. Thus, the sampling stratification provides insights into the environmental context of the survey locations, allowing for a more nuanced understanding of litter density based on land use.

In the sampling stratification and trash density table, the highest pieces per meter (pcs/m) values for buildings, forest, and undefined categories were observed under different conditions. For buildings, the highest value was 1.33 pcs/m, which occurred when buildings occupied the 40-60% proportion of the buffer zone, with 25.8% of the samples collected in that range. For forests, the highest value was 0.79 pcs/m, found in the 20-40% proportion of the buffer, where 64.0% of the samples were collected. The undefined category also had a notable average of 0.96 pcs/m in the 0-20% proportion of the buffer, with 34.8% of the samples collected. These values indicate the density of trash found in relation to the space occupied by each land use feature.



::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_9273b tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_9273b tr:nth-child(odd) {
  background: #FFF;
}
#T_9273b tr {
  font-size: 12px;
}
#T_9273b th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_9273b td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_9273b table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9273b  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9273b  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9273b  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9273b caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_9273b">
  <caption>
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.
</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9273b_level0_col0" class="col_heading level0 col0" colspan="9">Proportion of samples collected</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_9273b_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_9273b_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_9273b_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_9273b_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_9273b_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_9273b_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_9273b_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_9273b_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_9273b_level1_col8" class="col_heading level1 col8" >orchards</th>
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
      <th id="T_9273b_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_9273b_row0_col0" class="data row0 col0" >30.3%</td>
      <td id="T_9273b_row0_col1" class="data row0 col1" >100.0%</td>
      <td id="T_9273b_row0_col2" class="data row0 col2" >27.0%</td>
      <td id="T_9273b_row0_col3" class="data row0 col3" >98.9%</td>
      <td id="T_9273b_row0_col4" class="data row0 col4" >100.0%</td>
      <td id="T_9273b_row0_col5" class="data row0 col5" >34.8%</td>
      <td id="T_9273b_row0_col6" class="data row0 col6" >44.9%</td>
      <td id="T_9273b_row0_col7" class="data row0 col7" >100.0%</td>
      <td id="T_9273b_row0_col8" class="data row0 col8" >100.0%</td>
    </tr>
    <tr>
      <th id="T_9273b_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_9273b_row1_col0" class="data row1 col0" >31.5%</td>
      <td id="T_9273b_row1_col1" class="data row1 col1" >none</td>
      <td id="T_9273b_row1_col2" class="data row1 col2" >64.0%</td>
      <td id="T_9273b_row1_col3" class="data row1 col3" >1.1%</td>
      <td id="T_9273b_row1_col4" class="data row1 col4" >none</td>
      <td id="T_9273b_row1_col5" class="data row1 col5" >12.4%</td>
      <td id="T_9273b_row1_col6" class="data row1 col6" >36.0%</td>
      <td id="T_9273b_row1_col7" class="data row1 col7" >none</td>
      <td id="T_9273b_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9273b_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_9273b_row2_col0" class="data row2 col0" >25.8%</td>
      <td id="T_9273b_row2_col1" class="data row2 col1" >none</td>
      <td id="T_9273b_row2_col2" class="data row2 col2" >9.0%</td>
      <td id="T_9273b_row2_col3" class="data row2 col3" >none</td>
      <td id="T_9273b_row2_col4" class="data row2 col4" >none</td>
      <td id="T_9273b_row2_col5" class="data row2 col5" >51.7%</td>
      <td id="T_9273b_row2_col6" class="data row2 col6" >11.2%</td>
      <td id="T_9273b_row2_col7" class="data row2 col7" >none</td>
      <td id="T_9273b_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9273b_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_9273b_row3_col0" class="data row3 col0" >10.1%</td>
      <td id="T_9273b_row3_col1" class="data row3 col1" >none</td>
      <td id="T_9273b_row3_col2" class="data row3 col2" >none</td>
      <td id="T_9273b_row3_col3" class="data row3 col3" >none</td>
      <td id="T_9273b_row3_col4" class="data row3 col4" >none</td>
      <td id="T_9273b_row3_col5" class="data row3 col5" >1.1%</td>
      <td id="T_9273b_row3_col6" class="data row3 col6" >5.6%</td>
      <td id="T_9273b_row3_col7" class="data row3 col7" >none</td>
      <td id="T_9273b_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9273b_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_9273b_row4_col0" class="data row4 col0" >2.2%</td>
      <td id="T_9273b_row4_col1" class="data row4 col1" >none</td>
      <td id="T_9273b_row4_col2" class="data row4 col2" >none</td>
      <td id="T_9273b_row4_col3" class="data row4 col3" >none</td>
      <td id="T_9273b_row4_col4" class="data row4 col4" >none</td>
      <td id="T_9273b_row4_col5" class="data row4 col5" >none</td>
      <td id="T_9273b_row4_col6" class="data row4 col6" >2.2%</td>
      <td id="T_9273b_row4_col7" class="data row4 col7" >none</td>
      <td id="T_9273b_row4_col8" class="data row4 col8" >none</td>
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
#T_102dc tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_102dc tr:nth-child(odd) {
  background: #FFF;
}
#T_102dc tr {
  font-size: 12px;
}
#T_102dc th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_102dc td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_102dc table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_102dc  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_102dc  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_102dc  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_102dc caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_102dc">
  <caption>
The land use profile allows us to group locations according to the topography. Here we consdider how the observed litter density changes based on the land use feature and the proportion of the buffer-zone that the feature occupies</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_102dc_level0_col0" class="col_heading level0 col0" colspan="9">Pieces of trash per meter</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_102dc_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_102dc_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_102dc_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_102dc_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_102dc_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_102dc_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_102dc_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_102dc_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_102dc_level1_col8" class="col_heading level1 col8" >orchards</th>
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
      <th id="T_102dc_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_102dc_row0_col0" class="data row0 col0" >0,52</td>
      <td id="T_102dc_row0_col1" class="data row0 col1" >0,61</td>
      <td id="T_102dc_row0_col2" class="data row0 col2" >0,31</td>
      <td id="T_102dc_row0_col3" class="data row0 col3" >0,62</td>
      <td id="T_102dc_row0_col4" class="data row0 col4" >0,61</td>
      <td id="T_102dc_row0_col5" class="data row0 col5" >0,96</td>
      <td id="T_102dc_row0_col6" class="data row0 col6" >0,38</td>
      <td id="T_102dc_row0_col7" class="data row0 col7" >0,61</td>
      <td id="T_102dc_row0_col8" class="data row0 col8" >0,61</td>
    </tr>
    <tr>
      <th id="T_102dc_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_102dc_row1_col0" class="data row1 col0" >0,22</td>
      <td id="T_102dc_row1_col1" class="data row1 col1" >none</td>
      <td id="T_102dc_row1_col2" class="data row1 col2" >0,79</td>
      <td id="T_102dc_row1_col3" class="data row1 col3" >0,03</td>
      <td id="T_102dc_row1_col4" class="data row1 col4" >none</td>
      <td id="T_102dc_row1_col5" class="data row1 col5" >0,79</td>
      <td id="T_102dc_row1_col6" class="data row1 col6" >1,04</td>
      <td id="T_102dc_row1_col7" class="data row1 col7" >none</td>
      <td id="T_102dc_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_102dc_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_102dc_row2_col0" class="data row2 col0" >1,33</td>
      <td id="T_102dc_row2_col1" class="data row2 col1" >none</td>
      <td id="T_102dc_row2_col2" class="data row2 col2" >0,22</td>
      <td id="T_102dc_row2_col3" class="data row2 col3" >none</td>
      <td id="T_102dc_row2_col4" class="data row2 col4" >none</td>
      <td id="T_102dc_row2_col5" class="data row2 col5" >0,34</td>
      <td id="T_102dc_row2_col6" class="data row2 col6" >0,32</td>
      <td id="T_102dc_row2_col7" class="data row2 col7" >none</td>
      <td id="T_102dc_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_102dc_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_102dc_row3_col0" class="data row3 col0" >0,31</td>
      <td id="T_102dc_row3_col1" class="data row3 col1" >none</td>
      <td id="T_102dc_row3_col2" class="data row3 col2" >none</td>
      <td id="T_102dc_row3_col3" class="data row3 col3" >none</td>
      <td id="T_102dc_row3_col4" class="data row3 col4" >none</td>
      <td id="T_102dc_row3_col5" class="data row3 col5" >none</td>
      <td id="T_102dc_row3_col6" class="data row3 col6" >0,48</td>
      <td id="T_102dc_row3_col7" class="data row3 col7" >none</td>
      <td id="T_102dc_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_102dc_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_102dc_row4_col0" class="data row4 col0" >0,31</td>
      <td id="T_102dc_row4_col1" class="data row4 col1" >none</td>
      <td id="T_102dc_row4_col2" class="data row4 col2" >none</td>
      <td id="T_102dc_row4_col3" class="data row4 col3" >none</td>
      <td id="T_102dc_row4_col4" class="data row4 col4" >none</td>
      <td id="T_102dc_row4_col5" class="data row4 col5" >none</td>
      <td id="T_102dc_row4_col6" class="data row4 col6" >0,07</td>
      <td id="T_102dc_row4_col7" class="data row4 col7" >none</td>
      <td id="T_102dc_row4_col8" class="data row4 col8" >none</td>
    </tr>
  </tbody>
</table>
</div>



:::

::::
:::{dropdown} Sampling stratification frequently asked questions
### Frequently asked questions

**1. What does the sampling stratification table tell us?**

The sampling stratification table provides critical insights into the density of trash as it relates to different land-use features. For instance, in the category of buildings, when the proportion of the buffer zone occupied by buildings is 40-60%, the average trash density is 1.33 pcs/m, and 25.8% of the samples were collected in that range. This indicates a significant concentration of trash in areas where buildings are prevalent. In terms of undefined land use, the average density is 0.96 pcs/m when undefined areas occupy 0-20% of the buffer, with 34.8% of the samples collected. This suggests that even in areas not specifically categorized, there are notable levels of litter, warranting attention.

**2. How can the information in the sampling stratification and trash density table help identify areas of concern?**

The information in the sampling stratification and trash density table is instrumental in identifying areas of concern by highlighting where trash density is highest relative to specific land uses. By knowing which areas exhibit the most litter, policymakers and environmental agencies can prioritize cleanup efforts and implement measures to reduce litter in high-density zones. For example, if certain areas with a high proportion of buildings also show elevated trash densities, it could indicate a need for increased waste management resources in urban settings. Similarly, areas with high undefined density may require further investigation to understand the sources and types of litter present.

**3. Under what land-use conditions would a surveyor expect to find the most trash?**

Surveyors would expect to find the most trash in areas where buildings occupy a larger proportion of the buffer zone. For example, when buildings occupy 40-60% of the buffer zone, the average density is 1.33 pcs/m. This indicates a significant concentration of litter in these urbanized areas. Similarly, in forested areas, when the buffer is occupied by forests at 20-40%, the average density is 0.79 pcs/m. These examples demonstrate that both urban and semi-urban areas are likely to have higher trash densities, prompting further investigation and potential mitigation strategies.

**4. Given the results in the sampling stratification table, were these surveys collected in mostly urban environments or forested?**

The surveys do not predominantly meet the criteria to classify the surveyed locations as either urban or rural. To determine urban classification, the sum of the proportions of samples for buildings in the rows 60-80% and 80-100% must exceed 50%. Here, the respective values are 10.1% and 2.2%, totaling 12.3%, which is below 50%. For rural classification, the sum for forests in the same rows must exceed 50%. However, there are no samples in these ranges for forests. Thus, the area is considered mixed, as neither classification criterion is met. The highest proportion of samples for buildings is 31.5% at 20-40% of the buffer, while the highest for forests is 27.0% at 0-20%, indicating a diverse land-use environment without a clear dominant category.
:::

## Linear and ensemble methods

**Define cluster analysis (kmeans)**: Cluster analysis, specifically K-Means clustering, is a method used to group a set of observations into clusters, where each observation belongs to the cluster with the nearest mean. This approach helps identify patterns in data by categorizing observations based on their features.

**Identify the cluster that had the highest pcs/m and cite the composition of buildings, forest, undefined, the units are average proportion of the buffer**: The cluster that had the highest pcs/m was cluster 2, with an average of 1.02 objects per meter of beach. The composition of this cluster is as follows: buildings = 0.46, forest = 0.33, and undefined land use = 0.21, representing the average proportion of the buffer zone.

**Define linear regression and ensemble regression, explain the basic assumptions of each method**: Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data. The basic assumptions of linear regression include linearity, independence of errors, homoscedasticity (constant variance of errors), and normality of error terms. Ensemble regression, on the other hand, combines multiple regression models to improve prediction accuracy. Basic assumptions for ensemble methods include the independence of individual models and the assumption that the combined models can reduce variance and bias, thereby improving overall performance.

**If a regression analysis was conducted cite the model that had the highest r², cite the name and the MSE**: The model that had the highest R² was the Bagging: Random Forest Regression with an R² of 0.62 and a mean squared error (MSE) of 0.48.

**If there was a regression analysis conducted, what conclusions can be drawn given the best model? Given the r² and MSE of the best model how reliable would predictions be?**: Given that the Bagging: Random Forest Regression model had the highest R² value of 0.62, it indicates a moderate level of explained variance in the data, suggesting that the model can reasonably predict outcomes based on the input features. The MSE of 0.48 indicates that there is some error in the predictions, but it is not excessively high, suggesting that the model's predictions could be considered reliable within the context of the data.



:::{dropdown} Linear methods frequently asked questions
### Frequently asked questions

**What were the r² and MSE of each test?**: The following are the R² and MSE results from the regression analysis conducted:

|    | Model                            |       R² |      MSE |
|---:|:---------------------------------|---------:|---------:|
|  0 | Linear Regression                | 0.17     | 1.05     |
|  1 | Random Forest Regression         | 0.61     | 0.49     |
|  2 | Gradient Boosting Regression     | 0.16     | 1.07     |
|  3 | Theil-Sen Regressor              | 0.22     | 0.99     |
|  4 | Bagging: Random Forest Regression| 0.62     | 0.48     |
|  5 | Voting                           | 0.38     | 0.78     |

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**: The reliability of predictions varies across the different models. The Bagging: Random Forest Regression, with an R² of 0.62 and MSE of 0.48, indicates a moderate level of reliability. However, models such as Linear Regression and Gradient Boosting Regression show lower R² values and higher MSE, suggesting less reliable predictions.

**Can any conclusions be drawn from these results?**: Yes, conclusions can be drawn regarding the effectiveness of different regression models. The Bagging: Random Forest Regression model appears to be the most effective in predicting outcomes, as evidenced by its highest R² and lowest MSE. This suggests that ensemble methods may provide better predictive performance compared to simpler models like Linear Regression.

**According to the cluster analysis what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**: According to the cluster analysis, cluster 2 has the greatest average pcs/m, with an average of 1.02 objects per meter of beach. The distribution of land use values within this cluster is as follows: buildings occupy 46.3% of the buffer, forest occupies 33%, and undefined land use occupies 20.6%.
:::

## Forecasts and methods

A grid approximation is a statistical method used to estimate the probability of survey results exceeding a given threshold by employing prior observations and new data. It is constructed using an inference table, which contains the statistical measures derived from the data, including priors and likelihoods. An inference table summarizes the relationship between prior distributions (previously observed data) and likelihood distributions (data from the specific location being analyzed) to create posterior distributions (updated beliefs after considering new data). 

In the context of this report, the priors and their respective similarity thresholds are as follows:
1. **In boundary prior**: 0.98
2. **Out boundary prior**: 0.98

The posterior distributions for the different grid approximations provide a comparison to the observed results in terms of objects per meter (pcs/m). The observed average pcs/m from the summary statistics is 0.61. The average pcs/m for each posterior is as follows:
- **In boundary posterior**: 0.96 (difference from observed: 0.35)
- **Out boundary posterior**: 0.98 (difference from observed: 0.37)
- **Combined posterior**: 0.62 (difference from observed: 0.01)

In general, the in-boundary and out-boundary posteriors suggest a higher average than the observed value, indicating a likelihood of an increase in trash density within those boundaries.

When considering the likelihood of noticing changes in trash density, if a person takes one sample, they may not be able to confidently determine an increase or decrease. However, if two samples are taken, the likelihood of noticing a change increases, as the combined data from two samples can provide a clearer picture of the density trends.


::::{grid} 1
:margin: 0

:::{grid-item}
:padding: 0

![image info](bern/boxplots_observed_expected.jpeg)

:::

::::


:::{dropdown} Grid approximation frequently asked questions
### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**  
Grid approximation is a reasonable modeling technique given the data because it allows for the estimation of probabilities across a specified range, accounting for both prior knowledge and new information. In this case, the mean pcs/m is 0.61, while the median is 0.34. The difference between the mean and median (0.27) suggests that the data may not be normally distributed, as a normal distribution typically has mean and median values that are close together. If the data were normally distributed, we could expect the predictions from the grid approximation to be more reliable. However, since it appears skewed, this indicates that the predictions may have higher uncertainties, especially in the context of trash density.

**2. Do you have an example of other fields or domains that use grid approximation or Bayesian methods?**  
Yes, grid approximation and Bayesian methods are used in various fields, including environmental science for assessing pollution levels, finance for risk assessment, and clinical research for estimating the efficacy of treatments.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**  
If the data is normally distributed, the predictions from the grid approximation may align more closely with those from a normal distribution approach. The normal distribution would provide a clear mean and standard deviation, which can be used to make probabilistic predictions about new observations. In contrast, grid approximation might show wider variations in predictions due to the incorporation of less reliable priors.

**4. What is the difference between grid approximation and linear or ensemble regression?**  
Grid approximation focuses on estimating probabilities of outcomes based on prior distributions and new data, treating each grid point as a potential threshold. Linear regression, on the other hand, identifies a linear relationship between dependent and independent variables, while ensemble regression combines multiple models to improve prediction accuracy. Grid approximation does not assume a linear relationship and is more flexible in handling different distributions.

**5. With which posterior do we expect to find most? The least?**  
We expect to find the most with the **in boundary posterior**, which averages 0.96 pcs/m, suggesting higher trash density within the boundary. Conversely, we would expect to find the least with the **combined posterior**, which averages 0.62 pcs/m, indicating a lower density compared to the in-boundary and out-boundary estimates.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**  
If the in-boundary grid approximation predicts an increase, it suggests that there were likely elevated values observed in other locations within the boundary compared to the likelihood. This weighting indicates a trend of increasing trash density based on the aggregated data from various locations.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**  
If the out-boundary grid approximation predicts an increase, it indicates that other locations outside the boundary exhibited elevated values compared to the likelihood. This suggests that the trash density in areas outside the boundary may be contributing to an overall increase in trash density trends.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**  
The expected results differ from the observed results, with the in-boundary posterior averaging 0.96 and the out-boundary posterior averaging 0.98, compared to the observed average of 0.61. The differences in average pcs/m indicate a potential increase in trash density. Given the standard deviations of the posteriors (0.94 for in-boundary and 0.99 for out-boundary), it seems reasonable to expect an increase in future observations, particularly given that the observed value is lower than both the in-boundary and out-boundary predictions.
:::

## Consolidated results : city, survey area


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_b6e99 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_b6e99 tr:nth-child(odd) {
  background: #FFF;
}
#T_b6e99 tr {
  font-size: 12px;
}
#T_b6e99 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_b6e99 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_b6e99 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b6e99  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b6e99  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b6e99  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b6e99 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_b6e99">
  <caption>Sample totals : city, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_b6e99_level0_col0" class="col_heading level0 col0" >city</th>
      <th id="T_b6e99_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_b6e99_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_b6e99_row0_col0" class="data row0 col0" >Beatenberg</td>
      <td id="T_b6e99_row0_col1" class="data row0 col1" >29</td>
      <td id="T_b6e99_row0_col2" class="data row0 col2" >0,67</td>
    </tr>
    <tr>
      <td id="T_b6e99_row1_col0" class="data row1 col0" >Bern</td>
      <td id="T_b6e99_row1_col1" class="data row1 col1" >10</td>
      <td id="T_b6e99_row1_col2" class="data row1 col2" >0,07</td>
    </tr>
    <tr>
      <td id="T_b6e99_row2_col0" class="data row2 col0" >Biel/Bienne</td>
      <td id="T_b6e99_row2_col1" class="data row2 col1" >1'034</td>
      <td id="T_b6e99_row2_col2" class="data row2 col2" >1,62</td>
    </tr>
    <tr>
      <td id="T_b6e99_row3_col0" class="data row3 col0" >Brienz (BE)</td>
      <td id="T_b6e99_row3_col1" class="data row3 col1" >68</td>
      <td id="T_b6e99_row3_col2" class="data row3 col2" >0,46</td>
    </tr>
    <tr>
      <td id="T_b6e99_row4_col0" class="data row4 col0" >Brügg</td>
      <td id="T_b6e99_row4_col1" class="data row4 col1" >10</td>
      <td id="T_b6e99_row4_col2" class="data row4 col2" >0,28</td>
    </tr>
    <tr>
      <td id="T_b6e99_row5_col0" class="data row5 col0" >Burgdorf</td>
      <td id="T_b6e99_row5_col1" class="data row5 col1" >4</td>
      <td id="T_b6e99_row5_col2" class="data row5 col2" >0,09</td>
    </tr>
    <tr>
      <td id="T_b6e99_row6_col0" class="data row6 col0" >Bönigen</td>
      <td id="T_b6e99_row6_col1" class="data row6 col1" >106</td>
      <td id="T_b6e99_row6_col2" class="data row6 col2" >1,25</td>
    </tr>
    <tr>
      <td id="T_b6e99_row7_col0" class="data row7 col0" >Erlach</td>
      <td id="T_b6e99_row7_col1" class="data row7 col1" >28</td>
      <td id="T_b6e99_row7_col2" class="data row7 col2" >0,49</td>
    </tr>
    <tr>
      <td id="T_b6e99_row8_col0" class="data row8 col0" >Gals</td>
      <td id="T_b6e99_row8_col1" class="data row8 col1" >8</td>
      <td id="T_b6e99_row8_col2" class="data row8 col2" >0,21</td>
    </tr>
    <tr>
      <td id="T_b6e99_row9_col0" class="data row9 col0" >Kallnach</td>
      <td id="T_b6e99_row9_col1" class="data row9 col1" >5</td>
      <td id="T_b6e99_row9_col2" class="data row9 col2" >0,08</td>
    </tr>
    <tr>
      <td id="T_b6e99_row10_col0" class="data row10 col0" >Köniz</td>
      <td id="T_b6e99_row10_col1" class="data row10 col1" >6</td>
      <td id="T_b6e99_row10_col2" class="data row10 col2" >0,09</td>
    </tr>
    <tr>
      <td id="T_b6e99_row11_col0" class="data row11 col0" >Ligerz</td>
      <td id="T_b6e99_row11_col1" class="data row11 col1" >24</td>
      <td id="T_b6e99_row11_col2" class="data row11 col2" >1,54</td>
    </tr>
    <tr>
      <td id="T_b6e99_row12_col0" class="data row12 col0" >Lüscherz</td>
      <td id="T_b6e99_row12_col1" class="data row12 col1" >17</td>
      <td id="T_b6e99_row12_col2" class="data row12 col2" >0,06</td>
    </tr>
    <tr>
      <td id="T_b6e99_row13_col0" class="data row13 col0" >Nidau</td>
      <td id="T_b6e99_row13_col1" class="data row13 col1" >15</td>
      <td id="T_b6e99_row13_col2" class="data row13 col2" >0,60</td>
    </tr>
    <tr>
      <td id="T_b6e99_row14_col0" class="data row14 col0" >Port</td>
      <td id="T_b6e99_row14_col1" class="data row14 col1" >61</td>
      <td id="T_b6e99_row14_col2" class="data row14 col2" >0,70</td>
    </tr>
    <tr>
      <td id="T_b6e99_row15_col0" class="data row15 col0" >Rubigen</td>
      <td id="T_b6e99_row15_col1" class="data row15 col1" >3</td>
      <td id="T_b6e99_row15_col2" class="data row15 col2" >0,17</td>
    </tr>
    <tr>
      <td id="T_b6e99_row16_col0" class="data row16 col0" >Spiez</td>
      <td id="T_b6e99_row16_col1" class="data row16 col1" >50</td>
      <td id="T_b6e99_row16_col2" class="data row16 col2" >0,08</td>
    </tr>
    <tr>
      <td id="T_b6e99_row17_col0" class="data row17 col0" >Thun</td>
      <td id="T_b6e99_row17_col1" class="data row17 col1" >65</td>
      <td id="T_b6e99_row17_col2" class="data row17 col2" >0,31</td>
    </tr>
    <tr>
      <td id="T_b6e99_row18_col0" class="data row18 col0" >Unterseen</td>
      <td id="T_b6e99_row18_col1" class="data row18 col1" >658</td>
      <td id="T_b6e99_row18_col2" class="data row18 col2" >0,69</td>
    </tr>
    <tr>
      <td id="T_b6e99_row19_col0" class="data row19 col0" >Vinelz</td>
      <td id="T_b6e99_row19_col1" class="data row19 col1" >59</td>
      <td id="T_b6e99_row19_col2" class="data row19 col2" >0,33</td>
    </tr>
    <tr>
      <td id="T_b6e99_row20_col0" class="data row20 col0" >Walperswil</td>
      <td id="T_b6e99_row20_col1" class="data row20 col1" >0</td>
      <td id="T_b6e99_row20_col2" class="data row20 col2" >0,00</td>
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
#T_fc512 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_fc512 tr:nth-child(odd) {
  background: #FFF;
}
#T_fc512 tr {
  font-size: 12px;
}
#T_fc512 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_fc512 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_fc512 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_fc512  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_fc512  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_fc512  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_fc512 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_fc512">
  <caption>Sample totals : parent_boundary, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_fc512_level0_col0" class="col_heading level0 col0" >parent_boundary</th>
      <th id="T_fc512_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_fc512_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_fc512_row0_col0" class="data row0 col0" >aare</td>
      <td id="T_fc512_row0_col1" class="data row0 col1" >2'260</td>
      <td id="T_fc512_row0_col2" class="data row0 col2" >0,61</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::

## Inventory

<div>
<style type="text/css">
#T_cffff tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_cffff tr:nth-child(odd) {
  background: #FFF;
}
#T_cffff tr {
  font-size: 12px;
}
#T_cffff th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_cffff td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_cffff table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_cffff  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_cffff  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_cffff  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_cffff caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_cffff">
  <caption> </caption>
  <thead>
    <tr>
      <th id="T_cffff_level0_col0" class="col_heading level0 col0" >quantity</th>
      <th id="T_cffff_level0_col1" class="col_heading level0 col1" >pcs/m</th>
      <th id="T_cffff_level0_col2" class="col_heading level0 col2" >% of total</th>
      <th id="T_cffff_level0_col3" class="col_heading level0 col3" >sample_id</th>
      <th id="T_cffff_level0_col4" class="col_heading level0 col4" >fail rate</th>
      <th id="T_cffff_level0_col5" class="col_heading level0 col5" >object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_cffff_row0_col0" class="data row0 col0" >1'671</td>
      <td id="T_cffff_row0_col1" class="data row0 col1" >0,42</td>
      <td id="T_cffff_row0_col2" class="data row0 col2" >0,74</td>
      <td id="T_cffff_row0_col3" class="data row0 col3" >89</td>
      <td id="T_cffff_row0_col4" class="data row0 col4" >0,81</td>
      <td id="T_cffff_row0_col5" class="data row0 col5" >Cigarette filters</td>
    </tr>
    <tr>
      <td id="T_cffff_row1_col0" class="data row1 col0" >589</td>
      <td id="T_cffff_row1_col1" class="data row1 col1" >0,19</td>
      <td id="T_cffff_row1_col2" class="data row1 col2" >0,26</td>
      <td id="T_cffff_row1_col3" class="data row1 col3" >89</td>
      <td id="T_cffff_row1_col4" class="data row1 col4" >0,80</td>
      <td id="T_cffff_row1_col5" class="data row1 col5" >Food wrappers; candy, snacks</td>
    </tr>
  </tbody>
</table>


</div>
