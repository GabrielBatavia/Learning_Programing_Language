import json

with open("./people.json", mode="r") as f:
    data = json.load(f)

for person in data['people']:
    print(person['name'])
    print(person['phone'])
    print(person)