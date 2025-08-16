-- Headcount by department
SELECT department, COUNT(*) AS headcount
FROM hris
GROUP BY department
ORDER BY headcount DESC;

-- Attrition rate by department
SELECT department,
       AVG(attrition)::float AS attrition_rate
FROM hris
GROUP BY department
ORDER BY attrition_rate DESC;

-- Median time to fill by source
SELECT source, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY time_to_fill_days) AS median_ttf
FROM recruiting
GROUP BY source
ORDER BY median_ttf;
