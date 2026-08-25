# Supply Chain Analytics & Predictive Modeling - Project Summary

## Executive Summary
This project implements an end-to-end data pipeline, exploratory data analysis (EDA), and machine learning framework simulating enterprise-scale supply chain logistics (100,000+ records). The goal is to analyze supplier performance, track order fulfillment, and predict potential delivery delays.

---

## Key Performance Indicators (KPIs) & Findings
* **Total Order Volume:** 100,000+ transactions processed via a local SQLite database (`supply_chain.db`).
* **Fulfillment Performance:** Approximately 18.7% of orders experience delays across regional shipping hubs.
* **Supplier Impact:** Performance tracking reveals major cost concentrations and lead time variances across multiple suppliers (Global Freight Co, Swift Transit, Reliable Shipping, Prime Cargo).

---

## Machine Learning Experimentation
We tested and evaluated **6 diverse machine learning models** ranging from linear baselines to advanced gradient boosting algorithms:
1. **Logistic Regression** (Baseline)
2. **Gaussian Naive Bayes**
3. **Decision Tree Classifier**
4. **Random Forest Classifier**
5. **Gradient Boosting Classifier**
6. **XGBoost Classifier**

### Modeling Insights:
* Models were evaluated using **Accuracy, Precision, Recall, and ROC-AUC**. 
* Due to the independent nature of the baseline mock features relative to random delay assignments, advanced tree-based models and linear models correctly identified the lack of direct linear correlation, providing a crucial lesson in data hygiene and feature engineering.
* All trained models have been serialized and stored in the `models/` directory using `joblib` for future deployment.

---

## Tech Stack
* **Database:** SQLite & SQL
* **Data Processing & Analysis:** Python, Pandas, NumPy, Scikit-Learn
* **Machine Learning:** XGBoost, LightGBM, Random Forest
* **Visualization:** Matplotlib, Seaborn
* **Interactive App:** Streamlit