##### 任务1：变量作用域练习，掌握global关键字的用法
###### 任务要求
#1.  定义全局变量`total_study_days = 28`，`completed_days = 7`
#2.  定义函数`complete_one_day()`：每调用一次，就把`completed_days`加1，打印当前完成天数
#3.  定义函数`get_progress()`：计算并返回学习完成进度（完成天数/总天数），保留2位小数
#4.  定义函数`reset_progress()`：把完成天数重置为0，打印重置提示
#5.  调用所有函数，验证功能正常

#调用utils.py文件里面的函数
from utils import add_num, multiply_num, is_even, get_max


import requests
# 导入内置模块datetime
from datetime import datetime

# 测试代码
if __name__ == "__main__":
    print("\n=== 第三方库requests测试 ===")
    # 发送GET请求到百度
    response = requests.get("https://www.baidu.com", timeout=10)
    # 打印状态码
    print("响应状态码：", response.status_code)
    # 打印响应头里的服务器信息
    print("服务器信息：", response.headers.get("Server"))

    print("\n=== 内置模块datetime测试 ===")
    # 获取当前时间
    now = datetime.now()
    # 格式化输出：年-月-日 时:分:秒
    format_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("当前系统时间：", format_time)


# # 测试导入的函数
# if __name__ == "__main__":
#     print("\n=== 模块导入测试 ===")
#     print("加法测试：10 + 20 =", add_num(10, 20))
#     print("乘法测试：5 * 6 * 2 =", multiply_num(5, 6, 2))
#     print("偶数判断：10是偶数？", is_even(10))
#     print("最大值测试：25和18的最大值是", get_max(25, 18))

# #1
# total_study_days = 28
# completed_days = 7

# #2
# def complete_one_day():
#     global completed_days #第一次没加
#     completed_days += 1
#     print(f"今日学习完成！累计完成天数：{completed_days}")

# #3
# def get_progress():
#     return (completed_days / total_study_days)

# #4
# def reset_progress():
#     global completed_days #也没加
#     completed_days = 0
#     print(f"已重置完成天数，目前完成天数为{completed_days}天")

# if __name__ == "__main__":
#     print("初始完成天数：", completed_days)
#     print("初始学习进度：", get_progress(), "%")

#     complete_one_day()
#     get_progress()
#     reset_progress()

