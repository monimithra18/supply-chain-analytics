import sqlite3
import pandas as pd
import numpy as np
import os
import time

# Get absolute path of the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)

db_path = os.path.join(data_dir, "supply_chain.db")

print("Connecting to database and generating 100,000+ rows of mock data...")
start_time = time.time()

conn = sqlite3.connect(db_path)

# 1. Suppliers Data
suppliers_data = {
    "supplier_id": ["SUP_001", "SUP_002", "SUP_003", "SUP_004", "SUP_005"],
    "supplier_name": ["Apex Logistics", "Global Freight Co", "Swift Transit", "Prime Cargo", "Reliable Shipping"],
    "location": ["New York, USA", "Chicago, USA", "San Francisco, USA", "London, UK", "Toronto, Canada"],
    "reliability_score": [0.92, 0.85, 0.78, 0.95, 0.88]
}

df_suppliers = pd.DataFrame(suppliers_data)
df_suppliers.to_sql("raw_suppliers", conn, if_exists="replace", index=False)

# 2. Generate 100,000 Orders Data efficiently
np.random.seed(42)
n_orders = 100000

order_ids = [f"ORD_{i:06d}" for i in range(1, n_orders + 1)]
supplier_ids = np.random.choice(suppliers_data["supplier_id"], n_orders)

# Generate random dates across a 2-year span (2024-2026)
start_date = pd.to_datetime("2024-01-01")
random_days = np.random.randint(0, 730, size=n_orders)
order_dates = start_date + pd.to_timedelta(random_days, unit='D')

# Lead times between 2 and 20 days
lead_times = np.random.randint(2, 21, size=n_orders)
delivery_dates = order_dates + pd.to_timedelta(lead_times, unit='D')

order_quantities = np.random.randint(10, 1000, size=n_orders)
unit_costs = np.round(np.random.uniform(5.0, 500.0, size=n_orders), 2)
statuses = np.random.choice(["Delivered", "Delayed", "Cancelled"], size=n_orders, p=[0.78, 0.18, 0.04])

df_orders = pd.DataFrame({
    "order_id": order_ids,
    "supplier_id": supplier_ids,
    "order_date": order_dates.strftime("%Y-%m-%d"),
    "delivery_date": delivery_dates.strftime("%Y-%m-%d"),
    "order_quantity": order_quantities,
    "unit_cost": unit_costs,
    "status": statuses
})

# Write to SQLite in chunks to optimize memory and speed
df_orders.to_sql("raw_orders", conn, if_exists="replace", index=False, chunksize=10000)

# Add indexes for high performance querying
cursor = conn.cursor()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_supplier ON raw_orders(supplier_id);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_status ON raw_orders(status);")
conn.commit()

conn.close()

elapsed = time.time() - start_time
print(f"Success! 100,000 rows generated and indexed in {elapsed:.2f} seconds.")