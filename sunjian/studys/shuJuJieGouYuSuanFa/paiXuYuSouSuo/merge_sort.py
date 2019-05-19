# coding:utf-8
"""
    归并排序
        稳定
"""

def merge_sort(alist):
    n = len(alist) # 列表长度
    if n <= 1:
        return alist
    mid = n // 2 # 中间角标

    # left采用归并排序后形成的有序的新的zuo列表
    left_li = merge_sort(alist[:mid])

    # right采用归并排序后形成的有序的新的you列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    # merge(left,right)
    left_pointer, right_point = 0, 0 # 设置新列表的首角标
    result = [] # 结果列表

    while left_pointer < len(left_li) and right_point < len(right_li):
        if left_li[left_pointer] < right_li[right_point]: # 如果左边新列表的第一个值小于右边新列表的第一个值
            result.append(left_li[left_pointer]) # 将左边的第一个值添加到结果列表中
            left_pointer += 1 # 向后移动左边新列表的角标
        else:
            result.append(right_li[right_point])
            right_point += 1

    result += left_li[left_pointer:] # 将左边新列表的最后一个添加到结果列表中
    result += right_li[right_point:] # 同理
    return result # 返回结果列表


if __name__ == "__main__":
    alist = [11,2,44,777,33,4455,66,77,44,8888]
    print(alist)
    sorted_li = merge_sort(alist)
    print(sorted_li)