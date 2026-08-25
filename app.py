import streamlit as st
import pandas as pd
import sqlite3
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Supply Chain Analytics & Intelligence Hub",
    page_icon="📦",
    layout="wide"
)

# Database Connection Helper
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "data", "supply_chain.db")

@st.cache_data
def load_data():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM analytics_order_summary", conn)
    conn.close()
    return df

df = load_data()

# App Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["📊 Executive Overview", "🔍 Data Explorer", "🤖 ML Delay Predictor"])

# --- PAGE 1: EXECUTIVE OVERVIEW ---
if page == "📊 Executive Overview":
    st.title("📦 Supply Chain Executive Dashboard")
    st.markdown("High-level overview of supplier performance, spending, and order fulfillment tracking.")

    # Key Metrics Row
    total_orders = len(df)
    total_spend = df['total_order_value'].sum()
    avg_lead_time = df['calculated_lead_time'].mean()
    delay_rate = (df['status'] == 'Delayed').mean() * 100

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Orders", f"{total_orders:,}")
    col2.metric("Total Spend", f"${total_spend:,.2f}")
    col3.metric("Avg Lead Time", f"{avg_lead_time:.1f} Days")
    col4.metric("Delay Rate", f"{delay_rate:.1f}%")

    st.markdown("---")

    # Visualizations
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Top Suppliers by Spend")
        supplier_spend = df.groupby('supplier_name')['total_order_value'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=supplier_spend, x='total_order_value', y='supplier_name', palette='crest', ax=ax)
        ax.set_xlabel("Total Spend ($)")
        ax.set_ylabel("Supplier Name")
        st.pyplot(fig)

    with col_b:
        st.subheader("Order Status Distribution")
        status_counts = df['status'].value_counts().reset_index()
        status_counts.columns = ['status', 'count']
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=status_counts, x='status', y='count', palette='Set2', ax=ax)
        ax.set_xlabel("Status")
        ax.set_ylabel("Count")
        st.pyplot(fig)

# --- PAGE 2: DATA EXPLORER ---
elif page == "🔍 Data Explorer":
    st.title("🔍 Raw Order Data Explorer")
    st.markdown("Filter and inspect the underlying supply chain database.")

    # Sidebar Filters
    selected_status = st.sidebar.multiselect("Filter by Status", df['status'].unique(), default=df['status'].unique())
    selected_location = st.sidebar.multiselect("Filter by Location", df['location'].unique(), default=df['location'].unique())

    filtered_df = df[df['status'].isin(selected_status) & df['location'].isin(selected_location)]

    st.dataframe(filtered_df, use_container_width=True)
    st.write(f"Showing {len(filtered_df):,} of {len(df):,} total orders.")

# --- PAGE 3: ML DELAY PREDICTOR ---
elif page == "🤖 ML Delay Predictor":
    st.title("🤖 Supply Chain Delay Prediction Hub")
    st.markdown("Test out your trained machine learning models to predict whether a new order will experience a delay.")

    # Model Selector
    model_choice = st.selectbox("Select ML Model", [
        "Random Forest", "XGBoost", "Gradient Boosting", 
        "Decision Tree", "Logistic Regression", "Gaussian Naive Bayes"
    ])

    model_filename_map = {
        "Random Forest": "random_forest_model.pkl",
        "XGBoost": "xgboost_model.pkl",
        "Gradient Boosting": "gradient_boosting_model.pkl",
        "Decision Tree": "decision_tree_model.pkl",
        "Logistic Regression": "logistic_regression_model.pkl",
        "Gaussian Naive Bayes": "gaussian_nb_model.pkl"
    }

    # Input Form
    with st.form("prediction_form"):
        st.subheader("Order Parameters")
        col1, col2 = st.columns(2)
        
        with col1:
            order_qty = st.number_input("Order Quantity", min_value=1, max_value=10000, value=150)
            unit_cost = st.number_input("Unit Cost ($)", min_value=0.01, max_value=1000.0, value=25.50)
        
        with col2:
            supplier = st.selectbox("Supplier Name", df['supplier_name'].unique())
            lead_time = st.number_input("Calculated Lead Time (Days)", min_value=1, max_value=90, value=14)

        submit_button = st.form_submit_button("Predict Delay Risk")

    if submit_button:
        total_val = order_qty * unit_cost
        
        # Build feature DataFrame mimicking training structure
        input_data = pd.DataFrame({
            'order_quantity': [order_qty],
            'unit_cost': [unit_cost],
            'total_order_value': [total_val],
            'calculated_lead_time': [lead_time],
            'supplier_name': [supplier]
        })

        # Recreate dummy columns matching training encoding
        all_suppliers = df['supplier_name'].unique()
        for s in all_suppliers[1:]: # drop_first=True equivalent
            input_data[f'supplier_name_{s}'] = 1 if supplier == s else 0
        
        input_data = input_data.drop(columns=['supplier_name'])

        # Load chosen model
        model_path = os.path.join(BASE_DIR, "models", model_filename_map[model_choice])
        if os.path.exists(model_path):
            loaded_model = joblib.load(model_path)
            prediction = loaded_model.predict(input_data)[0]
            probability = loaded_model.predict_proba(input_data)[0][1] if hasattr(loaded_model, "predict_proba") else 0.0

            st.markdown("---")
            st.subheader("Prediction Results")
            if prediction == 1:
                st.error(f"⚠️ **High Risk:** This order is predicted to be **Delayed** (Confidence: {probability*100:.1f}%).")
            else:
                st.success(f"✅ **Low Risk:** This order is predicted to be **On-Time** (Delay Probability: {probability*100:.1f}%).")
        else:
            st.error(f"Model file not found at {model_path}. Please check your models/ folder.")