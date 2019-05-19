# cding:utf-8
"""
    栈的实现
        先进后出
"""

class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = [] # 定义一个私有的列表

    def push(self, item):
        """添加一个新的原素item到栈顶（最后）"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.is_empty())
    print(s.peek())

    for i in range(s.size()):
        print(s.pop())