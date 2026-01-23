## **Predicting Remaining Useful Life (RUL) of a Turbofan Engine Using Machine Learning**

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Overview

Modern industrial environments rely heavily on high value machinery such as engines, turbines, compressors, and pumps. However, unexpected failures lead to costly downtime, safety risks, and inefficient maintenance cycles. Traditional maintenance strategies (reactive or scheduled) fail to account for real time machine health.

This project uses the NASA CMAPSS Turbo Fan Engine Degradation dataset to build a predictive maintenance model capable of estimating the Remaining Useful Life (RUL) of engines based on sensor data collected over time.

The goal is to demonstrate how data analytics and machine learning can transform maintenance from reactive or scheduled to predictive — improving reliability, reducing costs, and supporting smarter industrial operations.

## Dataset Description

- **Dataset**:
  - NASA CMAPSS (Commercial Modular Aero Propulsion System Simulation) Turbo Fan Jet Engines
  - It was sourced from [Kaggle](https://www.kaggle.com/datasets/behrad3d/nasa-cmaps/data) version of the public dataset for asset degradation modelling.
  - It includes Run-to-Failure simulated data from 4 Turbo Fan Jet engines (FD001, FD002, FD003 and FD004) with different operating conditions and fault modes.
  - Each dataset is divided into train and test subsets.
  - The datasets can be considered to be from a fleet of engines of the same type.
  - The data is contaminated with sensor noise.
  - It also include a vector of true Remaining Useful Life (RUL) values for the test data.
  - Due to time constraints only FD001 dataset will be used for this project.
- **Type**: Multivariate time series
- **Contents**:
  - Sensor readings (21+ channels)
  - Operating conditions (3)
  - Engine cycles
  - Failure labels (implicit via RUL)
- **Why this dataset**:
  - Realistic simulation of engine degradation
  - Rich time series structure
  - Ideal for predictive modelling
  - Widely used in industry and research
  - Perfect match for engineering + AI applications

## Business Problem

Industrial engines degrade over time, but the rate of degradation varies depending on load, environment, and operating conditions. Maintenance teams often lack the ability to predict when a component will fail.

Key business questions:

- How long before an engine reaches failure?
- Which sensors provide the strongest early indicators of degradation?
- Can we recommend optimal maintenance intervals?
- What cost savings could predictive maintenance deliver?

## Project Objectives

**Primary Objective**:

- Build a machine learning model that predicts the Remaining Useful Life (RUL) of turbo fan engines.

**Secondary Objectives**:

- Perform descriptive analytics to understand sensor behaviour
- Identify key drivers of engine degradation
- Compare multiple predictive models
- Communicate insights through visualisations and a business focused narrative

## Hypotheses Testing

The following hypotheses will be explored either through visualisation or testing:

- Operational settings have substantial effects on engine performance
- Some sensors are far greater indicator of failures than others
- There is correlation between RUL and some operating conditions/sensors/engines
- Gradient Boosting Regressor performs better than Random Forest Regressor
- Predictive maintenance delivers cost savings over scheduled maintenance

## Methodology

The methodology used for this project involved conducting the following types of data analytics.  The beauty of the NASA CMAPSS dataset is that it allow us to conduct the full categories of data analytics - descriptive, diagnostic, predictive, prescriptive and cognitive.  However, for this project we will limit it to descriptive, diagnostic and predictive.

- A. Descriptive Analytics
  -	Explore sensor trends over engine cycles
  - Visualise degradation patterns
  - Identify anomalies and outliers
  - Compare operating conditions

- B. Diagnostic Analytics
  - Correlation analysis
  -	Feature importance
  -	Healthy vs degrading engine behaviour
  -	Sensor drift analysis

- C. Predictive Analytics
  - Models to consider:
  -	Random Forest Regressor
  -	Gradient Boosting (XGBoost / LightGBM)
  -	LSTM or GRU neural networks

## Tools & Technologies

The following libraries, tools and technologies were used in the project:

- Python (Pandas, NumPy, Matplotlib, Plotly, Seaborn)
- Scikit learn
- Jupyter Notebook
- Streamlit for dashboard

## Expected Deliverables

- Cleaned and processed dataset
- Exploratory data analysis
- Predictive model with performance metrics
- Visual dashboard showing engine health and RUL
- Key findings and recommendations

## Dashboard Development

A dashboard web application was developed using Streamlit providing overview, engine explorer, sensor diagnostics, model performance, insights and recommendations .  It allows both technical and non-technical users to gain an insight into the dataset, receive some recommendations and perform some predictive maintenance analytics.  The dashboard can be access the following  [link](https://predictive-maintenance-project-ge9iv5ikdy5uj9jnaejzwb.streamlit.app/)

## Key Insights and Recommendations

Many of the key insights and recommendations of this project have been covered in many locations in the Jupyter Notebook and the Streamlit Dashboard App.

The project set out to answer some business questions and test some hypotheses.  While time did not allow the conduct of statistical hypothesis testing, many of the data visualisations ploted and the predictive models built have answered many of these questions and hypotheses.

- How long before an engine reaches failure can easily be answered by visualising its Remaining Useful Life (RUL)
- Which sensors provide the strongest early indicators of degradation can be answered by checking the visualisation of the correlation heatmaps of sensors to RUL
- Optimal maintenance intervals can be recommended by observing the engine degradation overtime and knowing its RUL
- Cost savings offered by predictive maintenance over scheduled or reactive maintenance can readily be estimated
- It was noticed that operational settings have limited if any effects on engine performance
- Feature performance and its visualisation show that some sensors are far greater indicator of failures than others - in fact a few othem - 3 or 4
- There is correlation between RUL and some sensors but less so of operating conditions or engine types
- There was very little difference between Gradient Boosting Regressor and Random Forest Regressor on any of their two scores (RMSE and MAE)
- Predictive maintenance can deliver susbstantial cost savings over reactive or scheduled maintenance

## Future Work

Time limitations did not allow one to conduct many of the tasks planned for this project.  One would have conducted a more detailed descriptive analytics or diagnostic analysics.  Some of the more advanced and interesting machine learning models, such as XGBoost or Artificial Neural Networks, could have experimented upon.  Estimating downtime reduction or recommending maintenance with prescriptive analytics could be conducted.  Also in consideration is cognitive analytics, with the prospect of showing how predictions in real-time could be possible though a digital twin.

Furthermore, only subset of the four subsets of the dataset was used in this project. Using the four subsets offer the prospect of analysing a fleet of engines.

The design of the dashboard was small and simple but could be developed further in details and made as the go to app for insights, recommendations and predictive modelling of engines.

## Ethical Considerations

The dataset used for the project are sensors, engines and operating conditions data.  The dataset was provided by NASA CMAPSS and is open and available through many organisations.  The one used for the project was sourced a Kaggle.  Since it is open and no personal data involved there is no ethical consideration in the collection, processing and storage of the dataset.

## Project Planning, Management and Documentation

The project planning and management was conducted via [GitHub Project](https://github.com/users/sarkima/projects/2/views/1). The project was broken down into items using a Kaban flow system with items moving from backlog through ready, in progress to done. The time taken to complete each item can be tracked and the number of commits made during each item can be noted. The flow of items through the system can be tracked and actions can be taken to deal with bottlenecks or items taking too long to complete than planned noted and addressed.

The project is fully documented in the README.md file, the Jupyter Notebook, and the Streamlit Dashboard Web App.  The project's repository is located [here](https://github.com/sarkima/predictive-maintenance-project).

## Conclusion

The project provided me with the opportunity to explore real-world datasets and apply some of the knowledge and expertise gained with the Code Institute to solve challenging industrial problems with predictive analytics.

This project has sourced, processed and analysed NASA CMPASS engines dataset to industrial problems using data analytics and machine learning for engines predictive maintenance.  Data visualisations, predictive models, and a Streamlit Dashboard app were produced to provide helpful insights, recommendations and interactive tools for exploration and better understanding.  A number of business questions were answered and many interesting hypotheses were tested.

## Reflections

The project was very interesting and I enjoyed doing it as it has the project of covering the full spectrum of data analytics - from descriptive through diagnostic, predictive, prescriptive and all the way down to cognitive analytics.  However, many difficulties were encountered through out the project.  Not enough time, computing slowing down to a frustrating snail speed with all the loadded libraries and tools, not getting the project template to work the Python 3.13.9 that was loaded on my computer, and not getting enough sleep.  Hopefully, the learning outcome will be rewarding.

## AI Tools

The following AI tools were used in the project:

- Microsoft Copilot was used to search for a suitable dataset for the project.  It was also used to generate a suitable structure and business requirements for the project. Some code snipets were also generated for some parts of the project.  It was also used to help developed a modular, structured and concised Streamlit Dashboard App.
- GitHub Copilot was used for code snipets suggestion using prompting, dealing with errors, requesting help with problems encountered, and for optimising some of the code.

## Credits

I would like to credit the following:

- NASA CMPASS and Kaggle for providing the dataset that was used for the project.
- Code Institute course materials that we used in the project.
- AI tools that helped in searching for this dataset, guided in the planning of the project, and aided in the execution of the project with helpful computing prompts.

## Acknowledgement

I acknowledge the support and help provided by the staff of the Code Institute during the execusion of this project.
