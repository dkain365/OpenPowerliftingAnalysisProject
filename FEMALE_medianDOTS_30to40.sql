SELECT
    female_age_range,
    ROUND(CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dots) AS NUMERIC), 2) AS median_dots
FROM (
    SELECT
        sex,
        age,
        dots,
        CASE
            WHEN age BETWEEN 29.5 AND 30 THEN '29.5-30'
            WHEN age BETWEEN 30 AND 31 THEN '30-31'
            WHEN age BETWEEN 31 AND 32 THEN '31-32'
            WHEN age BETWEEN 32 AND 33 THEN '32-33'
            WHEN age BETWEEN 33 AND 34 THEN '33-34'
            WHEN age BETWEEN 34 AND 35 THEN '34-35'
            WHEN age BETWEEN 35 AND 36 THEN '35-36'
            WHEN age BETWEEN 36 AND 37 THEN '36-37'
            WHEN age BETWEEN 37 AND 38 THEN '37-38'
            WHEN age BETWEEN 38 AND 39 THEN '38-39'
            WHEN age BETWEEN 39 AND 40 THEN '39-40'
            ELSE 'Other'
        END AS female_age_range
    FROM
        openpowerlifting_data
    WHERE
        sex = 'F'
) AS age_data
GROUP BY
    female_age_range
ORDER BY
    female_age_range;