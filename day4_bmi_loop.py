def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "超重"
    else:
        return "肥胖"
running = "Y"

while running == "Y":



    height = float(input("请输入身高(米): "))
    weight = float(input("请输入体重(公斤): "))
    bmi = calculate_bmi(weight, height)

    category = bmi_category(bmi)
    print("BMI:", round(bmi, 2))
    print("分类:", category)
    running=input("是否继续计算? (Y/N): ")        