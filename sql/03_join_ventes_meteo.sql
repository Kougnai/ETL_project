CREATE OR REPLACE TABLE ventes_meteo AS
SELECT 
    current_timestamp AS date_importation,
    v.date_vente,
    v.site,
    v.ca_ht,
    v.nb_couverts,
    v.ca_ttc,
    v.food_ht,
    v.bev_ht,
    m.temp_max,
    m.temp_min,
    m.precipitations
FROM clean_ventes v
LEFT JOIN clean_meteo m ON v.date_vente = m.date_meteo;