# coding:utf-8
"""
    队列的实现--先进先出
        队列：
            Queue()     创建一个空的队列
            enqueue()   往队列中添加一个item元素
            dequeue()   从队列头部删除一个元素
            is_empty()  判断一个队列是否为空
            size()      返回队列的大小
"""

# 队列
class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()

    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)

    print(s.is_empty())

    for i in range(s.size()):
        print(s.dequeue())