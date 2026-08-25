import sqlite3
import pandas as pd
import os

# Get absolute path to database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "supply_chain.db")

# Connect to database
conn = sqlite3.connect(db_path)

# Write a SQL query to join orders with suppliers and calculate metrics
query = """
SELECT 
    o.order_id,
    o.supplier_id,
    s.supplier_name,
    s.location,
    o.order_date,
    o.delivery_date,
    o.order_quantity,
    o.unit_cost,
    (o.order_quantity * o.unit_cost) AS total_order_value,
    o.status,
    julianday(o.delivery_date) - julianday(o.order_date) AS calculated_lead_time
FROM raw_orders o
JOIN raw_suppliers s ON o.supplier_id = s.supplier_id
"""

# Load transformed data into a pandas dataframe
df_transformed = pd.read_sql_query(query, conn)

# Save the transformed data back into the database as an analytics table
df_transformed.to_sql("analytics_order_summary", conn, if_exists="replace", index=False)

conn.close()

print("Success! Data transformed and saved into 'analytics_order_summary' table.")
print("\nPreview of transformed data:")
print(df_transformed.head())