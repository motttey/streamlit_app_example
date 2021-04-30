import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets

st.title('Dashboard')

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

df = load_data()
targets = list(df.target.unique())
selected_targets = st.multiselect('select targets', targets, default=targets)
df = df[df.target.isin(selected_targets)]

st.dataframe(df)

fig, ax = plt.subplots()
sns.boxplot(x='sepal width (cm)', y='target', data=df, whis=[0,100], width=.5, palette="vlag", ax=ax)
st.pyplot(fig)

# st.table(df)

# vega-lite
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})
