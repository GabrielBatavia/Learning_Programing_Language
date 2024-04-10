# Make BMI Calculations
print(" Weclome to BMI calculation")
print("Please input yout height and width")

height = input()
weight = input()

height_norm = float(height)
weight_norm = int(weight)

height_norm_final = height_norm ** 2
#height_norm_final = int(height_norm_final)
bmi = weight_norm / height_norm_final

print('Your bmi is', str(bmi))