import dlt
import requests

@dlt.resource(name="raw_meteo", write_disposition="replace")
def get_meteo():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=45.83&longitude=6.21&start_date=2020-06-20&end_date=2026-10-03&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"
    response = requests.get(url)
    data = response.json()["daily"]
    
    # Transformation des listes en enregistrements individuels (aplatissement)
    for i in range(len(data["time"])):
        yield {
            "time": data["time"][i],
            "temperature_2m_max": data["temperature_2m_max"][i],
            "temperature_2m_min": data["temperature_2m_min"][i],
            "precipitation_sum": data["precipitation_sum"][i]
        }

def run_meteo_pipeline():
    # Correction : utiliser la destination motherduck native de dlt
    pipeline = dlt.pipeline(
        pipeline_name="meteo_pipeline",
        destination="motherduck",
        dataset_name="main"
    )
    
    load_info = pipeline.run(get_meteo())
    print(load_info)

if __name__ == "__main__":
    run_meteo_pipeline()