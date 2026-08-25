import sqlite3
import pandas as pd
import os

# Get absolute path to database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "supply_chain.db")

# Connect to database
conn = sqlite3.connect(db_path)

# Query 1: Supplier Performance Summary (Spend, Order Count, Avg Lead Time)
supplier_perf_query = """
SELECT 
    supplier_name,
    COUNT(order_id) AS total_orders,
    SUM(total_order_value) AS total_spend,
    ROUND(AVG(calculated_lead_time), 1) AS avg_lead_time_days
FROM analytics_order_summary
GROUP BY supplier_name
ORDER BY total_spend DESC;
"""

df_supplier_perf = pd.read_sql_query(supplier_perf_query, conn)

# Query 2: Order Status Breakdown (Delivered vs Delayed vs Cancelled)
status_query = """
SELECT 
    status,
    COUNT(order_id) AS count,
    ROUND(COUNT(order_id) * 100.0 / (SELECT COUNT(*) FROM analytics_order_summary), 2) AS percentage
FROM analytics_order_summary
GROUP BY status;
"""

df_status = pd.read_sql_query(status_query, conn)

conn.close()

print("--- SUPPLIER PERFORMANCE ANALYTICS ---")
print(df_supplier_perf)
print("\n--- ORDER FULFILLMENT STATUS BREAKDOWN ---")
print(df_status)