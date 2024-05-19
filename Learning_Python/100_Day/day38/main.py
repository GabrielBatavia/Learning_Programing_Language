import requests
import datetime as dt

GENDER = "male"
WEIGHT_KG = "100"
HEIGHT_CM = "160"
AGE = "19"

APP_ID = "c69ec56b"
API_KEY = "e8799c74ae966fa89c6901c002151040"
SHETTY_ENDPOINT = "https://api.sheety.co/5fb410767ff998e7fb4d26150f7a67dd/bataviaWorkouts/workouts"

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
#print(result)




# sheet #

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #sheet_response = requests.post(SHETTY_ENDPOINT, json=sheet_inputs)

    #print(sheet_response.text)
    
sheet_response = requests.get(SHETTY_ENDPOINT, headers=headers, verify=False)
print(sheet_response.text)