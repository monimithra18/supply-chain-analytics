import sqlite3
import os

# Create a folder named 'data' if it doesn't exist
os.makedirs("data", exist_ok=True)

db_path = "data/supply_chain.db"

# Connect to SQLite (this automatically creates the database file)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a raw suppliers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_suppliers (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT,
    location TEXT,
    reliability_score REAL
);
""")

# Create a raw orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_orders (
    order_id TEXT PRIMARY KEY,
    supplier_id TEXT,
    order_date TEXT,
    delivery_date TEXT,
    order_quantity INTEGER,
    unit_cost REAL,
    status TEXT
);
""")

conn.commit()
conn.close()

print("Success! Database and tables created.")
