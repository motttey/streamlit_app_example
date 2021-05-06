import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

def map(lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50
        },
        layers=[]
    ))

row1, row2 = st.beta_columns((2,3))

with row1:
    st.title("MapBox Example")
    st.write(
    """
    ### Fujisawa!
    """
    )
    lat = st.slider(
        label="latitude",
        min_value=35.0,
        max_value=36.0,
        step=0.01,
        value=35.25
    )
    lon = st.slider(
        label="latitude",
        min_value=139.0,
        max_value=140.0,
        step=0.01,
        value=139.48
    )

with row2:
    map(lat, lon, 11)
