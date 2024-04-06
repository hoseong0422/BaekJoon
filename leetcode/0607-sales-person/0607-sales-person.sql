# Write your MySQL query statement below
SELECT s.name
FROM Orders AS o
JOIN Company AS c
ON o.com_id = c.com_id
AND c.name = 'RED'
RIGHT JOIN SalesPerson AS s
ON o.sales_id = s.sales_id
WHERE o.sales_id IS NULL;