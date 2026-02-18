import time
import json
from coordinator import city_status

def monitor_city():
    print("Urban Resilience Monitoring Started...")

    while True:
        try:
            # get real AI analysis from agents
            status = city_status()

            # add geo risk zones
            status["zones"] = [
                {"type": "flood", "lat": 10.020, "lon": 76.340, "level": status["flood"]},
                {"type": "traffic", "lat": 10.000, "lon": 76.360, "level": status["traffic"]},
                {"type": "crowd", "lat": 10.030, "lon": 76.320, "level": status["crowd"]},
                {"type": "power", "lat": 10.015, "lon": 76.350, "level": status["power"]}
            ]

            print("\n===== CITY STATUS UPDATE =====")
            print(status)

            # save as JSON (NOT str)
            with open("latest_alert.txt", "w", encoding="utf-8") as f:
                json.dump(status, f, indent=2)

        except Exception as e:
            print("Monitoring error:", e)

        time.sleep(20)  # every 20 sec


if __name__ == "__main__":
    monitor_city()
