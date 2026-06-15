height = float(input("请输入身高(米): "))
weight = float(input("请输入体重(公斤): "))

bmi = weight / (height * height)

print("你的BMI是:", round(bmi, 2))

if bmi < 18.5:
    print("偏瘦")
    print("建议：增加蛋白质摄入和力量训练")

elif bmi < 24:
    print("正常")
    print("建议：继续保持当前状态")

elif bmi < 28:
    print("超重")
    print("建议：增加有氧运动并控制饮食")

else:
    
    print("肥胖")
    print("建议：制定减脂计划并控制热量摄入")