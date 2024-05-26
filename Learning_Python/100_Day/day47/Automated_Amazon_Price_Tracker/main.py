# Load environment variables from .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Import libraries 
import requests as req
from bs4 import BeautifulSoup
import lxml
import smtplib

# Set email
my_email = "gabrielbatavia20@gmail.com"
password = os.getenv('Password')
to_email = "gabrielbatavia7@gmail.com"

URL = "https://www.amazon.com/Overlord-Light-Novel-Kugane-Maruyama/dp/B0B3DB4W1N/ref=sr_1_4?crid=1Y0SM1NE2ZEXY&dib=eyJ2IjoiMSJ9.pkG-udsbgqyFhKnBZnimxSsznRqynQrFmzdcobgDk5tPPYQsamEgICq9vLrI-hSyHO8so0fqPapD7Sb0Zq2r8liNRPjes1hlce58L_NUqj-cWb3FtMyUZvx3MNUEN2VDcyE5ckURRXF9kBMTKY-_ZOg85vwTrb4sr6X5rLX_pHqlBKD_ZYPtau750WIr2fCaolD0gmK0R1i5u8SGZRICUC1VW42LzbFp5zUejizRxjo.E49UQ9IbSoNaJv6v-PqmK_sSssmmdCPUQ2MhEV-9WUI&dib_tag=se&keywords=overlord&qid=1716724883&sprefix=overlord%2Caps%2C308&sr=8-4"
Accept_Language = os.getenv('Accept_Language')
User_Agent = os.getenv('User_Agent')

headers = { 'Accept-Language' : Accept_Language,
            'User-Agent':User_Agent}


response = req.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float > 200:
    # Message we want to send
    subject = "Hello from Gabriel Batavia"
    body = f"Hay...The Overlord Noves is pretty cheap now! the price is ${price_as_float}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)