height = float(input("enter your height[m]: "))
weight = float(input("enter your weight[kg]: "))

BMI = float(weight / height ** 2)
if BMI < 18.5:
    result = "underweight"
elif BMI < 25:
    result = "normal weight"
elif BMI < 30:
    result = "slightly overweight"
elif BMI < 35:
    result = "obese"
else:
    result = "clinically obese"
print(f"Your BMI is {BMI:.2f}, which means: {result}")