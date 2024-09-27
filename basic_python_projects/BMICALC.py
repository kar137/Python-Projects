weight = input("Enter your weight in kg: \n")
height = input("Enter your height in m: \n")

w=float(weight)
h=float(height)

BMI = int(w/h**2)

print("Your BMI is: " + str(BMI))