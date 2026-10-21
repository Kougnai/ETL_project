CREATE OR REPLACE TABLE clean_meteo AS 
SELECT 
    current_timestamp AS date_importation,
    TRY_CAST(date_meteo AS DATE) AS date_meteo,
    TRY_CAST(temp_max AS FLOAT) AS temp_max,
    TRY_CAST(temp_min AS FLOAT) AS temp_min,
    TRY_CAST(precipitations AS FLOAT) AS precipitations
FROM raw_meteo
WHERE date_meteo IS NOT NULL;