import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


"""""""""
@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data(path = "./data/ev_communes.csv")

st.title("Predicting-demand-for-charging-stations-in-Switzerland")
st.header("Number of new charging stations")

if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=df)


df["delta"] = df.recomm_2022 - df.Count
df2 = df.dropna()
df2 = df[df['delta'] >= 0]

with open("./data/gemeinden-geojson.geojson", encoding='utf-8') as response:
    munis = json.load(response)

for f in munis['features']:
    f['properties']['gemeinde_NAME'] = f['properties']['gemeinde.NAME']
    del f['properties']['gemeinde.NAME']

fig = px.choropleth_mapbox(
    df2,
    color="delta",
    geojson=munis,
    locations="City",
    featureidkey="properties.gemeinde_NAME",
    center={"lat": 46.8, "lon": 8.3},
    mapbox_style="open-street-map",
    zoom=6.3,
    opacity=0.8,
    width=900,
    height=500,
    labels={"City": "Municipality",
           "delta":"Number of new charging stations"},
    title="<b> New charging stations required per municipality</b>",
    color_continuous_scale="Viridis",
)
fig.update_layout(margin={"r":0,"t":35,"l":0,"b":0},
                  font={"family":"Sans",
                       "color":"black"},
                  hoverlabel={"bgcolor":"white",
                              "font_size":12,
                             "font_family":"Sans"},
                  title={"font_size":20,
                        "xanchor":"left", "x":0.01,
                        "yanchor":"bottom", "y":0.95}
                 )
"""

#we read the csv
df_cs = pd.read_csv("./data/ev_communes_final.csv", index_col = 1)
df_cs = df_cs.dropna()

#we create the first chart. Its a bubble chart with all the cities and recommendations for 2024 in the bububle size
fig1 = go.Figure(data=[
    go.Scatter(
        x=df_cs['2021'], y=df_cs['Count'],
        mode="markers",
        marker={"size": df_cs['recomm_2024'], "sizemode": "area", "sizeref": 2*max(df_cs["recomm_2024"])/1000},
        text=df_cs.index,
        hovertemplate=
            "<b>%{text}</b><br><br>" +
            "Recomended Charging Stations in 2024: %{marker.size:,}" +
            "<extra></extra>"
        )
])
#this the layout of fig 1
fig1.update_layout(
    title={"text": "Charging Stations Recommendations", "font": {"size": 20}},
    xaxis={"title": {"text": "EV Cars per City", "font": {"size": 12}}},
    yaxis={"title": {"text": "Charging Stations per City", "font": {"size": 12}}},
    paper_bgcolor='rgb(255,255, 255)',
    plot_bgcolor='rgb(254, 246, 224)',
)
#fig1.update_yaxes(type="log")

st.plotly_chart(fig1)

#1st data frame. It's take the first years and then transpose
df_cs_trans = df_cs[["2017", "2018", "2019", "2020", "2021"]]
df_cs_trans = df_cs_trans.transpose()
df_cs_trans.reset_index()
#2nd data frame. Take the predictiosn for EV cars and transpose it
df_cs_trans_2 = df_cs[["2021","2022_pred","2023_pred","2024_pred"]]
df_cs_trans_2 = df_cs_trans_2.transpose()
df_cs_trans_2.reset_index()

#3rd Data Frame. This one whas the recomendations for charging stations
df_cs_trans_3 = df_cs[["Count","recomm_2022","recomm_2023","recomm_2024"]]
df_cs_trans_3 = df_cs_trans_3.transpose()
df_cs_trans_3.reset_index()

#4rd data frame with all the yeas
df_cs_trans_4 = df_cs[["2017", "2018", "2019", "2020", "2021","2021","2022_pred","2023_pred","2024_pred"]]
df_cs_trans_4 = df_cs_trans_4.transpose()
df_cs_trans_4.reset_index()



# Widgets:Select Box
cities_list = ["All"]
for cities in df_cs_trans:
    cities_list.append(cities)

st.header("Header")

cities_list = ["All"]
for cities in df_cs_trans:
    cities_list.append(cities)


city_box = st.selectbox("Choose a Citi", cities_list)

#this is the plot for the first chart

fig2, ax = plt.subplots(figsize=(8, 4))
#this is a loop for all the cities

for cities in df_cs_trans:
    ax.plot(df_cs_trans.index ,df_cs_trans[cities], alpha = 0.2)
    ax.plot(df_cs_trans_2.index ,df_cs_trans_2[cities], alpha = 0.2)
    if cities == city_box:
        ax.plot(df_cs_trans_4.index, df_cs_trans_4[cities], alpha=1)
        ax.annotate(city_box, (max(df_cs_trans_2.index), max(df_cs_trans_2[cities])))

ax.set_xlabel("year + prediction", loc="right")
ax.set_ylabel("Cars per city + Cars per city E")


st.pyplot(fig2)

input_double_chart = city_box
fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))     #, sharex=True, sharey=True)

ax1.plot(df_cs_trans_4.index ,df_cs_trans_4[input_double_chart], alpha = 1)
ax2.plot(df_cs_trans_3.index ,df_cs_trans_3[input_double_chart], alpha = 1)


st.pyplot(fig3)