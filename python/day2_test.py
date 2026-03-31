account = "admin"
password = "123456"


while True:
    user_account = input("请输入你的账号")
    if user_account == "admin":
        print("请输入您的密码：")
        user_password = input("请输入你的密码")
        if user_password == "123456":
            print("密码正确")
            break
        else:
            print("密码错误")
            continue
            
    else:
        print("您输入的账号有误")
        continue
