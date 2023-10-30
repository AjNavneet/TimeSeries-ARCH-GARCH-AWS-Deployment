# Time Series ARCH Model Deployment on AWS

## Business Objective

A time series is a sequence of data points ordered over time. In time series analysis, time is often the independent variable, and the primary goal is to make future forecasts. Time series data finds applications in various day-to-day activities, such as:

- Tracking daily, hourly, or weekly weather data
- Monitoring changes in application performance
- Visualizing real-time vitals in medical devices

The ARCH (Autoregressive Conditional Heteroskedasticity) process, introduced by Engle in 1982, explicitly accounts for the difference between unconditional and conditional variance. It allows the conditional variance to change over time based on past errors. The key components are:

- Autoregressive: Current values are correlated with previous values.
- Conditional: Variance depends on past errors.
- Heteroskedasticity: The series exhibits varying variance.

GARCH (Generalized Autoregressive Conditional Heteroskedasticity) is an extension of the ARCH model, incorporating past variances and squared residuals to estimate current and future variances. It is well-suited for modeling time series data with heteroskedasticity and volatility clustering.

Deployment is the process of integrating a machine learning model into an existing production environment, enabling practical decision-making based on data. MLOps (Machine Learning Operations) emphasizes automation and monitoring at all stages of ML system construction, including integration, testing, releasing, deployment, and infrastructure management.

In this project, we aim to create an MLOps project for deploying the time series ARCH model using Python on the AWS cloud platform (Amazon Web Services), with a focus on cost optimization by minimizing the use of services.

---

## Data Description

The dataset is "Call-centers" data, recorded at a monthly level. Calls are categorized by domain as the call center operates for various domains. External regressors, such as the number of channels and phone lines, indicate traffic predictions by in-house analysts and resource availability.

The dataset contains 132 rows and 8 columns:

- Month, healthcare, telecom, banking, technology, insurance, number of phone lines, and number of channels.

---

## Aim

- Build ARCH and GARCH models on the provided dataset.
- Create an MLOps pipeline using the Amazon Web Services (AWS) platform to deploy the time series ARCH model in a production environment.

----

## Tech Stack

- **Language:** `Python`
- **Libraries:** `Flask`, `pickle`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `scipy`, `arch`
- **Services:** `Flask`, `AWS`, `Docker`, `Lightsail`, `EC2`

---

## Approach

1. Import the required libraries and read the dataset.
2. Perform descriptive analysis.
3. Data pre-processing:
   - Set the date as the index.
   - Set the frequency as monthly.
4. Exploratory Data Analysis (EDA):
   - Visualize the data.
5. Perform train-test split.
6. Calculate returns and volatility.
7. ARCH model:
   - Install necessary libraries.
   - Build ARCH models with varying parameters.
   - Build higher-lag ARCH models.
8. GARCH model:
   - Build a GARCH model.
9. Forecasting the results:
   - Forecast results using the best model.

---

1. **Model Creation**
   - Save the model in a pickle format (.pkl).

2. **Flask App**
   - Create a Flask application.

3. **EC2 Machine Setup**
   - Create an EC2 instance using the AWS Management Console.
   - Launch the instance.
   - Install the 'Putty' tool on your local machine for remote access.

4. **EC2 and Docker Setup**
   - Follow the instructions in the 'install-docker.sh' file.

5. **AWS CLI Installation**
   - Follow the steps in the 'install-aws-cli.sh' file.

6. **Lightsail Installation**
   - Refer to the steps in the 'install-lightsail-cli.sh' file.

7. **Upload Files to the EC2 Machine**
   - **Method 1:**
     - Upload the code file in zip format on AWS Console (Cloud Shell).
   - **Method 2:**
     - Create an S3 storage bucket.
     - Copy the object URL and use it on the EC2 machine to download the code.
     - Unzip the Bitbucket folder.

8. **Deployment**
   - Follow the installation order as outlined in 'lightsail-deployment.md'.

---

## Project Structure

1. **Input:** CallCenterData.xlsx
2. **MLPipeline:** This folder contains all the functions organized into different Python files.
3. **Notebook:** Time series ARCH model IPython notebook file.
4. **Output:** ARCH model saved in a pickle format.
5. **App.py:** Flask app configuration.
6. **Dockerfile:** Docker image configuration.
7. **Engine.py:** File where the MLPipeline files are called.
8. **install-aws-cli.sh:** Steps for AWS CLI installation.
9. **install-docker.sh:** Steps for Docker installation.
10. **install-lightsail-cli.sh:** Steps for Lightsail installation.
11. **lightsail-deployment.md:** Lightsail deployment readme file.
12. **requirements.txt:** List of essential libraries with their versions.

---

## Key Concepts Explored

- Introduction to time series analysis.
- Data preprocessing and EDA.
- Understanding ARCH and GARCH models.
- Building and training ARCH and GARCH models.
- Forecasting with ARCH and GARCH models.
- Model deployment using AWS services, including EC2, Docker, and Lightsail.
- MLOps best practices for continuous model delivery and deployment.

---