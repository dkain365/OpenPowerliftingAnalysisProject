SELECT
    ROUND(avg_dots, 2) AS avg_dots_rounded,
    state,
    "date",
    RANK() OVER (ORDER BY avg_dots DESC) as state_ranking_by_DOTS
FROM (
    SELECT
        AVG(dots) AS avg_dots,
        state,
        MIN("date") AS "date" 
    FROM
        openpowerlifting_data
    WHERE
        "date" > '2022-12-31'
        AND dots IS NOT NULL
    GROUP BY
        state
) AS avg_dots_per_state
LIMIT 10;

