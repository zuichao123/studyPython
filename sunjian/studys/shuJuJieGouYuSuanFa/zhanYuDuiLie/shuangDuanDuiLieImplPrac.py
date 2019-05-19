# coding:utf-8
"""
      双队列的实现--先进先出
        双端队列：
            Deque()         创建一个空的双端队列
            add_front(item) 从队头加入一个item元素
            add_rear(item)  从队尾加入一个item元素
            remove_front()  从对头删除一个item元素
            remove_rear()   从队尾删除一个item元素
            is_empty()      判断双端队列是否为空
            size()          返回队列的大小
"""
# 双端队列
class Deque(object):
    """创建一个空的双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个item元素"""
        return self.__list.pop(-1)

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Deque()

    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)

    print(s.is_empty())
    print("对头",s.remove_front())
    print("队尾",s.remove_rear())
    print(s.size())