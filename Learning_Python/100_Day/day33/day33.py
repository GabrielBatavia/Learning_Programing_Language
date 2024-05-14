import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -7.966620
MY_LNG = 112.632629

parameters = {
    "lat" : MY_LAT,
    "lng":MY_LNG,
    "fomatted": 0 
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 10 <= iss_latitude <= MY_LAT + 10 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_nigth():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"Sunrise in malang will be in : {sunrise}")
    print(f"Sunset in malang will be in : {sunset}")

    time_now = datetime.now().hour
    print(f"Your time now is : {time_now}")
    
    if time_now >= sunset or time_now <= sunrise:
        return True



# Main Send and email

while True:
    time.sleep(1000)
    my_email = "xaveriusgabriel10@gmail.com"
    password = "wtsbzslxwdunojwf"
    to_email = "gabrielbatavia7@gmail.com"
    
    subject = "Hello from Gabriel Batavia"
    body = f"Hay...Look...the satelit is over out head"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)