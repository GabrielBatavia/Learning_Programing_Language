import requests
from datetime import datetime

MY_LAT = -7.966620
MY_LNG = 112.632629

api_key = "551bfd1aedf3be81762a1a1835da73bd"

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LNG}&appid={api_key}")
response.raise_for_status()

data = response.json()
print(data)