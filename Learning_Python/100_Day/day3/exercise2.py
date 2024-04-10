# make a bmi 2.0 

height = float(input("Please enter your height : "))
weight = int(input("Please enter your weight : "))

bmi = weight / (height ** 2)

if bmi <= 18.5 :
    print(f"You bmi is {round(bmi, 2)}, you are underweight")
elif bmi <= 25 :
    print(f"You bmi is {round(bmi, 2)}, you are normal")
elif bmi <= 30 :
    print(f"You bmi is {round(bmi, 2)}, you are overweight")
elif bmi <= 35 :
    print(f"You bmi is {round(bmi, 2)}, you are obese")
else :
    print(f"you bmi is {round(bmi, 2)}, you are clinicaly obese")