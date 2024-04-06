# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state
FROM Address AS A
RIGHT JOIN Person AS P
ON P.personId = A.personId;