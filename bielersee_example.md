
# Bielersee - example

**Summary and analysis of observations of trash density**: objects related to tobacco and food and drink found in lakes. <i>Report number: Bielersee - example lake 2020-01-01 2021-05-31</i>

 <i>Proof of concept: llm assissted reporting grid forecasting example</i>

## Executive Summary

The Bielersee report, covering the period from January 26, 2020, to March 31, 2021, includes data from eight cities: Biel/Bienne, Vinelz, Lüscherz, Nidau, Gals, Erlach, Le Landeron, and Ligerz, with the survey area identified as Aare and one lake, Bielersee. A total of 39 samples were collected, yielding an average of 0.92 pcs/m, a maximum of 3.88 pcs/m, a median of 0.41 pcs/m, and a standard deviation of 1.10 pcs/m. The total number of objects identified was 1,166. The five most common objects were cigarette filters (fail rate: 79.49%, 70.24% of total), and food wrappers (fail rate: 87.18%, 29.76% of total).

Sampling stratification is a method used to ensure that survey samples are representative of the various land-use features surrounding the survey locations. The survey locations were classified as mixed areas since the sum of the proportions of samples for buildings and forests did not exceed 50% in the relevant buffer zones. The highest trash density was found in the 'forest' category with 2.00 pcs/m in the 40-60% buffer zone, where 33.3% of the samples were collected. The sampling stratification table helps quantify the relationship between land use and litter density, highlighting areas where trash density is particularly high.

The regression analysis conducted indicated that the Bagging: Gradient Boosting Regression model had the highest R² of 0.30 and a mean squared error (MSE) of 0.72. Feature importance analysis revealed that 'streets' (0.274337) and 'buildings' (0.218129) were the most significant predictors. Permutation feature importance showed that 'buildings' (0.137264) and 'streets' (0.0350437) were crucial. Despite these findings, the relatively low R² values suggest that the models only capture a small portion of the variance in the data, indicating limited predictive reliability.

Grid approximation, a Bayesian inference technique, was employed to estimate the conditional probabilities of survey outcomes. The in-boundary and out-boundary priors yielded average pcs/m values of 0.97 and 1.04, respectively, compared to the observed average of 0.92 pcs/m. Both priors suggest an expected increase in trash density, with the out-boundary posterior indicating a higher increase.
## Sample results

The report details administrative boundaries including a total of eight cities: Biel/Bienne, Vinelz, Lüscherz, Nidau, Gals, Erlach, Le Landeron, and Ligerz. The survey area identified is Aare. There is one lake included in the report, which is Bielersee, and no parks are mentioned.

The sampling period spans from January 26, 2020, to March 31, 2021. A total of 39 samples were collected, yielding an average of 0.92 pcs/m, a median of 0.41 pcs/m, and a maximum of 3.88 pcs/m. The standard deviation of the sample data is 1.10, and the total number of objects identified during the survey is 1,166.

The most common objects identified with the greatest quantity were:
1. Cigarette filters: Fail rate of 79.49%, 70.24% of total, 0.60 pcs/m, total quantity of 819.
2. Food wrappers (candy, snacks): Fail rate of 87.18%, 29.76% of total, 0.32 pcs/m, total quantity of 347.

The material composition of the objects found was exclusively plastic, comprising 100% of the total identified materials.


:::{dropdown} Sample results frequently asked questions
### Frequently asked questions

**What were the ten most common items found?**  
The two most common items found were as follows:
1. Cigarette filters: Fail rate of 79.49%, 70.24% of total.
2. Food wrappers (candy, snacks): Fail rate of 87.18%, 29.76% of total.  
(Note: Only two objects met the criteria for reporting.)

**Are these objects found on European beaches? If so, is there any data on how many per 100 m of beach?**  
Yes, these objects are commonly found on European beaches. According to the OSPAR report from 2021, the average number of items found on beaches is reported to be 150 pieces per 100 m. For more details, you can access the report here: [OSPAR Beach Litter Report 2021](https://www.ospar.org/documents?v=40827).

**What are possible sources of these specific objects?**  
Possible sources of cigarette filters may include recreational areas such as parks, beaches, and public spaces where smoking occurs. Food wrappers are typically linked to fast food outlets, convenience stores, and picnics, where individuals consume snacks and convenience foods outdoors.

**Which three cities had the highest average pcs/m? Which three had the lowest?**  
The three cities with the highest average pcs/m were:
1. Biel/Bienne: 1.79 pcs/m
2. Ligerz: 1.55 pcs/m
3. Erlach: 0.49 pcs/m  

The three cities with the lowest average pcs/m were:
1. Lüscherz: 0.06 pcs/m
2. Gals: 0.21 pcs/m
3. Vinelz: 0.33 pcs/m
:::

::::{grid} 1
:margin 0
:padding: 0

:::{grid-item-card}
:padding: 0
:img-background: bielersee/situation_map.jpg

:::

::::


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_72b3d_row0_col0, #T_72b3d_row0_col1, #T_72b3d_row0_col2, #T_72b3d_row0_col3, #T_72b3d_row0_col4, #T_72b3d_row0_col5, #T_72b3d_row0_col6 {
  background-color: rgba(31, 119, 180, 0.6);
  color: white;
}
#T_72b3d_row1_col0, #T_72b3d_row1_col1, #T_72b3d_row1_col2, #T_72b3d_row1_col3, #T_72b3d_row1_col4, #T_72b3d_row1_col5, #T_72b3d_row1_col6 {
  background-color: rgba(174, 199, 232, 0.6);
  color: black;
}
#T_72b3d_row2_col0, #T_72b3d_row2_col1, #T_72b3d_row2_col2, #T_72b3d_row2_col3, #T_72b3d_row2_col4, #T_72b3d_row2_col5, #T_72b3d_row2_col6 {
  background-color: rgba(255, 127, 14, 0.6);
  color: black;
}
</style>
<table id="T_72b3d">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_72b3d_level0_col0" class="col_heading level0 col0" >pcs/m</th>
      <th id="T_72b3d_level0_col1" class="col_heading level0 col1" >buildings</th>
      <th id="T_72b3d_level0_col2" class="col_heading level0 col2" >forest</th>
      <th id="T_72b3d_level0_col3" class="col_heading level0 col3" >undefined</th>
      <th id="T_72b3d_level0_col4" class="col_heading level0 col4" >streets</th>
      <th id="T_72b3d_level0_col5" class="col_heading level0 col5" >public-services</th>
      <th id="T_72b3d_level0_col6" class="col_heading level0 col6" >recreation</th>
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
      <th id="T_72b3d_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_72b3d_row0_col0" class="data row0 col0" >1,04</td>
      <td id="T_72b3d_row0_col1" class="data row0 col1" >0,31</td>
      <td id="T_72b3d_row0_col2" class="data row0 col2" >0,11</td>
      <td id="T_72b3d_row0_col3" class="data row0 col3" >0,54</td>
      <td id="T_72b3d_row0_col4" class="data row0 col4" >0,44</td>
      <td id="T_72b3d_row0_col5" class="data row0 col5" >0,06</td>
      <td id="T_72b3d_row0_col6" class="data row0 col6" >0,03</td>
    </tr>
    <tr>
      <th id="T_72b3d_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_72b3d_row1_col0" class="data row1 col0" >0,06</td>
      <td id="T_72b3d_row1_col1" class="data row1 col1" >0,17</td>
      <td id="T_72b3d_row1_col2" class="data row1 col2" >0,56</td>
      <td id="T_72b3d_row1_col3" class="data row1 col3" >0,13</td>
      <td id="T_72b3d_row1_col4" class="data row1 col4" >0,00</td>
      <td id="T_72b3d_row1_col5" class="data row1 col5" >0,04</td>
      <td id="T_72b3d_row1_col6" class="data row1 col6" >0,00</td>
    </tr>
    <tr>
      <th id="T_72b3d_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_72b3d_row2_col0" class="data row2 col0" >1,16</td>
      <td id="T_72b3d_row2_col1" class="data row2 col1" >0,32</td>
      <td id="T_72b3d_row2_col2" class="data row2 col2" >0,11</td>
      <td id="T_72b3d_row2_col3" class="data row2 col3" >0,48</td>
      <td id="T_72b3d_row2_col4" class="data row2 col4" >0,71</td>
      <td id="T_72b3d_row2_col5" class="data row2 col5" >0,13</td>
      <td id="T_72b3d_row2_col6" class="data row2 col6" >0,02</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::
## Sampling stratification

Sampling stratification is a method used to ensure that survey samples are representative of the various land-use features surrounding the survey locations. In this context, each survey location is surrounded by a buffer zone of 1,500 meters, which includes various land-use features, such as buildings, forests, wetlands, and streets. The proportion of each land use feature within the buffer zone is quantified, allowing researchers to analyze how these features might influence litter density. The survey results are interpreted by examining how trash density varies according to the different land-use conditions present in the buffer zones surrounding each sampled location.

The highest pieces of trash per meter (pcs/m) values in the sampling stratification and trash density table are found in the 'forest' and 'undefined' columns. For the forest category, the highest value is 2.00 pcs/m, which occurs in the 40-60% buffer zone, where 33.3% of the samples were collected. In the undefined category, the highest value is 1.55 pcs/m, which occurs in the 20-40% buffer zone, where 5.1% of the samples were collected. These values indicate that areas with a higher proportion of forests and undefined land-use features show a significant presence of trash.

To classify the surveyed locations, we examine the proportions of samples collected according to the definitions of urban, rural, and mixed areas. The sum of the proportions of samples for buildings in the rows 60-80% and 80-100% of the sampling stratification table is 7.7% + 0%, which is less than 50%. For forests, the sum of the proportions in the same rows is also 0% + 0%, which is also less than 50%. Thus, we classify the surveyed locations as mixed. 




::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_f850f tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_f850f tr:nth-child(odd) {
  background: #FFF;
}
#T_f850f tr {
  font-size: 12px;
}
#T_f850f th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_f850f td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_f850f table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_f850f  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_f850f  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_f850f  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_f850f caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_f850f">
  <caption>
Each survey location is surrounded by a buffer zone of radius = 1 500 meters. The buffer zone is comprised of land-use features, each land use feature occupies a proportion of the buffer zone (0 - 100%). The land-use-profile is measured by considering the proportion of the buffer dedicated to each of land use feature that is present in the buffer zone. Each location has the same size buffer zone. What changes is how the land use features are distributed within the buffer zone, Which means we assume that locations that have a similar distribution of features in the buffer zone should have similar survey results. The sampling stratification tells us under what conditions the surveys were collected and what proportions of the samples were taken according to the different conditions.
</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_f850f_level0_col0" class="col_heading level0 col0" colspan="9">Proportion of samples collected</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_f850f_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_f850f_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_f850f_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_f850f_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_f850f_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_f850f_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_f850f_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_f850f_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_f850f_level1_col8" class="col_heading level1 col8" >orchards</th>
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
      <th id="T_f850f_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_f850f_row0_col0" class="data row0 col0" >17.9%</td>
      <td id="T_f850f_row0_col1" class="data row0 col1" >100.0%</td>
      <td id="T_f850f_row0_col2" class="data row0 col2" >38.5%</td>
      <td id="T_f850f_row0_col3" class="data row0 col3" >100.0%</td>
      <td id="T_f850f_row0_col4" class="data row0 col4" >100.0%</td>
      <td id="T_f850f_row0_col5" class="data row0 col5" >53.8%</td>
      <td id="T_f850f_row0_col6" class="data row0 col6" >20.5%</td>
      <td id="T_f850f_row0_col7" class="data row0 col7" >100.0%</td>
      <td id="T_f850f_row0_col8" class="data row0 col8" >100.0%</td>
    </tr>
    <tr>
      <th id="T_f850f_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_f850f_row1_col0" class="data row1 col0" >41.0%</td>
      <td id="T_f850f_row1_col1" class="data row1 col1" >none</td>
      <td id="T_f850f_row1_col2" class="data row1 col2" >48.7%</td>
      <td id="T_f850f_row1_col3" class="data row1 col3" >none</td>
      <td id="T_f850f_row1_col4" class="data row1 col4" >none</td>
      <td id="T_f850f_row1_col5" class="data row1 col5" >5.1%</td>
      <td id="T_f850f_row1_col6" class="data row1 col6" >5.1%</td>
      <td id="T_f850f_row1_col7" class="data row1 col7" >none</td>
      <td id="T_f850f_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_f850f_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_f850f_row2_col0" class="data row2 col0" >33.3%</td>
      <td id="T_f850f_row2_col1" class="data row2 col1" >none</td>
      <td id="T_f850f_row2_col2" class="data row2 col2" >12.8%</td>
      <td id="T_f850f_row2_col3" class="data row2 col3" >none</td>
      <td id="T_f850f_row2_col4" class="data row2 col4" >none</td>
      <td id="T_f850f_row2_col5" class="data row2 col5" >41.0%</td>
      <td id="T_f850f_row2_col6" class="data row2 col6" >30.8%</td>
      <td id="T_f850f_row2_col7" class="data row2 col7" >none</td>
      <td id="T_f850f_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_f850f_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_f850f_row3_col0" class="data row3 col0" >7.7%</td>
      <td id="T_f850f_row3_col1" class="data row3 col1" >none</td>
      <td id="T_f850f_row3_col2" class="data row3 col2" >none</td>
      <td id="T_f850f_row3_col3" class="data row3 col3" >none</td>
      <td id="T_f850f_row3_col4" class="data row3 col4" >none</td>
      <td id="T_f850f_row3_col5" class="data row3 col5" >none</td>
      <td id="T_f850f_row3_col6" class="data row3 col6" >35.9%</td>
      <td id="T_f850f_row3_col7" class="data row3 col7" >none</td>
      <td id="T_f850f_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_f850f_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_f850f_row4_col0" class="data row4 col0" >none</td>
      <td id="T_f850f_row4_col1" class="data row4 col1" >none</td>
      <td id="T_f850f_row4_col2" class="data row4 col2" >none</td>
      <td id="T_f850f_row4_col3" class="data row4 col3" >none</td>
      <td id="T_f850f_row4_col4" class="data row4 col4" >none</td>
      <td id="T_f850f_row4_col5" class="data row4 col5" >none</td>
      <td id="T_f850f_row4_col6" class="data row4 col6" >5.1%</td>
      <td id="T_f850f_row4_col7" class="data row4 col7" >none</td>
      <td id="T_f850f_row4_col8" class="data row4 col8" >none</td>
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
#T_9b1aa tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_9b1aa tr:nth-child(odd) {
  background: #FFF;
}
#T_9b1aa tr {
  font-size: 12px;
}
#T_9b1aa th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_9b1aa td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_9b1aa table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9b1aa  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9b1aa  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9b1aa  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_9b1aa caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_9b1aa">
  <caption>
The land use profile allows us to group locations according to the topography. Here we consdider how the observed litter density changes based on the land use feature and the proportion of the buffer-zone that the feature occupies</caption>
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9b1aa_level0_col0" class="col_heading level0 col0" colspan="9">Pieces of trash per meter</th>
    </tr>
    <tr>
      <th class="blank level1" >&nbsp;</th>
      <th id="T_9b1aa_level1_col0" class="col_heading level1 col0" >buildings</th>
      <th id="T_9b1aa_level1_col1" class="col_heading level1 col1" >wetlands</th>
      <th id="T_9b1aa_level1_col2" class="col_heading level1 col2" >forest</th>
      <th id="T_9b1aa_level1_col3" class="col_heading level1 col3" >public-services</th>
      <th id="T_9b1aa_level1_col4" class="col_heading level1 col4" >recreation</th>
      <th id="T_9b1aa_level1_col5" class="col_heading level1 col5" >undefined</th>
      <th id="T_9b1aa_level1_col6" class="col_heading level1 col6" >streets</th>
      <th id="T_9b1aa_level1_col7" class="col_heading level1 col7" >vineyards</th>
      <th id="T_9b1aa_level1_col8" class="col_heading level1 col8" >orchards</th>
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
      <th id="T_9b1aa_level0_row0" class="row_heading level0 row0" >0-20%</th>
      <td id="T_9b1aa_row0_col0" class="data row0 col0" >0,48</td>
      <td id="T_9b1aa_row0_col1" class="data row0 col1" >0,92</td>
      <td id="T_9b1aa_row0_col2" class="data row0 col2" >0,36</td>
      <td id="T_9b1aa_row0_col3" class="data row0 col3" >0,92</td>
      <td id="T_9b1aa_row0_col4" class="data row0 col4" >0,92</td>
      <td id="T_9b1aa_row0_col5" class="data row0 col5" >1,32</td>
      <td id="T_9b1aa_row0_col6" class="data row0 col6" >0,48</td>
      <td id="T_9b1aa_row0_col7" class="data row0 col7" >0,92</td>
      <td id="T_9b1aa_row0_col8" class="data row0 col8" >0,92</td>
    </tr>
    <tr>
      <th id="T_9b1aa_level0_row1" class="row_heading level0 row1" >20-40%</th>
      <td id="T_9b1aa_row1_col0" class="data row1 col0" >0,33</td>
      <td id="T_9b1aa_row1_col1" class="data row1 col1" >none</td>
      <td id="T_9b1aa_row1_col2" class="data row1 col2" >1,60</td>
      <td id="T_9b1aa_row1_col3" class="data row1 col3" >none</td>
      <td id="T_9b1aa_row1_col4" class="data row1 col4" >none</td>
      <td id="T_9b1aa_row1_col5" class="data row1 col5" >1,54</td>
      <td id="T_9b1aa_row1_col6" class="data row1 col6" >0,21</td>
      <td id="T_9b1aa_row1_col7" class="data row1 col7" >none</td>
      <td id="T_9b1aa_row1_col8" class="data row1 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9b1aa_level0_row2" class="row_heading level0 row2" >40-60%</th>
      <td id="T_9b1aa_row2_col0" class="data row2 col0" >2,00</td>
      <td id="T_9b1aa_row2_col1" class="data row2 col1" >none</td>
      <td id="T_9b1aa_row2_col2" class="data row2 col2" >0,06</td>
      <td id="T_9b1aa_row2_col3" class="data row2 col3" >none</td>
      <td id="T_9b1aa_row2_col4" class="data row2 col4" >none</td>
      <td id="T_9b1aa_row2_col5" class="data row2 col5" >0,33</td>
      <td id="T_9b1aa_row2_col6" class="data row2 col6" >0,33</td>
      <td id="T_9b1aa_row2_col7" class="data row2 col7" >none</td>
      <td id="T_9b1aa_row2_col8" class="data row2 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9b1aa_level0_row3" class="row_heading level0 row3" >60-80%</th>
      <td id="T_9b1aa_row3_col0" class="data row3 col0" >0,48</td>
      <td id="T_9b1aa_row3_col1" class="data row3 col1" >none</td>
      <td id="T_9b1aa_row3_col2" class="data row3 col2" >none</td>
      <td id="T_9b1aa_row3_col3" class="data row3 col3" >none</td>
      <td id="T_9b1aa_row3_col4" class="data row3 col4" >none</td>
      <td id="T_9b1aa_row3_col5" class="data row3 col5" >none</td>
      <td id="T_9b1aa_row3_col6" class="data row3 col6" >1,88</td>
      <td id="T_9b1aa_row3_col7" class="data row3 col7" >none</td>
      <td id="T_9b1aa_row3_col8" class="data row3 col8" >none</td>
    </tr>
    <tr>
      <th id="T_9b1aa_level0_row4" class="row_heading level0 row4" >80-100%</th>
      <td id="T_9b1aa_row4_col0" class="data row4 col0" >none</td>
      <td id="T_9b1aa_row4_col1" class="data row4 col1" >none</td>
      <td id="T_9b1aa_row4_col2" class="data row4 col2" >none</td>
      <td id="T_9b1aa_row4_col3" class="data row4 col3" >none</td>
      <td id="T_9b1aa_row4_col4" class="data row4 col4" >none</td>
      <td id="T_9b1aa_row4_col5" class="data row4 col5" >none</td>
      <td id="T_9b1aa_row4_col6" class="data row4 col6" >0,42</td>
      <td id="T_9b1aa_row4_col7" class="data row4 col7" >none</td>
      <td id="T_9b1aa_row4_col8" class="data row4 col8" >none</td>
    </tr>
  </tbody>
</table>
</div>



:::

::::
:::{dropdown} Sampling stratification frequently asked questions
### Frequently asked questions

**What does the sampling stratification table tell us?**  
The sampling stratification table provides insight into the distribution of samples collected based on different land-use features. For example, in the buildings category, the highest average pcs/m is 2.00, observed in the 40-60% buffer zone, where 33.3% of the samples were taken. This indicates that as the proportion of buildings in the buffer zone increases to 40-60%, there is a corresponding increase in trash density. Similarly, in the undefined category, the average pcs/m is 1.55, found in the 20-40% buffer zone, where 5.1% of the samples were collected. This suggests that undefined land-use areas also exhibit a notable amount of trash. These examples illustrate how the table quantifies the relationship between land use and litter density, highlighting locations where trash density is particularly high.

**How can the information in the sampling stratification and trash density table help identify areas of concern?**  
The information provided in the sampling stratification and trash density table is crucial for identifying areas of concern regarding litter management and environmental health. By linking trash density with specific land-use features, it becomes possible to pinpoint locations that are particularly affected by litter. For instance, areas with a high density of buildings may indicate urban environments where litter is more prevalent. Understanding these relationships allows policymakers and environmental managers to devise targeted interventions in high-density litter areas, ultimately improving local environmental quality and public health.

**Under what land-use conditions would a surveyor expect to find the most trash?**  
Surveyors would expect to find the most trash in areas characterized by a higher proportion of buildings and undefined land use. Specifically, the sampling stratification and trash density table indicates that the highest average pcs/m for buildings is 2.00, observed in the 40-60% buffer zone, where 33.3% of the samples were collected. For undefined land use, the average pcs/m is 1.55, found in the 20-40% buffer zone, where 5.1% of the samples were taken. These findings suggest that as the proportions of buildings and undefined land increase, the density of trash also tends to rise, indicating that these land-use conditions are more prone to litter accumulation.

**Given the results in the sampling stratification table, were these surveys collected in mostly urban environments or forested?**  
The surveys were not collected in predominantly urban or forested environments. The proportion of samples for buildings in the relevant buffer zones sums to 7.7% (60-80%) + 0% (80-100%), which is less than 50%. Similarly, the sum for forests is 0% (60-80%) + 0% (80-100%). Therefore, these results classify the surveyed locations as mixed, indicating a more diverse land-use profile rather than a concentration in urban or forested areas.
:::

## Linear and ensemble methods

Cluster analysis, specifically K-Means clustering, is a statistical method used to categorize data points into distinct groups based on their similarities. It works by partitioning the dataset into K predefined clusters, with each data point assigned to the cluster whose centroid (mean) is closest to it. The goal is to minimize the variance within each cluster while maximizing the variance between clusters.

In the Bielersee example, the cluster with the highest average pcs/m was Cluster 2, with an average of 1.16 objects per meter of beach. The composition of land use values in this cluster was as follows: buildings accounted for 0.32 (32%), forests for 0.11 (11%), and undefined land use for 0.48 (48%) of the buffer zone.

Linear regression is a statistical method that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data. The basic assumptions of linear regression include linearity (the relationship between variables is linear), independence (the residuals are independent), homoscedasticity (constant variance of the residuals), and normality (the residuals should be normally distributed).

Ensemble regression refers to a combination of multiple regression models to improve predictive performance. It includes methods like Bagging and Boosting, which aggregate predictions from various models to produce a more robust estimate. The basic assumptions of ensemble regression methods depend on the individual models used, but generally, they assume that the models have some level of predictive power and that combining them will reduce variance and/or bias.

The regression analysis conducted indicated that the model with the highest R² was the Bagging: Gradient Boosting Regression, which had an R² of 0.30 and a mean squared error (MSE) of 0.72. Given these results, the conclusions that can be drawn suggest that while the model captures some of the variance in the data, the R² value indicates that only about 30% of the variability in the response variable can be explained by the model. The relatively low MSE also suggests that predictions made using this model may not be highly reliable, as they could vary significantly from the actual values.



:::{dropdown} Linear methods frequently asked questions
### Frequently asked questions

**What were the r² and MSE of each test?**  
The R² and MSE for each regression model tested are as follows: 
- Linear Regression: R² = -3.37, MSE = 4.51
- Random Forest Regression: R² = 0.20, MSE = 0.83
- Gradient Boosting Regression: R² = 0.30, MSE = 0.73
- Theil-Sen Regressor: R² = 0.01, MSE = 1.02
- Bagging: Gradient Boosting Regression: R² = 0.30, MSE = 0.72
- Voting: R² = -0.11, MSE = 1.14

**Given the r² and MSE of the different methods employed, how reliable do you think predictions would be based on these models?**  
The predictions based on these models generally exhibit low reliability. The negative R² values for some models indicate poor fit, suggesting that these models do not effectively explain the variability in the data. The best-performing model, Bagging: Gradient Boosting Regression, has a modest R² of 0.30, indicating that it explains only a small portion of the variance. The MSE values further suggest that there could be considerable error in the predictions.

**Can any conclusions be drawn from these results?**  
Yes, the results suggest that while some regression models can provide insights, the overall predictive power is limited. The highest-performing model explains only 30% of the variance, indicating that additional variables or alternative modeling approaches may be necessary to improve prediction accuracy.

**According to the cluster analysis, what is the cluster that has the greatest average pcs/m? What is the distribution of land use values within the cluster?**  
The cluster with the greatest average pcs/m is Cluster 2, which has an average of 1.16 objects per meter of beach. The distribution of land use values within this cluster is as follows: buildings account for 32% of the buffer zone, forests account for 11%, and undefined land use occupies 48% of the buffer.
:::

## Forecasts and methods

A grid approximation is a statistical technique used to estimate the conditional probabilities of outcomes based on prior observations and new data. It constructs a grid that spans the range of possible values, assessing how likely it is for a survey result to exceed or equal each value on the grid. This is achieved through a Bayesian inference approach, where prior distributions (based on historical data) are updated with new likelihood data derived from the specific observations being analyzed. 

An inference table is a structured format that displays prior and posterior distributions, providing a clear overview of the statistical characteristics of the data. The prior represents the information available before observing the new data, while the posterior is the updated belief after incorporating the new observations. In the context of this report, the priors used are the "in-boundary" and "out-boundary" datasets. The average cosine similarity score of the prior samples in both cases is 0.98. 

For each prior in the report, the results are as follows:
- **In-boundary prior**: Average pcs/m = 0.97, Median pcs/m = 0.60
- **Out-boundary prior**: Average pcs/m = 1.04, Median pcs/m = 0.63

When comparing the posterior distributions to the observed results, the observed average pcs/m is 0.92. The in-boundary posterior average is 0.97, which shows an increase of 0.05 compared to the observed average. In contrast, the out-boundary posterior average is 1.04, indicating an increase of 0.12. Given the standard deviations of the in-boundary (0.97) and out-boundary (1.01) distributions, it can be expected that an increase would be noticed, especially when taking more samples.

If a person takes one sample, the likelihood of noticing an increase or decrease from the observed results is fairly low due to the variability inherent in the data. However, if two samples are taken, the likelihood of detecting an increase or decrease becomes higher since the combined data can better reflect the underlying distribution trends.


::::{grid} 1
:margin: 0

:::{grid-item}
:padding: 0

![image info](bielersee/boxplots_observed_expected.jpeg)

:::

::::


:::{dropdown} Grid approximation frequently asked questions
### Frequently asked questions

**1. Why is grid approximation a reasonable modeling technique given the data?**  
Grid approximation is suitable because the observed data shows a mean of 0.92 and a median of 0.41, indicating that the data is likely not normally distributed (the mean is greater than the median). This suggests a skewness in the data distribution. If the data were normally distributed, predictions made with grid approximation would align closely with those from traditional normal distribution methods. However, given the observed skew, the predictions may vary significantly, highlighting the importance of using grid approximation to account for potential non-normal characteristics in the data.

**2. Do you have an example of other fields or domains that use grid approximation or Bayesian methods?**  
Grid approximation and Bayesian methods are widely used in various fields, including environmental science for ecological modeling, finance for risk assessment and portfolio management, and medical statistics for clinical trial analysis. These methods are valuable for updating beliefs based on new evidence in these domains.

**3. If the data is normally distributed, would the predictions from the grid approximation and the predictions from the normal distribution be different? If so, in what way?**  
If the data were normally distributed, the predictions from the grid approximation and the normal distribution would typically converge, leading to similar estimates of probabilities for outcomes. However, grid approximation can provide a more nuanced representation of the data, particularly in cases where the distribution is not strictly normal, allowing for better handling of skewness or kurtosis.

**4. What is the difference between grid approximation and linear or ensemble regression?**  
Grid approximation focuses on estimating probabilities of outcomes based on distributions and prior knowledge, while linear regression models the relationship between variables using a linear equation. Ensemble regression combines multiple models to improve prediction accuracy, often aggregating their predictions. Grid approximation, by contrast, does not necessarily rely on the assumptions of linearity and can provide insights into non-linear relationships.

**5. With which posterior do we expect to find most? The least?**  
We expect to find most of the samples within the out-boundary posterior, as it predicts a higher average pcs/m of 1.04 compared to the in-boundary posterior, which averages 0.97. Consequently, the out-boundary posterior captures a broader range of observations that likely reflect higher trash density than the in-boundary samples.

**6. If the in-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from within the boundary?**  
If the in-boundary grid approximation predicts an increase, it implies that elevated values were likely observed in other locations within the geographic boundary compared to the likelihood. This suggests that the trend observed is consistent across the samples taken from that area.

**7. If the out-boundary grid approximation predicts an increase or decrease, what does that say about the other samples from outside of the boundary?**  
If the out-boundary grid approximation predicts an increase, it indicates that locations outside the designated region likely had elevated values when compared to the likelihood. This suggests that the trash density may be higher on average in areas outside the boundary, influencing the posterior estimation.

**8. How different are the expected results from the observed results? Should an increase or decrease be expected?**  
The observed average pcs/m is 0.92. The in-boundary posterior average of 0.97 represents an increase of 0.05, while the out-boundary posterior average of 1.04 indicates an increase of 0.12 compared to the observed average. Given these differences, both the in-boundary and out-boundary results suggest that an increase is expected in future observations.
:::

## Consolidated results : city, canton, survey area


::::{grid}

:::{grid-item}


<div>

<style type="text/css">
#T_b4281 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_b4281 tr:nth-child(odd) {
  background: #FFF;
}
#T_b4281 tr {
  font-size: 12px;
}
#T_b4281 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_b4281 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_b4281 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b4281  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b4281  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b4281  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_b4281 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_b4281">
  <caption>Sample totals : city, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_b4281_level0_col0" class="col_heading level0 col0" >city</th>
      <th id="T_b4281_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_b4281_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_b4281_row0_col0" class="data row0 col0" >Biel/Bienne</td>
      <td id="T_b4281_row0_col1" class="data row0 col1" >1'001</td>
      <td id="T_b4281_row0_col2" class="data row0 col2" >1,79</td>
    </tr>
    <tr>
      <td id="T_b4281_row1_col0" class="data row1 col0" >Erlach</td>
      <td id="T_b4281_row1_col1" class="data row1 col1" >28</td>
      <td id="T_b4281_row1_col2" class="data row1 col2" >0,49</td>
    </tr>
    <tr>
      <td id="T_b4281_row2_col0" class="data row2 col0" >Gals</td>
      <td id="T_b4281_row2_col1" class="data row2 col1" >8</td>
      <td id="T_b4281_row2_col2" class="data row2 col2" >0,21</td>
    </tr>
    <tr>
      <td id="T_b4281_row3_col0" class="data row3 col0" >Le Landeron</td>
      <td id="T_b4281_row3_col1" class="data row3 col1" >14</td>
      <td id="T_b4281_row3_col2" class="data row3 col2" >0,38</td>
    </tr>
    <tr>
      <td id="T_b4281_row4_col0" class="data row4 col0" >Ligerz</td>
      <td id="T_b4281_row4_col1" class="data row4 col1" >24</td>
      <td id="T_b4281_row4_col2" class="data row4 col2" >1,54</td>
    </tr>
    <tr>
      <td id="T_b4281_row5_col0" class="data row5 col0" >Lüscherz</td>
      <td id="T_b4281_row5_col1" class="data row5 col1" >17</td>
      <td id="T_b4281_row5_col2" class="data row5 col2" >0,06</td>
    </tr>
    <tr>
      <td id="T_b4281_row6_col0" class="data row6 col0" >Nidau</td>
      <td id="T_b4281_row6_col1" class="data row6 col1" >15</td>
      <td id="T_b4281_row6_col2" class="data row6 col2" >0,60</td>
    </tr>
    <tr>
      <td id="T_b4281_row7_col0" class="data row7 col0" >Vinelz</td>
      <td id="T_b4281_row7_col1" class="data row7 col1" >59</td>
      <td id="T_b4281_row7_col2" class="data row7 col2" >0,33</td>
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
#T_58246 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_58246 tr:nth-child(odd) {
  background: #FFF;
}
#T_58246 tr {
  font-size: 12px;
}
#T_58246 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_58246 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_58246 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_58246  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_58246  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_58246  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_58246 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_58246">
  <caption>Sample totals : canton, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_58246_level0_col0" class="col_heading level0 col0" >canton</th>
      <th id="T_58246_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_58246_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_58246_row0_col0" class="data row0 col0" >Bern</td>
      <td id="T_58246_row0_col1" class="data row0 col1" >1'152</td>
      <td id="T_58246_row0_col2" class="data row0 col2" >0,94</td>
    </tr>
    <tr>
      <td id="T_58246_row1_col0" class="data row1 col0" >Neuchâtel</td>
      <td id="T_58246_row1_col1" class="data row1 col1" >14</td>
      <td id="T_58246_row1_col2" class="data row1 col2" >0,38</td>
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
#T_45e24 tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_45e24 tr:nth-child(odd) {
  background: #FFF;
}
#T_45e24 tr {
  font-size: 12px;
}
#T_45e24 th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_45e24 td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_45e24 table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_45e24  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_45e24  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_45e24  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_45e24 caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_45e24">
  <caption>Sample totals : parent_boundary, average, quantity, number of samples</caption>
  <thead>
    <tr>
      <th id="T_45e24_level0_col0" class="col_heading level0 col0" >parent_boundary</th>
      <th id="T_45e24_level0_col1" class="col_heading level0 col1" >quantity</th>
      <th id="T_45e24_level0_col2" class="col_heading level0 col2" >pcs/m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_45e24_row0_col0" class="data row0 col0" >aare</td>
      <td id="T_45e24_row0_col1" class="data row0 col1" >1'166</td>
      <td id="T_45e24_row0_col2" class="data row0 col2" >0,92</td>
    </tr>
  </tbody>
</table>


</div>


:::

::::

## Inventory

<div>
<style type="text/css">
#T_6ebfc tr:nth-child(even) {
  background-color: rgba(139, 69, 19, 0.08);
}
#T_6ebfc tr:nth-child(odd) {
  background: #FFF;
}
#T_6ebfc tr {
  font-size: 12px;
}
#T_6ebfc th {
  background-color: #FFF;
  font-size: 14px;
  text-align: left;
  width: auto;
  word-break: keep-all;
}
#T_6ebfc td {
  padding: 4px;
  font-size: 12px;
  text-align: center;
}
#T_6ebfc table {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_6ebfc  th {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_6ebfc  tr {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_6ebfc  td {
  border: 1px solid black;
  border-collapse: collapse;
}
#T_6ebfc caption {
  caption-side: top;
  font-size: 1em;
  text-align: left;
  margin-bottom: 10px;
}
</style>
<table id="T_6ebfc">
  <caption> </caption>
  <thead>
    <tr>
      <th id="T_6ebfc_level0_col0" class="col_heading level0 col0" >quantity</th>
      <th id="T_6ebfc_level0_col1" class="col_heading level0 col1" >pcs/m</th>
      <th id="T_6ebfc_level0_col2" class="col_heading level0 col2" >% of total</th>
      <th id="T_6ebfc_level0_col3" class="col_heading level0 col3" >sample_id</th>
      <th id="T_6ebfc_level0_col4" class="col_heading level0 col4" >fail rate</th>
      <th id="T_6ebfc_level0_col5" class="col_heading level0 col5" >object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_6ebfc_row0_col0" class="data row0 col0" >819</td>
      <td id="T_6ebfc_row0_col1" class="data row0 col1" >0,60</td>
      <td id="T_6ebfc_row0_col2" class="data row0 col2" >0,70</td>
      <td id="T_6ebfc_row0_col3" class="data row0 col3" >39</td>
      <td id="T_6ebfc_row0_col4" class="data row0 col4" >0,79</td>
      <td id="T_6ebfc_row0_col5" class="data row0 col5" >Cigarette filters</td>
    </tr>
    <tr>
      <td id="T_6ebfc_row1_col0" class="data row1 col0" >347</td>
      <td id="T_6ebfc_row1_col1" class="data row1 col1" >0,32</td>
      <td id="T_6ebfc_row1_col2" class="data row1 col2" >0,30</td>
      <td id="T_6ebfc_row1_col3" class="data row1 col3" >39</td>
      <td id="T_6ebfc_row1_col4" class="data row1 col4" >0,87</td>
      <td id="T_6ebfc_row1_col5" class="data row1 col5" >Food wrappers; candy, snacks</td>
    </tr>
  </tbody>
</table>


</div>
