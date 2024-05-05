import pandas as pd

data = pd.read_csv('./analyst_project/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#print(data.columns.values)

print()

gray_color_row = data[data['Primary Fur Color'] == 'Gray']
gray_columns = gray_color_row['Primary Fur Color'] 
#print(gray_columns)
gray_total = gray_columns.count()

black_color_row = data[data['Primary Fur Color'] == 'Black']
black_columns = black_color_row['Primary Fur Color'] 
#print(gray_columns)
black_total = black_columns.count()

cinnamon_color_row = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_columns = cinnamon_color_row['Primary Fur Color'] 
#print(cinnamon_columns)
cinnamon_total = cinnamon_columns.count()

# Create a dataframe from scratch
data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_total, cinnamon_total, black_total]
}

new_df = pd.DataFrame(data_dict)
print(new_df)

new_df.to_csv('squirrel_count.csv')