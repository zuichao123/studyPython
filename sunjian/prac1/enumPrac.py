#coding:utf-8
'''
    枚举类练习
        是通过单例模式实现的
        是不能实例化的
'''
from enum import Enum
from enum import IntEnum,unique

class VIP(Enum):
    YELLOW = 1
    YELLOW_alias = 1# 取值相等时用：别名
    GREEN = 2
    BLACK = 3
    RED = 4

# 输出枚举
print(VIP.RED)
for i in VIP:
    print(i)

print('---------------------------------')
# 输出别名
for i in VIP.__members__:
    print(i)

print('---------------------------------')
# 枚举的比较运算
result = VIP.GREEN == VIP.BLACK
print(result)

print('---------------------------------')
# 通过给变量赋值打印枚举
a = 1
print(VIP(a))

print('---------------------------------')
@unique
class VIP2(IntEnum):
    '''继承IntEnum后，枚举类中的值只能是数字'''
    YELLOW = 1
    # YELLOW = 1
    BLUE = 2
    WRITE = '5'

for i in VIP2:
    print(i)