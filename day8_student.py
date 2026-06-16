students = {
    "小明": 90,
    "小红": 85,
    "小刚": 100
}
total=0
for name, score in students.items():
    print(f"{name}的成绩是{score}")
    total=total+score
average=total/len(students)
print(f"平均成绩是{average}")
top_name = ""
top_score = 0
for name, score in students.items():
    if score > top_score:
        top_score = score
        top_name = name
print(f"最高成绩是{top_score}，获得者是{top_name}")
for name, score in students.items():

    if score >= 90:
        print(f"{name}成绩优秀，成绩是{score}")

    elif score >= 80:
        print(f"{name}成绩良好，成绩是{score}")

    elif score >= 60:
        print(f"{name}成绩及格，成绩是{score}")

    else:
        print(f"{name}成绩不及格，成绩是{score}")