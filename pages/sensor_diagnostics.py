import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run():
    st.title("Sensor Level Diagnostics")

    df = pd.read_csv("data/rul_predictions_fd001.csv")

    # --- Sensor selection ---
    sensor_cols = [col for col in df.columns if "sensor" in col]
    selected_sensor = st.selectbox("Select Sensor", sensor_cols)

    # --- Engine selection ---
    engine_ids = sorted(df["engine_id"].unique())
    selected_engine = st.selectbox("Select Engine ID", engine_ids)

    engine_data = df[df["engine_id"] == selected_engine].copy()

    # --- Smoothing slider ---
    smoothing = st.slider(
        "Smoothing window (moving average)",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    engine_data["smooth"] = (
        engine_data[selected_sensor].rolling(window=smoothing, min_periods=1).mean()
    )

    # --- Plotly sensor chart ---
    st.markdown(f"### {selected_sensor} Over Time (Interactive)")
    fig_sensor = px.line(
        engine_data,
        x="cycle",
        y="smooth",
        title=f"{selected_sensor} (Smoothed)",
        markers=True
    )
    st.plotly_chart(fig_sensor, use_container_width=True)

    # --- Summary statistics ---
    st.markdown("### Summary Statistics")
    st.write(engine_data[selected_sensor].describe())

    # --- Correlation heatmap ---
    st.markdown("### Sensor Correlation Heatmap")

    corr = df[sensor_cols].corr()

    fig_heatmap = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Sensor Correlation Matrix"
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)

    # --- Interpretation guide ---
    st.markdown("### Interpretation Guide")
    st.write("""
    - **Strong positive correlation (red):** sensors rise together  
    - **Strong negative correlation (blue):** one rises as the other falls  
    - **Near zero correlation:** sensors behave independently  
    - Use this to identify redundant sensors or strong predictors

    - **Upward trend:** sensor value increases as engine degrades  
    - **Downward trend:** sensor value decreases as engine degrades  
    - **High variance:** sensor may be noisy or influenced by operating conditions  
    - **Flat line:** sensor may not be useful for RUL prediction
    """)