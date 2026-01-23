import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

import pages.overview as overview
import pages.performance as performance
import pages.explorer as explorer
import pages.insights as insights
import pages.sensor_diagnostics as sensor_diagnostics

# --- Page title ---
st.set_page_config(page_title="Turbo Fan RUL Dashboard", layout="wide")


# --- Theme toggle ---
if "theme" not in st.session_state:
    st.session_state.theme = "light"

theme_choice = st.sidebar.radio("Theme", ["light", "dark"])
st.session_state.theme = theme_choice

# --- Apply theme CSS ---
if st.session_state.theme == "dark":
    st.markdown(
        """
        <style>
        body { background-color: #0E1117; color: #FAFAFA; }
        .stApp { background-color: #0E1117; }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body { background-color: #FFFFFF; color: #000000; }
        .stApp { background-color: #FFFFFF; }
        </style>
        """,
        unsafe_allow_html=True
    )


# --- Sidebar navigation ---

menu = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Model Performance",
        "Engine Explorer",
        "Sensor Diagnostics",
        "Insights & Recommendations"
    ]
)

if menu == "Overview":
    overview.run()
elif menu == "Model Performance":
    performance.run()
elif menu == "Engine Explorer":
    explorer.run()
elif menu == "Sensor Diagnostics":
    sensor_diagnostics.run()
elif menu == "Insights & Recommendations":
    insights.run()