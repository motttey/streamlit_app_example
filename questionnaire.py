import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("event_211145_participants.csv", encoding="cp932")
print(df.head())
print(df.columns)

fig, ax = plt.subplots()
sns.countplot(x='データ可視化に関する業務/研究の経験', data=df, ax=ax)
st.pyplot(fig)

sns.countplot(x='現在最も該当すると考えるポジションを選択してください', data=df, ax=ax)
st.pyplot(fig)
