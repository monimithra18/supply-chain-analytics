-- 1. Supplier Performance & Total Spend Breakdown
SELECT 
    supplier_name,
    COUNT(order_id) AS total_orders,
    SUM(total_order_value) AS total_spend,
    ROUND(AVG(calculated_lead_time), 1) AS avg_lead_time_days
FROM analytics_order_summary
GROUP BY supplier_name
ORDER BY total_spend DESC;

-- 2. Order Fulfillment Status Breakdown & Percentages
SELECT 
    status,
    COUNT(order_id) AS count,
    ROUND(COUNT(order_id) * 100.0 / (SELECT COUNT(*) FROM analytics_order_summary), 2) AS percentage
FROM analytics_order_summary
GROUP BY status;