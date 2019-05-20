# coding:utf-8
"""
    二叉树
"""

class Node(object):
    """"""
    def __init__(self, item):
        self.elem = item # 元素
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item) # 实例一个节点元素
        if self.root is None: # 如果根节点是None
            self.root = node # 设置元素为根节点
            return
        queue = [self.root] # 队列
        while queue: # 如果队列不为空
            cur_node = queue.pop(0) # 设置队列第一个元素为当前节点
            if cur_node.lchild is None: # 如果当前节点元素的左孩子为None
                cur_node.lchild = node # 将该节点设置为当前节点的左孩子
                return
            else:
                queue.append(cur_node.lchild) # 如果当前节点的左孩子不为None，将左孩子追加到队列中
            if cur_node.rchild is None: # 如果当前节点的右孩子为None
                cur_node.rchild = node # 将该节点设置为当前节点的右孩子
                return
            else:
                queue.append(cur_node.rchild) # 如果当前节点的右孩子不为None，将该右孩子追加到队列中

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root] # 队列（将根节点添加到队列）
        while queue:
            cur_node = queue.pop(0) # 设置队列中的第一个元素（根节点）为当前节点
            print(cur_node.elem, end="  ")
            if cur_node.lchild is not None: # 如果当前节点的左孩子不是None
                queue.append(cur_node.lchild) # 追加到队列中
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild) # 同理

    def preorder(self, node):
        """先序遍历---根、左、右"""
        if node is None:
            return
        print(node.elem, end="  ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历---左、根、右"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历---左、右、根"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")