import requests
import datetime as dt

# Informasi dasar pengguna
GENDER = "male"
WEIGHT_KG = "100"
HEIGHT_CM = "160"
AGE = "19"

# Informasi API Nutritionix
APP_ID = "c69ec56b"
API_KEY = "e8799c74ae966fa89c6901c002151040"

# Endpoint Sheety untuk menyimpan data latihan
SHETTY_ENDPOINT = "https://api.sheety.co/5fb410767ff998e7fb4d26150f7a67dd/bataviaWorkouts/workouts"

# Endpoint Nutritionix untuk menghitung kalori dari latihan
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Meminta input dari pengguna mengenai latihan yang telah dilakukan
exercise_text = input("Tell me which exercises you did: ")

# Header yang dibutuhkan untuk otentikasi API Nutritionix
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameter yang dikirim ke API Nutritionix untuk menghitung kalori
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Mengirim permintaan POST ke Nutritionix API untuk mendapatkan data latihan
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)  # Dapat digunakan untuk mencetak hasil dari API Nutritionix

# Mendapatkan tanggal dan waktu saat ini
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

# Memproses setiap latihan yang dikembalikan oleh API Nutritionix
for exercise in result["exercises"]:
    # Mempersiapkan data untuk dikirim ke Sheety API
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Mengirim permintaan POST ke Sheety API untuk menyimpan data latihan
    sheet_response = requests.post(SHETTY_ENDPOINT, json=sheet_inputs)
    print(sheet_response.text)  # Mencetak respons dari Sheety API

# Alternatif: Mengirim permintaan GET ke Sheety API untuk memeriksa data latihan yang sudah ada
# sheet_response = requests.get(SHETTY_ENDPOINT, headers=headers, verify=False)
# print(sheet_response.text)
