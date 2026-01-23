import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.title("Insights & Recommendations")

    # --- Load feature importance ---
    fi = pd.read_csv("data/feature_importance_fd001.csv")

    st.markdown("### Feature Importance (Gradient Boosting)")
    fig = px.bar(
        fi,
        x="importance",
        y="feature",
        orientation="h",
        title="Feature Importance",
        height=600
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Interpretation:**  
    - Features at the top contribute most to predicting RUL  
    - Low importance sensors may be redundant  
    - High importance sensors are strong candidates for monitoring  
    """)

    # --- Interactive maintenance threshold ---
    st.markdown("### Maintenance Threshold Recommendation")

    threshold = st.slider(
        "Select maintenance threshold (cycles)",
        min_value=5,
        max_value=50,
        value=20,
        step=1
    )

    st.info(
        f"Recommended action: schedule maintenance when predicted RUL "
        f"falls below **{threshold} cycles**."
    )

    # --- Additional insights ---
    st.markdown("### Key Insights")
    st.write("""
    - Gradient Boosting identifies the most predictive sensors for engine degradation  
    - These sensors should be prioritised in monitoring systems  
    - Maintenance decisions can be tied directly to predicted RUL thresholds  
             
    - Regularly review model performance and recalibrate thresholds as needed  
    - Consider integrating real-time sensor data for dynamic RUL predictions

    - Sensor X and Y show strong degradation patterns.
    - Improved model reduces RMSE by Z%.
    - Prediction accuracy is strongest in the early mid life of engines.                 

    ### Key Insights
    - Sensor X and Y show strong degradation patterns.
    - Improved model reduces RMSE by Z% compared to baseline.
    - Prediction accuracy is strongest in the early mid life of engines.

    ### Recommendations
    - Schedule maintenance when predicted RUL < **N cycles**.
    - Monitor sensors X and Y closely for early warning signs.
    - Integrate the model into a real time monitoring system for continuous updates.

    ### Next Steps
    - Expand to all CMAPSS subsets.
    - Add LSTM/GRU models for deeper time series learning.
    - Build a digital twin concept for real time simulation.

    """)

    st.markdown("### Next Steps")
    st.write("""
    - Expand to all NASA CMAPSS subsets  
    - Add LSTM/GRU models for deeper time series learning  
    - Build a digital twin simulation page  
    """)