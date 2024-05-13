import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# reguler way (primitive)

#if response.status_code == 404:
#    raise Exception("That resource does not exist")
#elif response.status_code == 401:
#    raise Exception("Your not authorized to access this resource")


response.raise_for_status()

data = response.json()
longitude = data['iss_position']["longitude"]
latitude = data['iss_position']["latitude"]

iss_position = (longitude, latitude)
print(iss_position)