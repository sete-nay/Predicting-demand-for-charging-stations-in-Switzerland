# Evolution of EV charging stations in Switzerland


!(./src/newplot.png)


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

Assumptions: current charging infrastructure is sufficient for current vehicle stock.

### 2. Data sources:
- Geographical data of the 2'215 EV charging stations currently available in Switzerland as of January 2022 https://opendata.swiss/fr/dataset/ladestationen-fuer-elektroautos
- Total EV registered in each 2'163 Swiss municipalities, yearly data from 2017 to 2021 https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1103020100_111/px-x-1103020100_111/px-x-1103020100_111.px/
- JSon data of Swiss municipalities https://datahub.io/cividi/ch-municipalities 

### 4. Conclusions
   - Live Visualization of results
   - Our model predicted that more than 1'000 additional EV will be operational in 2022, compared to 2'215 today. 
### 5. Suggestions for further improvements
   - Having a regresion model would be better. With more explanatory value
   - Where to put the new CS, not just by city buy also by where in the city
   - Make the prediction to take into account total car popultion in order to avoid wrong recomendations (Risch Case)
   - We could have combined the information for the charging stations per city with the information from the clean energy matrix for each canton so we don’t only know where to place the new CS but also if they are getting their energy flor clean power plants/sources

## Contributing Members

 - Jeremy Choppe (https://github.com/jeremychoppe)
 - Franco Palito (https://github.com/fpallitto)
 - Satanei Zhinova (https://github.com/SetenayZ)

