-- Superstore销售数据分析项目
-- Author: hongyang
-- 数据库: superstore_analysis
-- 数据表: orders


USE superstore_analysis;


-- 1. 总销售额

SELECT
SUM(Sales) AS total_sales
FROM orders;



-- 2. 总订单数量

SELECT
COUNT(DISTINCT `Order ID`) AS order_count
FROM orders;



-- 3. 平均订单金额

SELECT
AVG(Sales) AS avg_sales
FROM orders;



-- 4. 月销售趋势

SELECT
DATE_FORMAT(`Order Date`,'%Y-%m') AS month,
SUM(Sales) AS sales
FROM orders
GROUP BY month
ORDER BY month;



-- 5. 品类销售排名

SELECT
Category,
SUM(Sales) AS sales
FROM orders
GROUP BY Category
ORDER BY sales DESC;



-- 6. 区域销售分析

SELECT
Region,
SUM(Sales) AS sales
FROM orders
GROUP BY Region
ORDER BY sales DESC;



-- 7. Top10商品

SELECT
`Product Name`,
SUM(Sales) AS sales
FROM orders
GROUP BY `Product Name`
ORDER BY sales DESC
LIMIT 10;



-- 8. Top客户

SELECT
`Customer Name`,
SUM(Sales) AS sales
FROM orders
GROUP BY `Customer Name`
ORDER BY sales DESC
LIMIT 10;
