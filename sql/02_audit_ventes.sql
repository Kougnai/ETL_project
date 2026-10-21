SELECT 
    (SELECT COUNT(*) FROM raw_ventes) AS nb_lignes_raw,
    COUNT(*) AS nb_lignes_clean,
    COUNT(date_vente) AS nb_dates_valides,
    COUNT(ca_ht) AS nb_ca_ht_valides,
    MIN(date_vente) AS date_debut,
    MAX(date_vente) AS date_fin,
    ROUND(SUM(ca_ht), 2) AS total_ca_ht
FROM clean_ventes;