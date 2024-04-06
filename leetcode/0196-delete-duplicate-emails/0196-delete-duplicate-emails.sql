# Write your MySQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    SELECT sub.id
    FROM (
        SELECT MIN(id) AS id, email
        FROM Person
        GROUP BY email
        ) AS sub
    )