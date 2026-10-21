import os
import sys
import duckdb
from pathlib import Path
from dotenv import load_dotenv
from API.meteo_dlt import run_meteo_pipeline #<- IMPORT LA FUNCTION DE METEO DLT
from utils.logger import setup_logger

# 1. Connexion a motherduckdb
load_dotenv()
con = duckdb.connect("md:my_db")

# 2. importer logger
logger = setup_logger()

#3. DÉMARRAGE DU LOGER
logger.info("🚀 Démarrage du pipeline complet...")

try:
    # 2. Ingestion Météo via DLT (charge directement raw_meteo dans MotherDuck)
    logger.info("🌤️ Exécution du pipeline DLT Météo...")
    run_meteo_pipeline()
    logger.info("✅ Table raw_meteo créée avec succès via DLT !")

    # 4. Exécution séquentielle des scripts SQL de transformation
    for sql_file in sorted(Path("sql").glob("*.sql")):
        logger.info(f"⚙️ Exécution de {sql_file.name}...")
        sql_content = sql_file.read_text(encoding="utf-8")
        result = con.execute(sql_content)
        logger.info(f'fin exécution de {sql_file.name} avec succès !')
        
        # Si le script est une requête de sélection (comme l'audit), on trace le résultat
        if sql_content.strip().upper().startswith("SELECT"):
            df_result = result.df()
            logger.info(f"\n📊 Résultat de {sql_file.name} :\n{df_result.head()}:\n{df_result.info()}")

    logger.info("🚀 Pipeline terminé avec succès !")

except Exception as e:
    logger.error(f"❌ Erreur critique dans le pipeline : {e}")
    sys.exit(1)

con.close()