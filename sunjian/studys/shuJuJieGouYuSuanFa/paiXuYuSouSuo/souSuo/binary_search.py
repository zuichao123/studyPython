# coding:utf-8
"""
    二分法查找
        只能用于排序后的顺序表

        最优时间复杂度：O(1)
        最坏时间复杂度：O(logn)
"""

def binary_search(alist, item):
    """递归方式"""
    n = len(alist) # 列表长度
    if n > 0:
        mid = n // 2 # 中间值
        if alist[mid] == item: # 找到
            return True
        elif item < alist[mid]: # 要找的值小于中间的值
            return binary_search(alist[:mid], item) # 递归调用，在左边继续找
        elif item > alist[mid]: # 大于中间
            return binary_search(alist[mid+1:], item)
    return False

def binary_search2(alist, item):
    """非递归方式"""
    n = len(alist) # 列表长度
    first = 0 # 第一个角标
    last = n - 1 # 最后一个
    while first <= last:
        mid = (first + last) // 2 # 中间值
        if alist[mid] == item: # 如果中间就是要查找的
            return True
        elif alist[mid] > item: # 如果中间的值大于要找的
            last = mid - 1 # 设置最后一个角标设置为中间的-1
        else:
            first = mid + 1 # 设置第一个角标为中间的+1
    return False


if __name__ == "__main__":
    alist = [2, 11, 33, 44, 44, 66, 77, 777, 4455, 8888]
    print(binary_search(alist, 777))
    print(binary_search(alist, 7777))

    print(binary_search2(alist, 777))
    print(binary_search2(alist, 7777))