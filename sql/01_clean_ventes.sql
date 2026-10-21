-- 1. Macro pour nettoyer les espaces et convertir en nombre
CREATE TEMPORARY MACRO clean_num(x) AS (
    TRY_CAST(
        REPLACE(
            REGEXP_REPLACE(x::VARCHAR, '[^0-9,.]', '', 'g'), 
            ',', '.'
        ) AS DECIMAL(12,2)
    )
);
-- 2. Vue nettoyée avec conversion des types
CREATE OR REPLACE VIEW clean_ventes AS
SELECT
    CURRENT_TIMESTAMP AS date_importation,
    TRY_CAST(Date AS DATE) AS date_vente,
    Site AS site,
    clean_num(Ca_ht) AS ca_ht,
    clean_num(Ca_ttc) AS ca_ttc,
    clean_num(Food_ht) AS food_ht,
    clean_num(Bev_ht) AS bev_ht,
    TRY_CAST(Nb_de_cvts AS INT) AS nb_couverts
FROM raw_ventes
WHERE Date IS NOT NULL;