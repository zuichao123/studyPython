# coding:utf-8
"""
    选择排序
        不稳定
"""

def select_sort(alist):
    n = len(alist)
    for j in range(n-1): # 指0--倒数第二个
        min_index = j
        for i in  range(j+1,n): # 指j+1--倒数第一个
            if alist[min_index] > alist[i]:
                min_index = i # 交换位置，继续找最大的值
        # 找完一遍后，替换
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    alist = [11,2,33,4455,66,77,44,777,44,8888]
    print(alist)
    select_sort(alist)
    print(alist)