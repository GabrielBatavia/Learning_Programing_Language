import json

people_identified = '''
{
    "people": [
        {
            "name": "Shalom Velicia",
            "phone": "0851-7263-8472",
            "has_license": false
        },
        {
            "name": "Linda Alwi",
            "phone": null,
            "has_license": false            
        }
    ]   
}
'''

data = json.loads(people_identified)

print(type(data))
print(type(data['people']))
print(data)

print()

# access to people_identified
for person in data['people']:
    print(person['name'])
    print(person['phone'])
    print(person)
    del person['phone']

print()
new_people = json.dumps(data, indent=2, sort_keys= True)
print(new_people)
