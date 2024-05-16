import requests
from datetime import datetime

MY_LAT = -6.175110
MY_LNG = 106.865036

api_key = "551bfd1aedf3be81762a1a1835da73bd"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()

weather_data = response.json()
# weather_data["list"][0]["weather"]

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    print("Bring an umbrella")