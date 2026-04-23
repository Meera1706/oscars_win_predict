import streamlit as st
import pandas as pd

st.title("Model Comparison")

data = {
    "Model": ["Logistic", "Random Forest", "XGBoost", "Balanced Logistic"],
    "Precision": [0.97, 0.57, 1.00, 0.39],
    "Recall": [0.15, 0.15, 0.15, 0.27],
    "F1 Score": [0.27, 0.24, 0.26, 0.32]
}

df = pd.DataFrame(data)

st.dataframe(df)
st.bar_chart(df.set_index("Model")["F1 Score"])