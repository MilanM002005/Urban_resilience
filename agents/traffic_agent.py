from ingestion.traffic_api import get_traffic

def traffic_status():
    current, free = get_traffic()

    if current/free < 0.5:
        return "Heavy Traffic"
    return "Traffic Normal"
