# 1,定义加法函数
def add(a,b):
    return a + b

print(add(10,20))

def grade_score(score):
    if ((score <= 100) and (score > 90)):
        return "成绩为A"
    elif((score <= 90) and (score > 80)):
        return "成绩为B"
    elif((score <= 80) and (score > 70)):
        return "成绩为C"
    else:
        return "成绩为D"

print(grade_score(95))
print(grade_score(85))
print(grade_score(75))
print(grade_score(65))

def calculate_annual_salary(monthly_salary, bonus=0):
    return (monthly_salary * 12 + bonus)

print(calculate_annual_salary(10000,5000))
print(calculate_annual_salary(20000))


