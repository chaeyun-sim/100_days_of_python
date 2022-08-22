def bmi_calculator(bmi):
    if bmi < 16.0:
        category = "Underweight with Severe thinness"
    elif bmi <= 16.9:
        category = "Underweight with moderate thinness"
    elif bmi <= 18.4:
        category = "Underweight with mild thinness"
    elif bmi <= 24.9:
        category = "You are in Normal range"
    elif bmi <= 29.9:
        category = "Overweight with pre-obese"
    elif bmi <= 34.9:
        category = "Mild obese"
    elif bmi <= 39.9:
        category = "Obese"
    elif bmi >= 40:
        category = "Severe Obese"
    else:
        "Wrong number"
    return category


print("Hello, this is a BMI Calculator.")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / pow(float(height), 2)
category = bmi_calculator(bmi)
print("Your BMI is " + category)



# 강의 풀이
# print("Hello, this is a BMI Calculator.")
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = float(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)