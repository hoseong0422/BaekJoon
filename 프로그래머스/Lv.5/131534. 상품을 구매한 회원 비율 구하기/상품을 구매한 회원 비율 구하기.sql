-- 코드를 입력하세요
SELECT 
    YEAR(sales_date) AS year,
    MONTH(sales_date) AS month, 
    COUNT(DISTINCT(UI.user_id)) AS puchased_users,
    ROUND(COUNT(DISTINCT(UI.user_id)) 
    / 
    (SELECT COUNT(DISTINCT(user_Id)) FROM user_info WHERE joined LIKE '2021%'), 1) AS puchased_ratio
FROM user_info UI
LEFT JOIN ONLINE_SALE AS OS
ON UI.user_id = OS.user_id 
WHERE sales_date IS NOT NULL AND joined LIKE '2021%'
GROUP BY 2
ORDER BY 1 ASC, 2 ASC