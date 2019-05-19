# coding:utf-8
"""
    单链表
        单链表与顺序表的对比
            操作                   链表        顺序表
            访问元素               O(n)        O(1)
            在头部插入/删除        O(1)        O(n)
            在尾部插入/删除        O(n)        O(1)
            在中间插入/删除        O(n)        O(n)
"""

class Node(object):
    """节点"""
    def __init__(self,elem): # 创建节点实例时需要，传入一个节点元素
        self.elem = elem # 节点元素
        self.next = None # 节点的下一元素（用来记录连接的指向）

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        self.__head = node # 链表头部，也就是第一个元素

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
        node.next = self.__head # 设置新添加的节点下一个元素为链表的头部
        self.__head = node # 设置链表的头部为新添加的节点元素

    def append(self, item):
        """链表尾部添加元素--尾插法"""
        node = Node(item) # 实例化节点对象（就是要添加的元素）
        if self.is_empty():
            self.__head = node # 如果链表为空的，链表头部等于节点
        else:
            cur = self.__head # 设置游标为头部
            while cur.next != None: # 如果链表还有下一元素
                cur = cur.next  # 移动游标到最后
            cur.next = node # 设置最后个为添加的该元素节点

    def insert(self, pos, item):
        """指定位置添加元素
            pos：位置坐标
        """
        if pos <= 0: # 如果要插入的位置小于0
            self.add(item) # 在头部添加就好
        elif pos > (self.length()-1): # 如果要插入的位置大于链表的长度
            self.append(item) # 尾部添加就好
        else:
            pre = self.__head # 获取头部角标
            count = 0 # 记录数量
            while count < (pos - 1): # 如果小于传入的插入位置减1的话
                count += 1 # 数量＋1
                pre = pre.next # （移动角标）
            # 循环结束后，pre指向了pos-1的位置处（也就是要添加的位置的前一个位置）
            node = Node(item) # 实例化节点
            node.next = pre.next # 设置新元素的下一个元素指向角标的下一个元素
            pre.next = node # 设置角标的下一个元素为新创建的节点元素

    def remove(self, item):
        """删除节点"""
        cur = self.__head # 设置一个当前角标变量指向头部
        pre = None # 设置一个当前角标的前一个角标变量
        while cur != None: # 遍历（如果当前角标不是None【None代表最后一个】）
            if cur.elem == item: # 找到了
                # 先判断此节点是否是头节点
                if cur == self.__head: # 是头节点
                    self.__head = cur.next # 设置头节点为下一个元素（也就是None）
                else: # 不是头节点
                    pre.next = cur.next # 设置前一个元素的下一个元素指向，当前查找到的元素的下一个元素（这样就不当前元素给抛弃了）
                    break
            else: # 没有找到
                pre = cur # 设置前一个角标为现在元素的角标（就是向后移动一个位置）
                cur = cur.next # 设置当前的角标为下一个元素的位置

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head # 设置一个变量表示当前角标指向头部
        while cur != None: # 遍历（如果当前角标不是指向最后一个None）
            if cur.elem == item: # 如果找到了
                return True # 返回True
            else: # 没有找到
                cur = cur.next # 移动角标
        return False # 遍历完成后没有找到返回False


if __name__ == "__main__":
    ll = SingleLinkList()
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