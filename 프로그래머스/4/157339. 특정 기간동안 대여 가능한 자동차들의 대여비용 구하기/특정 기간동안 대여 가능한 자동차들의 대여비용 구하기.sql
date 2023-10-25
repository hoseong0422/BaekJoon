-- 코드를 입력하세요
WITH not_available_car AS (
 SELECT DISTINCT(car_id)
 FROM car_rental_company_rental_history
 WHERE (start_date <= '2022-11-30') AND (end_date >= '2022-11-01')
 ORDER BY car_id
),

available_car AS (
    SELECT car_id, car_type, daily_fee
    FROM car_rental_company_car
    WHERE car_id NOT IN 
    (
        SELECT car_id 
        FROM not_available_car
    ) 
    AND
    car_type IN ('세단', 'SUV')
),

discount_rate AS (
    SELECT car_type, (1-discount_rate/100) AS discount_rate
    FROM car_rental_company_discount_plan
    WHERE duration_type = '30일 이상'
)

SELECT car_id, car_type,
       round(daily_fee * 30 * discount_rate, 0) AS fee
FROM available_car
INNER JOIN discount_rate USING (car_type)
WHERE (daily_fee * 30 * discount_rate >= 500000) AND
      (daily_fee * 30 * discount_rate < 2000000)
ORDER BY fee DESC, car_type, car_id DESC