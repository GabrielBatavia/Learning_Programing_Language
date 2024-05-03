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
print(data)