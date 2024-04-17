# You are going to write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries.

# Your job is to create a function that can add new countries to this list.


country = input("Please input the country : ") # Add country name
visits = int(input("Input how many times you go there : ")) # Number of visits
list_of_cities = eval(input("Make a list in that country that allready you visits : Make like ['bekasi', 'bogor'] : ")) # create list from formatted string

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

# make the function to add to list
def add_new_country(new_country, num_visit, city_list):
    new_dict_travel = {}
    new_dict_travel["country"] = new_country
    new_dict_travel["visits"] = num_visit
    new_dict_travel["cities"] = city_list
    travel_log.append(new_dict_travel)


# Do not change the code below 
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
