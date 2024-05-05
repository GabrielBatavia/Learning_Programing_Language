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
print(data)