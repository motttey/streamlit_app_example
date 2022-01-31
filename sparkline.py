import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets

import base64
import requests
from time import sleep
from itertools import chain
from io import BytesIO
from datetime import timedelta, date

url='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv'
# https://github.com/iiSeymour/sparkline-nb/blob/master/sparkline-nb.ipynb
def sparkline(data, figsize=(4, 0.5), **kwags):
    """
    Returns a HTML image tag containing a base64 encoded sparkline style plot
    """
    data = list(data)

    fig, ax = plt.subplots(1, 1, figsize=figsize, **kwags)
    ax.plot(data)
    for k,v in ax.spines.items():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.plot(len(data) - 1, data[len(data) - 1], 'r.')

    ax.fill_between(range(len(data)), data, len(data)*[min(data)], alpha=0.1)

    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    plt.close()
    return '<img src="data:image/png;base64,{}"/>'.format(base64.b64encode(img.read()).decode())

st.title('Covid 19 Dashboard')

st.markdown('''
Data source: [owid/covid-19-data]({})
'''.format(url))

df = pd.read_csv(url, sep=",")
df = df[df['indicator'] == 'Daily hospital occupancy']

sort = st.radio("Sort ASC/DESC", (True, False))
key = st.selectbox(
     'Sort Keys',
     ('value_max', 'value_min', 'value_sum')
)

df_grouped = df.groupby(['entity', 'indicator'])['value'].apply(list).reset_index()

df_grouped['value_max'] = [max(x) for x in df_grouped['value']]
df_grouped['value_min'] = [min(x) for x in df_grouped['value']]
df_grouped['value_sum'] = [sum(x) for x in df_grouped['value']]

# st.dataframe(df_grouped)

df_grouped['sparklines'] = df_grouped['value'].map(sparkline)
df_grouped.sort_values(key, ascending=sort, inplace=True)

st.write(df_grouped[['entity', 'sparklines']].to_html(escape=False), unsafe_allow_html=True)
