# Write your MySQL query statement below
SELECT E.name, B.bonus
FROM Employee AS E
LEFT JOIN Bonus As B
ON E.empId = B.empId
WHERE bonus < 1000
OR bonus IS NULL;