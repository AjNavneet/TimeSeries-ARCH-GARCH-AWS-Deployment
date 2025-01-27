# Time Series ARCH Model and AWS Deployment

## Business Objective

Time series analysis involves studying a sequence of data points collected or recorded over time. The goal is often to forecast future data based on historical trends. Applications include:

- **Weather Monitoring**: Daily, hourly, or weekly weather data.
- **Performance Tracking**: Changes in application performance.
- **Medical Devices**: Real-time vitals monitoring.

This project focuses on using the **ARCH (Autoregressive Conditional Heteroskedasticity)** model, introduced by Engle in 1982, to capture conditional variance in time series data. Key concepts include:

- **Autoregressive**: Current values depend on past values.
- **Conditional Variance**: Variance depends on past errors.
- **Heteroskedasticity**: Time series exhibits changing variance over time.

The **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** model extends ARCH by incorporating past variances and squared residuals for better volatility modeling.

This project also incorporates **MLOps (Machine Learning Operations)** by deploying the ARCH model on the AWS platform, emphasizing cost optimization and scalability.

---

## Data Description

The dataset, titled "Call-centers," records monthly data for various domains (e.g., healthcare, telecom, banking). Key features include:

- **Month**: Time period.
- **Domains**: Call categories (e.g., healthcare, telecom).
- **External Regressors**: Number of channels and phone lines for traffic prediction and resource availability.

**Dimensions**: 132 rows × 8 columns.

---

## Aim

1. Build ARCH and GARCH models to analyze and forecast time series data.
2. Create an MLOps pipeline to deploy the ARCH model on AWS, ensuring scalability and cost efficiency.

---

## Tech Stack

- **Programming Language**: [Python](https://www.python.org/)
- **Libraries**:
  - [`Flask`](https://flask.palletsprojects.com/) for building the web application.
  - [`pickle`](https://docs.python.org/3/library/pickle.html) for model serialization.
  - [`pandas`](https://pandas.pydata.org/) and [`numpy`](https://numpy.org/) for data manipulation.
  - [`matplotlib`](https://matplotlib.org/) and [`seaborn`](https://seaborn.pydata.org/) for data visualization.
  - [`statsmodels`](https://www.statsmodels.org/) for statistical modeling.
  - [`arch`](https://arch.readthedocs.io/) for ARCH/GARCH models.
  - [`scipy`](https://scipy.org/) for scientific computing.
- **AWS Services**: [Amazon EC2](https://aws.amazon.com/ec2/), [AWS Lightsail](https://aws.amazon.com/lightsail/), [Docker](https://www.docker.com/).

---

## Approach

### Model Development

1. **Data Preprocessing**:
   - Set the date as the index.
   - Adjust the frequency to monthly.

2. **Exploratory Data Analysis (EDA)**:
   - Visualize the data for trends and seasonality.

3. **Model Building**:
   - Train ARCH models with varying lags.
   - Extend to GARCH models for better volatility forecasting.

4. **Forecasting**:
   - Use the best model to forecast time series data.

### Deployment Pipeline

1. **Model Saving**:
   - Serialize the ARCH model using `pickle`.

2. **Flask Application**:
   - Create a RESTful API for serving predictions.

3. **AWS Deployment**:
   - Set up an EC2 instance and configure it for deployment.
   - Use Docker for containerization.

4. **Lightsail Deployment**:
   - Optimize the deployment process using AWS Lightsail.

---

## Deployment Steps

1. **Model Creation**:
   - Save the trained model in `.pkl` format.

2. **Flask App Development**:
   - Build a Flask application to serve predictions.

3. **AWS EC2 Setup**:
   - Create and configure an EC2 instance.
   - Install required tools using `install-docker.sh` and `install-aws-cli.sh`.

4. **Code Upload**:
   - Use Cloud Shell or an S3 bucket to upload files to the EC2 instance.

5. **Dockerization**:
   - Build and run a Docker container for the application.

6. **Lightsail Configuration**:
   - Refer to `lightsail-deployment.md` for step-by-step deployment instructions.

---

## Project Structure

```plaintext
.
├── data/                                 # Input dataset (CallCenterData.xlsx).
├── MLPipeline/                           # Python scripts for preprocessing and modeling.
├── notebooks/                            # IPython notebook for ARCH model.
├── output/                               # Serialized models and results.
├── app.py                                # Flask app for serving predictions.
├── Dockerfile                            # Docker image configuration.
├── engine.py                             # Orchestrates MLPipeline functions.
├── install-aws-cli.sh                    # Steps for AWS CLI installation.
├── install-docker.sh                     # Steps for Docker installation.
├── install-lightsail-cli.sh              # Steps for Lightsail installation.
├── lightsail-deployment.md               # Lightsail deployment instructions.
├── requirements.txt                      # List of dependencies.
└── README.md                             # Project documentation.
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 3. Run the Project

Execute the pipeline by running the `engine.py` script:

```bash
python engine.py
```

### 4. Deploy the Flask App

Run the Flask application locally:

```bash
python app.py
```

---

## Results

- **Volatility Forecasting**:
  - Accurate forecasting of time series data using ARCH and GARCH models.
- **Scalable Deployment**:
  - Efficient deployment on AWS using Docker and Lightsail.
- **User-Friendly API**:
  - Flask app for easy interaction with the model.

---

## Feature of This Project?

- **Advanced Modeling**: Leverages ARCH and GARCH models for robust time series analysis.
- **MLOps Integration**: Combines machine learning with scalable AWS deployment.
- **Practical Application**: Ideal for real-world scenarios involving volatility forecasting and cloud deployment.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature-name
```

3. Commit your changes:

```bash
git commit -m "Add feature"
```

4. Push your branch:

```bash
git push origin feature-name
```

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any questions or suggestions, please reach out to:

- **Name**: [Your Name]
- **Email**: [Your Email]
- **GitHub**: [Your GitHub Profile]

---

## Acknowledgments

Special thanks to:

- [ARCH Documentation](https://arch.readthedocs.io/) for guidance on ARCH/GARCH modeling.
- [Flask](https://flask.palletsprojects.com/) for API development.
- [AWS](https://aws.amazon.com/) for cloud deployment tools.
- [Docker](https://www.docker.com/) for containerization.
- The Python open-source community for their invaluable tools and resources.

---
