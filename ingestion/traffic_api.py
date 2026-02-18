import requests

API_KEY = "ZzJ85mNOLHTTLohe8XyJvpHcSAA16JZU"

def get_traffic():
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point=9.9312,76.2673&key={API_KEY}"
    r = requests.get(url).json()

    data = r["flowSegmentData"]

    return data["currentSpeed"], data["freeFlowSpeed"]
