# utils/logger.py
import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("ETL_Pipeline")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        
        # Fichier de log centralisé
        file_handler = logging.FileHandler("logs/pipeline.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Affichage terminal
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        
    return logger