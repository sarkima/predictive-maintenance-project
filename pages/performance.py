import streamlit as st
import pandas as pd

def run():
    st.title("Model Performance")

    st.markdown("### Model Comparison")
    df = pd.read_csv("data/model_metrics.csv")

    st.dataframe(df)

    st.markdown("### RMSE Comparison")
    st.bar_chart(df.set_index("Model")["RMSE"])