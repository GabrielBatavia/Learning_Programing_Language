# You are going to write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries.

# Your job is to create a function that can add new countries to this list.


country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 

def add_new_country(new_country, num_visit, city_list):
    
