import requests
import pandas as pd

def fetch_meteo(start_date, end_date):
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude=45.83&longitude=6.21&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"
    
    data = requests.get(url).json()["daily"]
    
    return pd.DataFrame(data).rename(columns={
        "time": "date_meteo",
        "temperature_2m_max": "temp_max",
        "temperature_2m_min": "temp_min",
        "precipitation_sum": "precipitations"
    })