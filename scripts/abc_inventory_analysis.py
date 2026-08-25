import sqlite3
import pandas as pd
import os

# Get absolute path to database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "supply_chain.db")

conn = sqlite3.connect(db_path)

# Query total spend per supplier to run an ABC Inventory Classification
query = """
SELECT 
    supplier_name,
    SUM(total_order_value) AS total_spend,
    COUNT(order_id) AS total_orders
FROM analytics_order_summary
GROUP BY supplier_name
ORDER BY total_spend DESC;
"""

df_abc = pd.read_sql_query(query, conn)

# Calculate cumulative spend and percentage for ABC analysis
df_abc['cumulative_spend'] = df_abc['total_spend'].cumsum()
df_abc['cumulative_percentage'] = (df_abc['cumulative_spend'] / df_abc['total_spend'].sum()) * 100

# Assign ABC Classification Tiers
def assign_abc_tier(cum_pct):
    if cum_pct <= 80.0:
        return 'Class A (High Value)'
    elif cum_pct <= 95.0:
        return 'Class B (Moderate Value)'
    else:
        return 'Class C (Low Value)'

df_abc['abc_class'] = df_abc['cumulative_percentage'].apply(assign_abc_tier)

# Save back to database
df_abc.to_sql("analytics_abc_classification", conn, if_exists="replace", index=False)

conn.close()

print("--- ABC INVENTORY & SUPPLIER CLASSIFICATION ---")
print(df_abc[['supplier_name', 'total_spend', 'cumulative_percentage', 'abc_class']])