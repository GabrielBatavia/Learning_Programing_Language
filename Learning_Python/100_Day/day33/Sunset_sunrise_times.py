import requests
from datetime import datetime

MY_LAT = -7.966620
MY_LNG = 112.632629

parameters = {
    "lat" : MY_LAT,
    "lng":MY_LNG,
    "fomatted": 0 
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Sunrise in malang will be in : {sunrise}")
print(f"Sunset in malang will be in : {sunset}")

time_now = datetime.now()
print(f"Your time now is : {time_now}")