# coding:utf-8
"""
    冒泡排序
        稳定
"""

def bubble_sort(alist):
    for j in range(0,len(alist)-1):
        count = 0 # 记录是否交换了
        for i in range(0,len(alist)-1-j):
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return

if __name__ == "__main__":
    alist = [11,2,33,4455,66,77,44,777,44,8888]
    print(alist)
    bubble_sort(alist)
    print(alist)