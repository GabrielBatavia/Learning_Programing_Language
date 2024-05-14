import requests
from datetime import datetime

MY_LAT = -7.966620
MY_LNG = 112.632629

parameters = {
    "lat" : MY_LAT,
    "lng":MY_LNG,
    "fomatted": 0 
}

def is_iss_overhead():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"Sunrise in malang will be in : {sunrise}")
    print(f"Sunset in malang will be in : {sunset}")

    time_now = datetime.now()
    print(f"Your time now is : {time_now}")

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    