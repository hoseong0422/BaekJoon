-- 코드를 작성해주세요
SELECT HG.SCORE, HG.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_EMPLOYEES AS HE
JOIN 
(
    SELECT EMP_NO, YEAR, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    WHERE YEAR = 2022
    GROUP BY 1, 2
    ORDER BY 3 DESC
    LIMIT 1
) AS HG
ON HE.EMP_NO = HG.EMP_NO