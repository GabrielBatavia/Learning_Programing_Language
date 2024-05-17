import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get('API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY
}


response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()
data = data['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)



before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data['4. close']
print(before_yesterday_closing_price)

difference_price = float(before_yesterday_closing_price) - float(yesterday_closing_price)

if difference_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference_price / float(yesterday_closing_price)) * 100)


if abs(diff_percent) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news = news_response.json()
    articles = news["articles"]
    
    three_articles = articles[:3]
    print(three_articles)
    
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = article,
            from_ = "+17209243744",
            to = "+6285157677512"
        )


