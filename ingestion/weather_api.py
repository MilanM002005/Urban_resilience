import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")

def get_weather(city="Kochi"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url).json()

    return {
        "temp": r["main"]["temp"],
        "humidity": r["main"]["humidity"],
        "rain": r.get("rain", {}).get("1h", 0)
    }
