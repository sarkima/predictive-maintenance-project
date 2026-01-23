import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.title("Engine Level RUL Explorer")

    df = pd.read_csv("data/rul_predictions_fd001.csv")

    # --- Engine selection ---
    engine_ids = sorted(df["engine_id"].unique())
    selected_engine = st.selectbox("Select Engine ID", engine_ids)

    engine_data = df[df["engine_id"] == selected_engine].copy()

    # --- Interactive sliders ---
    st.subheader("Interactive Controls")

    threshold = st.slider(
        "Maintenance threshold (cycles)",
        min_value=5,
        max_value=50,
        value=20,
        step=1
    )

    smoothing = st.slider(
        "Prediction smoothing window (moving average)",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    # Apply smoothing
    engine_data["pred_rul_smooth"] = (
        engine_data["pred_rul"].rolling(window=smoothing, min_periods=1).mean()
    )

    # --- Plotly charts ---
    st.markdown("### True RUL Over Time")
    fig_true = px.line(
        engine_data,
        x="cycle",
        y="true_rul",
        title="True RUL",
        markers=True
    )
    st.plotly_chart(fig_true, use_container_width=True)

    st.markdown("### Predicted RUL (Smoothed)")
    fig_pred = px.line(
        engine_data,
        x="cycle",
        y="pred_rul_smooth",
        title="Predicted RUL (Smoothed)",
        markers=True
    )
    st.plotly_chart(fig_pred, use_container_width=True)

    # --- Maintenance threshold indicator ---
    st.markdown("### Maintenance Trigger Points")
    trigger_points = engine_data[engine_data["pred_rul_smooth"] < threshold]

    if trigger_points.empty:
        st.success("No maintenance trigger detected for this engine.")
    else:
        st.warning(
            f"Maintenance recommended at cycle {trigger_points['cycle'].iloc[0]} "
            f"(predicted RUL < {threshold} cycles)."
        )

    # --- Download button ---
    st.subheader("Download Engine Predictions")

    csv_data = engine_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download predictions as CSV",
        data=csv_data,
        file_name=f"engine_{selected_engine}_predictions.csv",
        mime="text/csv"
    )

    # --- Interpretation guide ---
    st.markdown("### Interpretation Guide")

    st.markdown("""
    - **True RUL Chart:** shows the actual remaining useful life of the engine over cycles  
    - **Predicted RUL Chart:** shows the model's prediction of remaining useful life over cycles  
        - This helps assess how reliable the model is for maintenance decisions.
    - **Maintenance Threshold:** indicates when maintenance should be scheduled based on the selected threshold  
    """)
                
                
