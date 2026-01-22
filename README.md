# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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
- Can we recommend optimal maintenance intervals? (**remove**)
- What cost savings could predictive maintenance deliver? (**remove**)

## Project Objectives

**Primary Objective**:

- Build a machine learning model that predicts the Remaining Useful Life (RUL) of turbo fan engines.

**Secondary Objectives**:

- Perform descriptive analytics to understand sensor behaviour
- Identify key drivers of engine degradation
- Compare multiple predictive models
- Build a prescriptive maintenance recommendation (**remove**)
- Communicate insights through visualisations and a business focused narrative

## Hypotheses Testing

The following hypotheses will be explored either through visualisation or testing:

- Operational settings have substantial effect on engine performance
- Some operating conditions are far greater indicator of failures than others
- There is correlation between RUL and some operating conditions/sensors/engines
- Gradient Boosting (XGBoost / LightGBM) performs better than Random Forest Regressor
- Predictive maintenance delivers cost savings over scheduled maintenance

## Methodology

The methodology used for this project involved conducting the following types of data analytics.  The beauty of the NASA CMAPSS datasets is that it allow us to conduct the full categories of data analytics - descriptive, diagnostic, predictive, prescriptive and cognitive.  However, for this project we will limit it to descriptive, diagnostic and predictive.

A. Descriptive Analytics
•	Explore sensor trends over engine cycles
•	Visualise degradation patterns
•	Identify anomalies and outliers
•	Compare operating conditions
B. Diagnostic Analytics
•	Correlation analysis
•	Feature importance
•	Healthy vs degrading engine behaviour
•	Sensor drift analysis
C. Predictive Analytics
Models you may implement:
•	Linear Regression
•	Random Forest Regressor
•	Gradient Boosting (XGBoost / LightGBM)
•	LSTM or GRU neural networks (optional advanced step)
Evaluation metrics:
•	RMSE
•	MAE
•	R²
D. Prescriptive Analytics
•	Recommend maintenance intervals
•	Estimate downtime reduction
•	Provide cost benefit insights
•	Suggest operational adjustments
E. Cognitive Analytics (Optional)
•	Simulate a simple digital twin concept
•	Show how predictions update in real time

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
- Business focused presentation (**remove this**)
- Written report summarising findings and recommendations (**remove this**)

## Dashboard Development

A dashboard application was developed using Streamlit.  It allows both technical and non-technical uses to gain an insight into the dataset and perform some predictive maintenance analytics.  The dashboard covers the following:

- 
- 
- 

## Key Insights and Recommendations

- Written report summarising findings and recommendations (**remove this**)

## Future Work

A. Descriptive Analytics
•	Explore sensor trends over engine cycles
•	Visualise degradation patterns
•	Identify anomalies and outliers
•	Compare operating conditions
B. Diagnostic Analytics
•	Correlation analysis
•	Feature importance
•	Healthy vs degrading engine behaviour
•	Sensor drift analysis
C. Predictive Analytics
Models you may implement:
•	Linear Regression
•	Random Forest Regressor
•	Gradient Boosting (XGBoost / LightGBM)
•	LSTM or GRU neural networks (optional advanced step)
Evaluation metrics:
•	RMSE
•	MAE
•	R²
D. Prescriptive Analytics
•	Recommend maintenance intervals
•	Estimate downtime reduction
•	Provide cost benefit insights
•	Suggest operational adjustments
E. Cognitive Analytics (Optional)
•	Simulate a simple digital twin concept
•	Show how predictions update in real time

## Ethical Considerations

## Project Planning, Management and Documentation

## Conclusion

## Reflections

## AI Tools

The following AI tools were used in the project:

- Microsoft Copilot was used to search for a suitable dataset for the project.  It was also used to generate a suitable structure and business requirements for the project. Some code snipets were also generated for some parts of the project.
- GitHub Copilot was used for code snipets suggestion using prompting and for optimising some of the code.

## Credits

## Acknowledgement



## Template Instructions

Welcome,

This is the Code Institute student template for the Data Analytics capstone project. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo. Click the **Use this template** button, then click **Create a new repository**.

1. Copy the URL of your repository to your clipboard.

1. In VS Code, select **File** -> **Open Folder**.

1. Select your `vscode-projects` folder, then click the **Select Folder** button on Windows, or the **Open** button on Mac.

1. From the top menu in VS Code, select **Terminal** > **New Terminal** to open the terminal.

1. In the terminal, type `git clone` followed by the URL of your GitHub repository. Then hit **Enter**. This command will download all the files in your GitHub repository into your vscode-projects folder.

1. In VS Code, select **File** > **Open Folder** again.

1. This time, navigate to and select the folder for the project you just downloaded. Then, click **Select Folder**.

1. A virtual environment is necessary when working with Python projects to ensure each project's dependencies are kept separate from each other. You need to create your virtual environment, also called a venv, and then ensure that it is activated any time you return to your workspace.
Click the gear icon in the lower left-hand corner of the screen to open the Manage menu and select **Command Palette** to open the VS Code command palette.

1. In the command palette, type: *create environment* and select **Python: Create Environment…**

1. Choose **Venv** from the dropdown list.

1. Choose the Python version you installed earlier. Currently, we recommend Python 3.12.8

1. **DO NOT** click the box next to `requirements.txt`, as you need to do more steps before you can install your dependencies. Click **OK**.

1. You will see a `.venv` folder appear in the file explorer pane to show that the virtual environment has been created.

1. **Important**: Note that the `.venv` folder is in the `.gitignore` file so that Git won't track it.

1. Return to the terminal by clicking on the TERMINAL tab, or click on the **Terminal** menu and choose **New Terminal** if no terminal is currently open.

1. In the terminal, use the command below to install your dependencies. This may take several minutes.

 ```console
 pip3 install -r requirements.txt
 ```

1. Open the `jupyter_notebooks` directory, and click on the notebook you want to open.

1. Click the **kernel** button and choose **Python Environments**.

Note that the kernel says `Python 3.12.8` as it inherits from the venv, so it will be Python-3.12.8 if that is what is installed on your PC. To confirm this, you can use the command below in a notebook code cell.

```console
! python --version
```

## Deployment Reminders

* Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version that closest matches what you used in this project.
* The project can be deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the **Deploy** tab, select **GitHub** as the deployment method.
3. Select your repository name and click **Search**. Once it is found, click **Connect**.
4. Select the branch you want to deploy, then click **Deploy Branch**.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button **Open App** at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.
