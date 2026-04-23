import streamlit as st

st.set_page_config(
    page_title="Oscars Prediction System",
    layout="wide"
)

st.title("🎬 Oscars Prediction System")

st.markdown("""
This app predicts whether a nomination will win an Oscar.

### Features:
- EDA
- Model Comparison
- Prediction
- Explainability

Use sidebar to navigate.
""")