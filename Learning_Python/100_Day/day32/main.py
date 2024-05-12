#import smtplib

#my_email = "xaveriusgabriel10@gmail.com"
#password = ""
#to_email = "bataviasensei@gmail.com"

# Message we want to send
#subject = "Hello from Python"
#body = "This is a test email sent from Python."
#message = f"Subject: {subject}\n\n{body}"

#with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)


import datetime as dt

now = dt.datetime.now()
year = now.year
#print(year)

date_of_birth = dt.datetime(year=2005, month=5, day=12, hour=15)
print(date_of_birth)