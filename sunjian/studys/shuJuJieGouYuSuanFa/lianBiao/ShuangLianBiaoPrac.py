# coding:utf-8
"""
    双向链表
"""

class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item # 节点元素
        self.next =  None # 节点的后一个指向
        self.prev = None # 节点的前一个指向


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """单链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素--头插法"""
        node = Node(item)
        node.next = self.__head  # 设置新添加的节点下一个元素为链表的头部
        self.__head = node  # 设置链表的头部为新添加的节点元素
        node.next.prev = node # 设置当前节点的下一个元素的前一个指向为当前节点

    def append(self, item):
        """链表尾部添加元素--尾插法"""
        node = Node(item)  # 实例化节点对象（就是要添加的元素）
        if self.is_empty():
            self.__head = node  # 如果链表为空的，链表头部等于节点
        else:
            cur = self.__head  # 设置游标为头部
            while cur.next != None:  # 如果链表还有下一元素
                cur = cur.next  # 移动游标到最后
            cur.next = node  # 设置最后一个为添加的该元素节点
            node.prev = cur # 将当前的游标位置设置为刚刚添加的节点的指向

    def insert(self, pos, item):
        """指定位置添加元素
            pos：位置坐标
        """
        if pos <= 0:  # 如果要插入的位置小于0
            self.add(item)  # 在头部添加就好
        elif pos > (self.length() - 1):  # 如果要插入的位置大于链表的长度
            self.append(item)  # 尾部添加就好
        else:
            cur = self.__head  # 获取头部角标
            count = 0  # 记录数量
            while count < pos:  # 如果小于传入的插入位置的话
                count += 1  # 数量＋1
                cur = cur.next  # （移动角标）
            # 循环结束后，cur指向了pos的位置处（也就是要添加的位置的前一个位置）
            node = Node(item)  # 实例化节点
            node.next = cur  # 设置新元素的下一个元素指向插入的位置
            node.prev = cur.prev # 设置插入的节点的前一个指向为当前位置的前一个指向
            cur.prev.next = node # 设置当前位置处的前一个节点的下一个指向为插入的节点
            cur.prev = node # 设置当前位置的前一个指向为插入的节点

    def remove(self, item):
        """删除节点"""
        cur = self.__head  # 设置一个当前角标变量指向头部
        while cur != None:  # 遍历（如果当前角标不是None【None代表最后一个】）
            if cur.elem == item:  # 找到了
                # 先判断此节点是否是头节点
                if cur == self.__head:  # 是头节点
                    self.__head = cur.next  # 设置头节点为下一个元素（也就是None）
                    if cur.next: # 如果下一个元素存在（就是不为None）
                        cur.next.prev = None # 设置当前节点的下一个节点的前一个指向为None
                else:  # 不是头节点
                    cur.prev.next = cur.next # 设置当前节点的前一个节点的下一个指向为，当前的元素的下一个（这样就把当前的节点绕过去了）
                    if cur.next: # 如果下一个元素存在（就是不为None）
                        cur.next.prev = cur.prev # 设置当前节点的下一元素的前一个的指向为，当前节点的前一个元素
                    break
            else:  # 没有找到
                pre = cur  # 设置前一个角标为现在元素的角标（就是向后移动一个位置）
                cur = cur.next  # 设置当前的角标为下一个元素的位置

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head  # 设置一个变量表示当前角标指向头部
        while cur != None:  # 遍历（如果当前角标不是指向最后一个None）
            if cur.elem == item:  # 如果找到了
                return True  # 返回True
            else:  # 没有找到
                cur = cur.next  # 移动角标
        return False  # 遍历完成后没有找到返回False


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(9)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)

    ll.insert(3, 100)
    ll.travel()
    ll.insert(5, 101)
    ll.travel()

    print(ll.search(100))
    ll.remove(101)
    ll.travel()