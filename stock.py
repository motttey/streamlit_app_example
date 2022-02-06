import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets

import yfinance as yf
import random

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

@st.cache
def load_data():
    sp500_list = pd.read_html(url)[0].Symbol.values.tolist()
    data = yf.download(random.sample(sp500_list, 10), '2022-01-01','2022-02-01')
    return data['Close']

def lineplot(df):
    fig = plt.figure(figsize=(10,4))
    sns.lineplot(data=df, x='Date', y='Close', hue='ticker')
    st.pyplot(fig)

# https://seaborn.pydata.org/examples/timeseries_facets.html
def smallMultiples(df):
    g = sns.relplot(
        data=df,
        x="Date", y="Close", col="ticker", hue="ticker",
        kind="line", palette="crest", linewidth=2.5, zorder=5,
        col_wrap=2, height=2, aspect=1.5, legend=False,
    )

    g.tight_layout()
    for year, ax in g.axes_dict.items():

        # Add the title as an annotation within the plot
        ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")

        # Plot every year's time series in the background
        sns.lineplot(
            data=df, x="Date", y="Close", units="ticker",
            estimator=None, color=".7", linewidth=1, ax=ax,
        )

    # Reduce the frequency of the x axis ticks
    ax.set_xticks(ax.get_xticks()[::4])

    st.pyplot(g)

sp500_list = load_data()

st.title('S&P 500')

st.dataframe(sp500_list)
stacked_df = sp500_list.stack().reset_index()
stacked_df = stacked_df.rename(columns={
    'level_1': 'ticker',
    0: 'Close'
})

lineplot(stacked_df)

smallMultiples(stacked_df)
