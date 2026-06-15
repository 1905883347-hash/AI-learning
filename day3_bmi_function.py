def calculate_bmi(weight, height):
    bmi=weight/(height*height)
    return bmi

bmi = calculate_bmi(70, 1.75)

print("BMI:", round(bmi, 2)