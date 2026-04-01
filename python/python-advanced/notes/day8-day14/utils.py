"""
低代码AI应用开发学习通用工具模块
包含常用的基础功能函数
"""

def add_num(a, b):
    """
    两个数字相加
    :param a: 第一个数字，int/float
    :param b: 第二个数字，int/float
    :return: 两个数的和，int/float
    """
    return a + b

def multiply_num(a, b, c=1):
    """
    三个数字相乘，第三个数字默认1
    :param a: 第一个数字，int/float
    :param b: 第二个数字，int/float
    :param c: 第三个数字，int/float，默认值1
    :return: 三个数的乘积，int/float
    """
    return a * b * c

def is_even(num):
    """
    判断一个数是不是偶数
    :param num: 要判断的整数，int
    :return: 是偶数返回True，奇数返回False，bool
    """
    return num % 2 == 0

def get_max(a, b):
    """
    返回两个数中较大的那个
    :param a: 第一个数字，int/float
    :param b: 第二个数字，int/float
    :return: 较大的数字，int/float
    """
    if a > b:
        return a
    else:
        return b