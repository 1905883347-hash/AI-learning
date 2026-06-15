def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi



def bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 24:
        return "正常"
    else:
        return "偏胖"
    
    
    
bmi = calculate_bmi(70, 1.75)

category = bmi_category(bmi)

print("BMI:", round(bmi, 2))
print("分类:", category)