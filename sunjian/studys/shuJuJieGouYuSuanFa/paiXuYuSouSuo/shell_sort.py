# coding:utf-8
"""
    希尔排序
        是插入排序的升级
        不稳定
"""
def shell_sort(alist):
    n = len(alist) # 列表的长度
    gap = n // 2 # 长度折半，步长
    # 步长变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法，与普通的插入算法的区别是：gap步长
        for j in range(gap, n): # j = [gap,gap+1,gap+2,...n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2


if __name__ == "__main__":
    alist = [11,2,44,777,33,4455,66,77,44,8888]
    print(alist)
    shell_sort(alist)
    print(alist)

