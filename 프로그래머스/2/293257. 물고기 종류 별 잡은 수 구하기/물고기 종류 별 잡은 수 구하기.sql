-- 코드를 작성해주세요
SELECT
    B.FISH_COUNT,
    A.FISH_NAME
FROM
    FISH_NAME_INFO AS A
JOIN 
    (
        SELECT
            FISH_TYPE, COUNT(FISH_TYPE) AS FISH_COUNT
        FROM
            FISH_INFO
        GROUP BY 
            1
    ) AS B
ON 
    A.FISH_TYPE = B.FISH_TYPE
ORDER BY
    1 DESC

