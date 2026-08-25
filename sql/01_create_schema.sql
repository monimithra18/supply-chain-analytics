-- Create raw suppliers table
CREATE TABLE IF NOT EXISTS raw_suppliers (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT NOT NULL,
    location TEXT NOT NULL,
    reliability_score REAL
);

-- Create raw orders table
CREATE TABLE IF NOT EXISTS raw_orders (
    order_id TEXT PRIMARY KEY,
    supplier_id TEXT,
    order_date TEXT,
    delivery_date TEXT,
    order_quantity INTEGER,
    unit_cost REAL,
    status TEXT,
    FOREIGN KEY (supplier_id) REFERENCES raw_suppliers(supplier_id)
);

-- Performance Indexes for Big Data (100k+ rows)
CREATE INDEX IF NOT EXISTS idx_orders_supplier ON raw_orders(supplier_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON raw_orders(status);