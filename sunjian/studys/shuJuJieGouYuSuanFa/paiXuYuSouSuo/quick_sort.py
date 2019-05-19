# coding:utf-8
"""
    快速排序
        不稳定

    注意：这个必须会

    常见排序算法效率比较
        排序方法        平均情况            最后情况        最坏情况        辅助空间        稳定性
        冒泡排序        O(n2)               O(n)            O(n2)           O(1)            稳定
        选择排序        O(n2)               O(n2)           O(n2)           O(1)            不稳定
        插入排序        O(n2)               O(n)            O(n2)           O(1)            稳定
        希尔排序        O(n long n)~ O(n2)  O(n1.3)         O(n2)           O(1)            不稳定
        堆排序          O(n log n)          O(n log n)      O(n log n)      O(1)            不稳定
        归并排序        O(n log n)          O(n log n)      O(n log n)      O(n)            稳定
        快速排序        O(n log n)          O(n log n)      O(n2)           O(log n)~ O(n)  不稳定
"""

def quick_sort(alist, first, last):
    if first >= last: # 如果开始位置大于或等于结束
        return
    mid_value = alist[first] # 开始时设置第一个为中间
    low = first # 最小角标
    hight = last # 最大角标

    while low < hight:
        while low < hight and alist[hight] >= mid_value: # 如果最后一个值大于等于中间值
            hight -= 1 # 向前移动最大角标
        alist[low] = alist[hight] # 退出循环，表示hight处的值小于中间值；so将最大角标处的值与最小角标处的值交换

        while low < hight and alist[low] < mid_value: # 如果最小角标的值小于中间值
            low += 1 # 不用交换，向后移动角标
        alist[hight] = alist[low] # 同理，交换最大值和最小值
    # 退出循环时，low==hight
    alist[low] = mid_value # 设置最小角标指向中间值

    # 然后
    # 对low左边的列表继续进行快排
    quick_sort(alist, first, low-1)

    # 对low右边的列表继续进行快排
    quick_sort(alist, low+1, last)


if __name__ == "__main__":
    alist = [11,2,44,777,33,4455,66,77,44,8888]
    print(alist)
    quick_sort(alist, 0, len(alist)-1)
    print(alist)