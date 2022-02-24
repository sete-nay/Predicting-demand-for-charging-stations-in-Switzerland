import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy



@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data(path = "./data/ev_communes.csv")

st.title("Predicting demand for charging stations in Switzerland")
st.header("Number of new charging stations")

st.subheader("New charging stations per municipalities")

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

st.plotly_chart(fig)


