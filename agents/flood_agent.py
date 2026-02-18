from ingestion.weather_api import get_weather

def flood_status():
    data = get_weather()

    if data["rain"] > 15 or data["humidity"] > 90:
        return "High Flood Risk"
    return "Normal Flood Risk"
