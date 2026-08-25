# 📦 Supply Chain Analytics & Predictive Modeling Platform

An enterprise-grade, end-to-end data science and engineering project simulating **100,000+ supply chain transactions**. The project combines a robust **SQLite database architecture**, **SQL transformation and analytics**, advanced **exploratory data analysis (EDA)**, **multi-model machine learning experimentation**, and an interactive **Streamlit web application**.

---

## 🚀 Project Architecture & Tech Stack

* **Database:** SQLite, SQL DDL, SQL transformations, analytical queries
* **Data Processing & Analysis:** Python, Pandas, NumPy, Scikit-Learn
* **Machine Learning:** Random Forest, XGBoost, Gradient Boosting, Decision Tree, Logistic Regression, Gaussian Naive Bayes
* **Visualization:** Matplotlib, Seaborn
* **Interactive Web App:** Streamlit
* **Version Control & Large Files:** Git, Git LFS

---

## 📂 Project Structure

```text
supply-chain-project/
│
├── data/                    # SQLite database and raw data assets
│   └── supply_chain.db
│
├── notebooks/               # Jupyter notebooks for EDA and modeling
│   ├── 01_eda_and_visualization.ipynb
│   └── 02_predictive_modeling.ipynb
│
├── models/                  # Serialized ML models
│   ├── random_forest_model.pkl
│   ├── xgboost_model.pkl
│   ├── gradient_boosting_model.pkl
│   ├── decision_tree_model.pkl
│   ├── logistic_regression_model.pkl
│   └── gaussian_nb_model.pkl
│
├── sql/                     # Database schema and analytical SQL
│   ├── 01_create_schema.sql
│   ├── 02_transform_orders.sql
│   └── 03_analytics_queries.sql
│
├── reports/                 # Project documentation and reports
│   └── project_summary.md
│
├── app.py                   # Interactive Streamlit application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📊 Analytics & Insights

The exploratory analysis focuses on operational and financial metrics that influence supply chain performance.

### Fulfillment Performance

Across **100,000+ processed transactions**, the analysis identified an overall delivery delay rate of approximately **18.7%** across regional distribution hubs.

### Supplier & Spend Analysis

SQL-based aggregations were used to analyze:

* Supplier spending patterns
* Order volumes
* Average order costs
* Lead-time efficiency
* Supplier-level operational performance
* Cost versus delivery performance

### Correlation & Data Exploration

EDA examined relationships between:

* Order quantities
* Unit costs
* Calculated lead times
* Delivery delays
* Shipping channels
* Regional performance

Multicollinearity checks, numerical distributions, and feature-level relationships were also evaluated before modeling.

---

## 🤖 Machine Learning Modeling & Comparison

A comparative machine learning pipeline was developed to evaluate **six classification algorithms** for predicting delivery-delay risk.

| Model                    | Accuracy | Precision | Recall | ROC-AUC |
| ------------------------ | -------: | --------: | -----: | ------: |
| **Logistic Regression**  |   81.27% |      0.00 |   0.00 |  0.4924 |
| **Gaussian Naive Bayes** |   81.27% |      0.00 |   0.00 |  0.5021 |
| **Decision Tree**        |   69.18% |      0.19 |   0.20 |  0.5041 |
| **Random Forest**        |   79.40% |      0.17 |   0.03 |  0.5038 |
| **Gradient Boosting**    |   81.26% |      0.33 | 0.0003 |  0.4943 |
| **XGBoost**              |   81.17% |      0.17 | 0.0014 |  0.4997 |

### 💡 Key Technical Takeaway

The modeling results highlight an important **data science and data quality lesson**: accuracy alone can be misleading when the target variable is highly imbalanced.

Although several models achieved approximately **81% accuracy**, their extremely low recall and near-random ROC-AUC scores indicate that they were not effectively identifying delivery-delay events.

This demonstrates why model evaluation should consider multiple metrics, particularly:

* Precision
* Recall
* ROC-AUC
* Class distribution
* Prediction behavior

The results also emphasize that machine learning performance depends heavily on the quality and predictive signal of the underlying features.

All six trained models are serialized and stored in the `models/` directory.

---

## 🖥️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/monimithra18/supply-chain-analytics.git
cd supply-chain-analytics
```

### 2. Create a Virtual Environment

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

The application will open in your browser and provide access to the interactive analytics and predictive modeling components.

---

## 🎯 Results & Application Features

### 📈 Interactive Executive Dashboard

Provides visibility into key supply chain KPIs, including:

* Total supply chain spend
* Fulfillment performance
* Supplier distribution
* Regional performance
* Order and delivery metrics

### 🔎 Data Explorer

A filterable interface allows users to explore transaction-level data directly from the SQLite database.

Users can inspect and filter supply chain records without querying the database manually.

### 🤖 Predictive Risk Simulator

The application provides an interactive interface for testing delivery-risk scenarios.

Users can enter custom order parameters and evaluate the predicted delivery-delay risk using any of the **six trained machine learning models**.

This connects the analytical pipeline to a practical decision-support interface for supply chain stakeholders.

---

## 🧠 Key Skills Demonstrated

This project demonstrates practical experience across the complete data science workflow:

* Relational database design
* SQL schema creation and transformations
* SQL analytical querying
* Data cleaning and preprocessing
* Exploratory data analysis
* Statistical analysis
* Feature engineering
* Classification modeling
* Model comparison and evaluation
* Imbalanced classification analysis
* Model serialization
* Interactive dashboard development
* Python application development
* Git and Git LFS
* End-to-end data science project development

---

## 📌 Project Objective

The goal of this project is to demonstrate how **data engineering, analytics, machine learning, and interactive visualization** can be combined into a single end-to-end supply chain intelligence platform.

Rather than focusing only on model accuracy, the project emphasizes the complete workflow:

**Raw Supply Chain Data → SQLite Database → SQL Transformations → EDA → Feature Engineering → ML Experiments → Model Evaluation → Interactive Business Application**
