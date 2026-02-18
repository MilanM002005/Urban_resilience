from agents.flood_agent import flood_status
from agents.traffic_agent import traffic_status
from agents.power_agent import power_status

def city_status():
    flood = flood_status()
    traffic = traffic_status()
    power = power_status()

    risk_score = 0

    if "HIGH" in flood:
        risk_score += 4
    if "SEVERE" in traffic:
        risk_score += 3
    if "OUTAGE" in power:
        risk_score += 5

    # Decision Engine
    if risk_score >= 7:
        level = "🚨 CRITICAL"
        advice = "Avoid travel. Emergency services recommended."
    elif risk_score >= 4:
        level = "⚠️ WARNING"
        advice = "Be cautious. Some city services affected."
    else:
        level = "✅ NORMAL"
        advice = "City operating normally."

    return f"""
CITY RISK LEVEL: {level}

Flood: {flood}
Traffic: {traffic}
Power: {power}

Advice: {advice}
"""
