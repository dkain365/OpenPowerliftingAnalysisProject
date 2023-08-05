--Median DOTS by year (Male & Female) with percent increase by year

WITH MedianCTE AS (
    SELECT
        sex,
        EXTRACT(YEAR FROM "date") AS year,
        ROUND(dots, 2) AS dots_rounded,
        ROW_NUMBER() OVER (PARTITION BY sex, EXTRACT(YEAR FROM "date") ORDER BY dots) AS row_num,
        COUNT(*) OVER (PARTITION BY sex, EXTRACT(YEAR FROM "date")) AS count_rows
    FROM
        openpowerlifting_data
    WHERE
        dots IS NOT NULL
        AND "division" IN ('FR-O', 'MR-O')
)
SELECT
    sex,
    year,
    CAST(AVG(dots_rounded) FILTER (WHERE row_num = (count_rows + 1) / 2) AS NUMERIC(10, 2)) AS median_dots,
    CAST(
        100.0 * (AVG(dots_rounded) FILTER (WHERE row_num = (count_rows + 1) / 2) -
                 LAG(AVG(dots_rounded) FILTER (WHERE row_num = (count_rows + 1) / 2))
                 OVER (PARTITION BY sex ORDER BY year)) /
        LAG(AVG(dots_rounded) FILTER (WHERE row_num = (count_rows + 1) / 2))
        OVER (PARTITION BY sex ORDER BY year)
        AS NUMERIC(10, 2)
    ) AS percent_increase_median
FROM
    MedianCTE
GROUP BY
    sex,
    year
ORDER BY
    sex,
    year;
