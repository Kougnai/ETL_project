CREATE OR REPLACE TABLE raw_ventes AS 
SELECT 
*,
CURRENT_TIMESTAMP AS date_importation,
CURRENT_DATE as date_imp_date
FROM read_csv_auto('Data/Cassines_bdd - Ventes.csv', header=True);