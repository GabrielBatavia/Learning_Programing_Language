# make  weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = eval(input("Input your temperature: "))

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)