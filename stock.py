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

sp500_list = load_data()

st.title('S&P 500')

st.dataframe(sp500_list)
stacked_df = sp500_list.stack().reset_index()
stacked_df = stacked_df.rename(columns={
    'level_1': 'ticker',
    0: 'Close'
})

lineplot(stacked_df)
