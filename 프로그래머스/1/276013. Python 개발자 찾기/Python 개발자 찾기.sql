-- 코드를 작성해주세요
SELECT 
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM
    DEVELOPER_INFOS
WHERE
    SKILL_1 LIKE "%python%" OR
    SKILL_2 LIKE "%python%" OR
    SKILL_3 LIKE "%python%"
ORDER BY
    ID