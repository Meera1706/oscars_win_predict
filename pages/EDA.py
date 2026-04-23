import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EDA")

df = pd.read_csv("data/dataset.csv")

st.write("Dataset Preview")
st.dataframe(df.head())

st.write("Class Distribution")

fig, ax = plt.subplots()
df['winner'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)