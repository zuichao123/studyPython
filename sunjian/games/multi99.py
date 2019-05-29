# coding:utf-8

def mutil():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            # if j < 2:
            #     print("%d*%d=%d\t" % (j, i, i * j), end="")
            # else:
            print("%d*%d=%d\t" % (j, i, i * j), end="")
            j += 1
        print("")
        i += 1

mutil()
print('-'*88)

def three_type():
    i = 1
    while i <= 9:
        '''
        #从键盘中输入一个值,这个值用来控制这行中*的个数
        num = int(input("请输入这个行里的*的个数:"))
        j = 1
        while j<=num:
            print("*", end="")
            j+=1
        '''
        j = 1
        while j <= i:
            print("* ", end="")
            j += 1
        print("")
        i += 1

three_type()
print('-'*88)

def ju_type():
    i = 1
    # 用来控制行数
    while i <= 5:
        # 用来控制每一行中的列数
        j = 1
        while j <= 5:
            print("*", end="")
            # j = j+1#c语言中向让j加上1的方式: j++;    ++j;   j+=1;  j=j+1;
            j += 1
        print("")
        i = i + 1

ju_type()
