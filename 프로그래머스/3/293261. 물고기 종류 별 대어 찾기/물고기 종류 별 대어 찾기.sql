-- 코드를 작성해주세요
WITH temp AS    
(SELECT
    FI.FISH_TYPE, FNI.FISH_NAME, MAX(FI.LENGTH) AS LENGTH
FROM
    FISH_INFO AS FI
JOIN
    FISH_NAME_INFO AS FNI
ON
    FI.FISH_TYPE = FNI.FISH_TYPE
GROUP BY
    1, 2)
    
SELECT
    FI.ID, T.FISH_NAME, T.LENGTH
FROM
    TEMP AS T
LEFT JOIN
    FISH_INFO AS FI
ON
    FI.FISH_TYPE = T.FISH_TYPE
    AND FI.LENGTH = T.LENGTH
ORDER BY
    ID ASC