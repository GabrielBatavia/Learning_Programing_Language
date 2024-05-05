# reguler way
#with open('weather_data.csv') as data_file:
#    data = data_file.readlines()

#   print(data)


# using csv library
import csv

tempratures = []

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    
    for row in data:
        print(row)
        
    # kembali ke awal file csv
    data_file.seek(0) # ini dilakukan jika kita sudah melakukan sesuatu ke data namun ingin melakukan hal lain lagi
    
    for row in data:
        if row[1] != "temp": # exclude label 
            tempratures.append(row[1])
    
    print(tempratures)
    

print()
print()

# use the more useful library
# pandas is powerful library

import pandas as pd

data = pd.read_csv('weather_data.csv')
print(type(data)) # pandas frame == table
print(data)
print()
print(type(data["temp"])) # pandas series == column
print(data["temp"])

print()

# convert to dictionary
data_dict = data.to_dict()
print(type(data_dict))
print(data_dict)

print()

# convert to list
temp_list = data["temp"].to_list()
print(type(temp_list))
print(temp_list)

print()

# get summary reguler way
avarage_temp = sum(temp_list) / len(temp_list)
print(avarage_temp)

# get summary with pandas
avarage_temp = data["temp"].mean()
print(avarage_temp)

# get maximum temp with pandas
max_temp = data['temp'].max()
print(max_temp)

# get minimum temp with pandas
min_temp = data['temp'].min()
print(min_temp)

print()

# get data in columns
# print(data['condition'])
print(data.condition) # simple way 

print()

# Get data in rows
print(data[data.day == 'Monday'])

# get max temp row 
print(data[data.temp == data.temp.max()])

# get particular column in particular row
monday = data[data.day == 'Monday']
print(monday.condition)

f_temp = monday['temp'] * 9/5 + 32
print(f_temp)

print()
print()

# Create a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 67, 80]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv('new_data.csv')