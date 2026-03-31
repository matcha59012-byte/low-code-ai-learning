# lst = [1, 2, 3]
# lst.insert(0,0)
# print(lst)
# # [0,1,2,3]
# lst[1] = 5

# print(lst)

# lst.pop(1)

# print(lst[2])

# lst2 = [5,6,7]

# lst.extend(lst2)


# lst.remove(5)

# print(len(lst))


# #字典
# #1
# dic = {}
# dic['name'] = 'Alice'
# dic['age'] = 25

# #2
# dic['age'] = 26

# #3
# dic['city'] = 'New York'

# #4
# print(dic['name'])

# #5
# del dic['age']

# #6
# print("age" in dic)  

# #7
# print(dic.items())

#综合练习
students = {
    "class": "三年二班",
    "members": [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92}
    ]
}

# 1. 追加新学生
students["members"].append({"name": "王五", "score": 78})
print(students["members"])  # 包含三个学生

# 2. 修改李四的成绩
# 方法：找到李四的字典，修改score
for stu in students["members"]:
    if stu["name"] == "李四":
        stu["score"] = 95
        break
print(students["members"])

# 3. 删除张三
# 方法：遍历找到索引并删除
for i, stu in enumerate(students["members"]):
    if stu["name"] == "张三":
        del students["members"][i]
        break
print(students["members"])

# 4. 打印班级名称和所有学生名字
print(students["class"])
for stu in students["members"]:
    print(stu["name"])