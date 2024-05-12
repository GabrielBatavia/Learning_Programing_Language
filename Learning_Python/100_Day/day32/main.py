import smtplib
import datetime as dt
import random

my_email = "xaveriusgabriel10@gmail.com"
password = ""
to_email = "petruskmkz@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    # Message we want to send
    subject = "Hello from Gabriel Batavia"
    body = f"Hay...remember...im always care about you...this is quote for you today : {quote}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)