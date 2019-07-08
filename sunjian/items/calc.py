# -*- coding:utf-8 -*-
"""
    计算器
"""

def add(str):
    """加"""
    total = 0
    numbers = []
    numbers += str.split("+")
    for number in numbers:
        total += float(number)
    print("{0} = {1}".format(str, total))

def reduce(str):
    """减"""
    total = 0
    numbers = []
    numbers += str.split("-")
    result = float(numbers[0]) # 得到第一个减数
    numbers.pop(0) # 将第一个减数弹栈
    for number in numbers:
        result -= float(number)
    print("{0} = {1}".format(str, result))

def ride(str):
    """乘"""
    total = 1
    numbers = []
    numbers += str.split("*")
    for number in numbers:
        total *= float(number)
    print("{0} = {1}".format(str, total))

def div(str):
    """除"""
    total = 0
    numbers = []
    numbers += str.split("/")
    result = float(numbers[0]) # 得到第一个除数
    numbers.pop(0) # 将第一个除数弹栈
    for number in numbers:
        result /= float(number)
    print("{0} = {1}".format(str, result))


def operator(tip):
    """具体操作方法"""
    try:
        while True:
            if tip == "1":
                str = input("请按此格式输入（1+2+3+...）,输入完成后回车即可")
                add(str)
                tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）")
            elif tip == "2":
                str = input("请按此格式输入（3-2-1-...）,输入完成后回车即可")
                reduce(str)
                tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）")
            elif tip == "3":
                str = input("请按此格式输入（1*2*3*...）,输入完成后回车即可")
                ride(str)
                tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）")
            elif tip == "4":
                str = input("请按此格式输入（3/2/1/...）,输入完成后回车即可")
                div(str)
                tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）")
            elif tip == "q":
                print("\n感谢使用...")
                break
            else:
                print("---------------输入错误，请重新输入...")
                tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）")
    except Exception as e:
        print("\n---------------sorry 请按套路出牌好吗...")


if __name__ == "__main__":
    print("*"*43)
    print("*"*10+"欢迎使用sunjian牌计算机"+"*"*10)
    print("*"*43)
    tip = input("加法：请按1（回车）\n减法：请按2（回车）\n乘法：请按3（回车）\n除法：请按4（回车）\n退出：请按q")
    operator(tip)
