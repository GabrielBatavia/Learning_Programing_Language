import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=15&category=18&type=boolean", params=parameters)
response.raise_for_status()
    
question = response.json()
question_data = question["results"]