# Telco Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to **churn** or **stay** based on their service usage and account information.

## Project Overview

Customer churn is a major problem for telecom companies.
This project uses Machine Learning to analyze customer data and predict churn risk so companies can take action before losing customers.

## Features

* Customer churn prediction using Machine Learning
* Data preprocessing using a Pipeline
* Multiple models tested (Logistic Regression, Random Forest, Gradient Boosting)
* Hyperparameter tuning for improved performance
* Feature importance analysis
* Flask web application for real-time prediction
* Clean dark-themed UI
* Ready for deployment

## Machine Learning Workflow

1. Data Exploration (EDA)
2. Data Cleaning & Preprocessing
3. Pipeline Creation
4. Model Training
5. Ensemble Learning
6. Hyperparameter Tuning
7. Feature Importance Analysis
8. Model Deployment with Flask

## Model Performance

Best model: **Logistic Regression**

* Accuracy: ~73%
* Churn Recall: **79%**

High recall helps detect customers likely to churn so companies can intervene early.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML & CSS
* Gunicorn

## Project Structure

```
telco-customer-churn
│
├── models
│   └── churn_model.pkl
│  
├──  notebooks   
│   └── churn_analysis.ipynb 
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

Clone the repository

```
git clone https://github.com/your-username/telco-customer-churn.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Flask app

```
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

## Future Improvements

* Add dropdown inputs instead of comma input
* Improve UI/UX
* Deploy using Docker
* Add SHAP model explainability

## Author

**Kartikey Gehra | **Data Science Enthusiast  
