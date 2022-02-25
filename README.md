# Evolution of EV charging stations in Switzerland


!(./src/newplot.png)


#### -- Project Status: [Active, On-Hold, Completed]

## Project Intro/Objective
The purpose of this project is to evaluate the future demand for charging stations in municipalities in Switzerland based in charging infrastructure that is currently available and the growth rate of electric vehicles. 

Assumptions: 
- current charging infrastructure is sufficient for current vehicle stock, 
- predictions are based on the electric vehicle stock growth rate from 2017 to 2021, for years 2022-23-24.

""""""nice to have: 
- build a prediction model for historical data for car sales using time series
- add green energy sources
- narrow down prediction from municipality to location within municipality (based in distance between the stations, etc.)
- visualisation: car sales per municipality, charging stations per municipality, prediction for new charging stations

Results:
- Our OLS model calculated a general EV growth rate of 1.624 for 2022. 
 
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

Data sources:
- charging stations available in Switzerland https://opendata.swiss/fr/dataset/ladestationen-fuer-elektroautos
- current stock of electric cars in Switzerland https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1103020100_111/px-x-1103020100_111/px-x-1103020100_111.px/
- Swiss municipalities https://datahub.io/cividi/ch-municipalities

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the group)*

3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages)
create another "setup.md" file and link to it here*

5. Follow setup [instructions](Link to file)

#
4. Conclusions
   - Live Visualization of results
6. Suggestions for further improvements
   - Having a regresion model would be better. With more explanatory value
   - Where to put the new CS, not just by city buy also by where in the city
   - Make the prediction to take into account total car popultion in order to avoid wrong recomendations (Rsisch Case)
   - We could have combined the information for the charging stations per city with the information from the clean energy matrix for each canton so we don’t only      know where to place the new CS but also if they are getting their energy flor clean power plants/sources

## Contributing Members

 - Jeremy Choppe (https://github.com/jeremychoppe)
 - Franco Palito (https://github.com/fpallitto)
 - Satanei Zhinova (https://github.com/SetenayZ)

