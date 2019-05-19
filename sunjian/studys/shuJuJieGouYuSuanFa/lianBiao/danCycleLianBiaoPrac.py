# coding:utf-8
"""
    单向循环链表
"""

class Node(object):
    """节点"""
    def __init__(self,elem): # 创建节点实例时需要，传入一个节点元素
        self.elem = elem # 节点元素
        self.next = None # 节点的下一元素（用来记录连接的指向）

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node = None):
        self.__head = node # 链表头部，也就是第一个元素
        if node: # 如果传入的节点不为None
            node.next = node # 设置该节点的下一个指向自身

    def is_empty(self):
        """单链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty(): # 如果是空链表
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head: # 如果当前节点的下一个不是头部
            count += 1
            cur = cur.next # 继续移动角标
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head # 创建一个游标指向节点头部
        while cur.next != self.__head: # 如果当前的节点的下一个不是头部
            print(cur.elem, end=" ") # 不换行输出当前节点的元素
            cur = cur.next # 设置当前节点为下一个（移动角标）
        # 退出循环，cur指向尾节点，但尾结点的元素未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素--头插法"""
        node = Node(item)
        if self.is_empty(): # 如果是空链表
            self.__head = node # 设置头部为该节点
            node.next = node # 设置该节点的下一个指向自身
        else:
            cur = self.__head # 创建一个游标指向节点头部
            while cur.next != self.__head: # 如果当前节点的下一个不是头部
                cur = cur.next # 移动角标
            # 退出循环，cur指向尾节点（因为尾结点的下一个指向头）
            node.next = self.__head # 设置当前节点的下一个指向头部
            self.__head = node # 设置头部为当前节点
            cur.next = self.__head # 设置尾节点的下一个指向头部（也就是指向刚添加的节点）

    def append(self, item):
        """链表尾部添加元素--尾插法"""
        node = Node(item) # 实例化节点对象（就是要添加的元素）
        if self.is_empty():
            self.__head = node # 如果链表为空的，链表头部等于节点
            node.next = node # 设置节点的下一个指向自身
        else:
            cur = self.__head # 设置游标为头部
            while cur.next != self.__head: # 如果当前所指向的节点的下一元素不是头部
                cur = cur.next  # 移动游标
            node.next = self.__head # 退出循环后，设置添加的节点的下一个指向为原来头部
            cur.next = node # 设置最后一个节点的指向为添加的节点

    def insert(self, pos, item):
        """指定位置添加元素
            pos：位置坐标
        """
        if pos <= 0: # 如果要插入的位置小于0
            self.add(item) # 在头部添加就好
        elif pos > (self.length()-1): # 如果要插入的位置大于链表的长度
            self.append(item) # 尾部添加就好
        else:
            pre = self.__head # 创建一个游标指向节点头部
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
        if self.is_empty():
            return
        cur = self.__head # 创建一个游标指向节点头部
        pre = None # 设置一个当前角标的前一个角标变量
        while cur.next != self.__head: # 遍历（如果当前角标不是最后一个）
            if cur.elem == item: # 找到了
                # 先判断此节点是否是头节点
                if cur == self.__head: # 是头节点
                    rear = self.__head # 定义一个变量用于找尾结点，首选指向头部从头找
                    while rear.next != self.__head: # 判断如果下一个不是头部（就是说当前不是最后一个时）
                        rear = rear.next # 移动角标
                    self.__head = cur.next # 设置头节点指向下一个元素
                    rear.next = self.__head # 设置尾结点的下一个指向头部
                else: # 中间节点
                    pre.next = cur.next # 设置前一个元素的下一个元素指向，当前查找到的元素的下一个元素（这样就把当前元素给抛弃了）
                    return
            else: # 没有找到
                pre = cur # 设置前一个角标为现在元素的角标（就是向后移动一个位置）
                cur = cur.next # 设置当前的角标为下一个元素的位置
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head: # 如果当前的指向就是头部
                # 链表只用一个节点
                self.__head = None # 设置头部指向None（就把当前的节点删除了）
            else:
                pre.next = self.__head # 不是头部时，设置前一个节点的下一个指向为头部（这样就把当前节点给抛弃了）

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head # 设置一个变量表示当前角标指向头部
        while cur.next != self.__head: # 遍历（如果当前角标不是指向最后一个）
            if cur.elem == item: # 如果找到了
                return True # 返回True
            else: # 没有找到
                cur = cur.next # 移动角标
        # 退出循环，cur指向尾节点
        if cur.elem == item: # 如果尾结点是要查找的元素
            return True
        return False # 遍历完成后没有找到返回False


if __name__ == "__main__":
    ll = SingleCycleLinkList()
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