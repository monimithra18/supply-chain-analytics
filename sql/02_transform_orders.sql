-- Create or replace the analytics summary table view/table
DROP TABLE IF EXISTS analytics_order_summary;

CREATE TABLE analytics_order_summary AS
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
JOIN raw_suppliers s ON o.supplier_id = s.supplier_id;