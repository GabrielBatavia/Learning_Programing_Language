##################### Hard Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "xaveriusgabriel10@gmail.com"
PASSWORD = ""

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("./Birthday_Wisher/birthdays.csv")


birth_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birth_dict:
    person = birth_dict[today]
    
    file_path = f"./Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as template:
        content = template.read()
        content = content.replace("[NAME]", person["name"])
        message = content
    
    to_email = person["email"]
        
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=message)
    
    