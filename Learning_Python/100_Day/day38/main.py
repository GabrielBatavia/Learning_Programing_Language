import requests

GENDER = "male"
WEIGHT_KG = "100"
HEIGHT_CM = "160"
AGE = "19"

APP_ID = "c69ec56b"
API_KEY = "e8799c74ae966fa89c6901c002151040"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)