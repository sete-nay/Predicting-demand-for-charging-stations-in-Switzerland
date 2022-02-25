# Evolution of EV charging stations in Switzerland

#### -- Project Status: [Active, On-Hold, Completed]

## Project Intro/Objective
The purpose of this project is to evaluate the future demand for charging stations in municipalities in Switzerland based in charging infrastructure that is currently available and the growth rate of electric vehicles. 

""nice to have: 
- build a prediction model for historical data for car sales using time series
- add green energy sources
- narrow down prediction from municipality to location within municipality (based in distance between the stations, etc.)
- visualisation: car sales per municipality, charging stations per municipality, prediction for new charging stations
 
### Partner
* [Name of Partner organization/Government department etc..]
* Website for partner
* Partner contact: [Name of Contact]
* If you do not have a partner leave this section out

### Methods Used
* Data Visualization
* Predictive Modeling

### Data Science tools
* Python
* Pandas, jupyter
* Plotly 
* Streamlit 

## Project Description
### 1. Introduction:
We realized how geographical data could be useful to solve sustainability related issues, as it can be a meaningful way to show the environmental impact of a specific market and inform public decision makers for future policies.

After having previously analyzed in our course, the situation of clean energy sources in Switzerland, we thought about using the same approach in order to optimize the use of electric vehicles in Switzerland and adapt the offer of charging stations.

We therefore tried to predict the future demand for charging stations per municipalities, based on the yearly sales of electric vehicles and the geographic charging points infrastructure that is currently available.

### 2. Data sources:
- Detailed geographical data of the 2'215 EV charging stations currently available in Switzerland as of January 2022, json format https://opendata.swiss/fr/dataset/ladestationen-fuer-elektroautos
- Total EV registered in each of the 2'163 Swiss municipalities, yearly data from 2017 to 2021, excel file https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1103020100_111/px-x-1103020100_111/px-x-1103020100_111.px/
- Geographic data of all Swiss municipalities borders, json format https://datahub.io/cividi/ch-municipalities 

### 3. Methods and data transformation
- Current stock of electric cars in Switzerland is used to collect ther data about infrastructure that is currently available. This file was cleaned and normalized. The dataframe is grouped by cities, which gives a number of available charging stations.
- Charging stations available in Switzerland as of Februrary 2022 is used to estimate the demand for new charging stations. We took the data from 2017 to 2021, calculated the mean growth rate and applied it to predict future demand for charging stations. Here we assume that the current infrastructure is sufficient for the current demand. 
- These 2 dataframes were merge to calculate the gap between future stock of electric vehicles and future demand for charging stations.

### 4. Conclusions
   - Live Visualization of results
   - Our model predicted that 20'646 additional EV will be operational by the end of 2022, compared to 42'951 today. Under the assumption that the current charging infrastructure is sufficient for the actuel EV stock, this means that 1'065 charging points should be installed through the country to meet the demand in 2022.

### 5. Suggestions for further improvements
   - Defining a meaningful OLS regression model, including more variables explaining influences on EV sales. Using time series predicitions to better understand yearly patterns.
   - Where to strategically add new charging stations, not just by city buy also by where in the city, using computed distances between charging points.
   - Make the prediction to take into account total car popultion in order to avoid wrong recomendations (Risch Case)
   - We could have combined the information for the charging stations per city with the information from the clean energy matrix for each canton so we don’t only know where to place the new CS but also if they are getting their energy flor clean power plants/sources

## Contributing Members

 - Jeremy Choppe (https://github.com/jeremychoppe)
 - Franco Palito (https://github.com/fpallitto)
 - Satanei Zhinova (https://github.com/SetenayZ)

