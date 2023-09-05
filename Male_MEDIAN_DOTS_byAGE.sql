SELECT
    male_age_range,
    ROUND(CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dots) AS NUMERIC), 2) AS median_dots
FROM (
    SELECT
        sex,
        age,
        dots,
        CASE
            WHEN age BETWEEN 19 AND 20 THEN '19-20'
            WHEN age BETWEEN 20 AND 21 THEN '20-21'
            WHEN age BETWEEN 21 AND 22 THEN '21-22'
            WHEN age BETWEEN 22 AND 23 THEN '22-23'
            WHEN age BETWEEN 23 AND 24 THEN '23-24'
            WHEN age BETWEEN 24 AND 25 THEN '24-25'
            WHEN age BETWEEN 25 AND 26 THEN '25-26'
            WHEN age BETWEEN 26 AND 27 THEN '26-27'
            WHEN age BETWEEN 27 AND 28 THEN '27-28'
            WHEN age BETWEEN 28 AND 29 THEN '28-29'
            WHEN age BETWEEN 29 AND 30 THEN '29-30'
            ELSE 'Over 30'
        END AS male_age_range
    FROM
        openpowerlifting_data
    WHERE
        sex = 'M'
) AS age_data
GROUP BY
    male_age_range
ORDER BY
    male_age_range;




