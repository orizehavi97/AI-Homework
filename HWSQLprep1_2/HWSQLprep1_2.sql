-- i
SELECT * FROM products p
LEFT JOIN nutritions n
on n.product_id = p.product_id

-- ii
SELECT * FROM orders_products op
LEFT JOIN products p
on op.product_id = p.product_id
ORDER by op.order_id

-- iii
INSERT INTO orders_products (order_id, product_id, amount) VALUES
(1, 25, 5),
(2, 25, 4),
(3, 25, 3),
(4, 25, 2),
(5, 24, 1);

-- iv
UPDATE orders
SET total_price = (
    SELECT SUM(op.amount * p.price)
    FROM orders_products op
    JOIN products p ON op.product_id = p.product_id
    WHERE op.order_id = orders.order_id
);

-- v
SELECT max(total_price), order_id FROM orders
SELECT min(total_price), order_id FROM orders
SELECT avg(total_price) as average FROM orders

-- vi
SELECT o.customer_name, max(c) FROM(
SELECT customer_name, count(*) as c
FROM orders
GROUP by customer_name) o

-- vii
SELECT op.product_id, max(s) FROM(
SELECT product_id, sum(amount) as s
FROM orders_products
GROUP by product_id) op

SELECT op.product_id, min(s) FROM(
SELECT product_id, sum(amount) as s
FROM orders_products
GROUP by product_id) op

SELECT avg(s) FROM(
SELECT sum(amount) as s
FROM orders_products
GROUP by product_id) op

-- viii
SELECT c.category_id, max(s) FROM(
SELECT category_id, sum(amount) as s
FROM orders_products op
LEFT JOIN products p
on op.product_id = p.product_id
GROUP by p.category_id) c

SELECT c.category_id, min(s) FROM(
SELECT category_id, sum(amount) as s
FROM orders_products op
LEFT JOIN products p
on op.product_id = p.product_id
GROUP by p.category_id) c

-- ix
SELECT p.product_id, max(order_count) FROM(
SELECT p.product_id, p.name, COUNT(DISTINCT op.order_id) as order_count
FROM orders_products op
LEFT JOIN products p
ON op.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY order_count DESC) p
