import requests
import os
from twilio.rest import Client

MY_LAT = -6.175110
MY_LNG = 106.865036


# HOW TO HIDE API KEYS
# $env:API_NAME = "API KEY"

api_key = os.environ.get('OWN_API_KEY')
account_sid = "ACce17cd502cf4beb423025d650fa5ae2d"
auth_token = "6b147837bcc5d7e358f0e046e7dbb4ee"

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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "Itts going to rain today, Remember tp bring an umbrella",
        from_ = "+17209243744",
        to = "+6285157677512"
    )

    print(message.status)