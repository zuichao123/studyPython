# coding:utf-8
"""
    插入排序
        稳定
"""
def insert_sort(alist):
    for j in range(1, len(alist)): # j代表需要比对的【1---len(alist)-1】
        i = j # i代表内存循环起始值
        while i > 0: # 遍历列表
            if alist[i] < alist[i-1]: # 判断如果当前的元素小于它前边的元素
                alist[i], alist[i-1] = alist[i-1], alist[i] # 交换位置
                i -= 1
            else: # 如果当前的大于前一个，就不用了交换了
                break # 结束本次，继续下次

if __name__ == "__main__":
    alist = [11,2,33,4455,66,77,44,777,44,8888]
    print(alist)
    insert_sort(alist)
    print(alist)