#coding:utf-8
'''
    石头剪刀布
'''
import random
player = int(input("0剪刀，1石头，2布"))
computer = random.randint(0,2)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player==2 and computer ==1):
    print("winner")
elif (player == computer):
    print("平局")
else:
    print("fail")