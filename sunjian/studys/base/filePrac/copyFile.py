#coding:utf-8
'''
    复制文件
        C:\\Users\\sunjian\\Desktop\\title

        C:\\Users\\sunjian\\Desktop\\Zbpl-复件

'''
import shutil
from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):
    """完成copy一个文件的功能"""
    fr = open(oldFolderName+"/"+name, "r+") # 定义输入流，打开旧文件
    fw = open(newFolderName+"/"+name, "w+") # 定义输出流，打开新文件

    content = fr.read() # 读取旧文件内容
    fw.write(content) # 将读取的内容写入新文件

    fr.close() # 关闭输入流
    fw.close() # 关闭输出流

    queue.put(name) # 加入写队列


def main(oldFolderName):
    print(oldFolderName)
    #2. 获取old文件夹中的所有的文件名字
    fileNames = os.listdir(oldFolderName)

    #3. 使用多进程的方式copy 原文件夹中的所有文件到新的文件夹中
    pool = Pool(4) # 意为设定同时进行5个的子进程，在进程池中并行执行
    queue = Manager().Queue()

    for name in fileNames:
        #print('--------------',name)
        if os.path.isfile(oldFolderName+"\\"+name):
            print('-------------',name)
            # 非阻塞式的且支持结果返回进行回调的执行
            pool.apply_async(copyFileTask, args=(name,oldFolderName,newFolderName,queue))
        else:
            main(oldFolderName+"/"+name) # 递归

    num = 0 # 标记文件的数量
    allNum = len(fileNames) # 获取所有文件的个数
    while num<allNum: # 遍历
        queue.get() # 获取队列中的数量（就是复制后的文件个数）
        num += 1 # 标记加一
        copyRate = num/allNum # 复制的比率
        print("\rcopy的进度是:%.2f%%"%(copyRate*100), end="")
        print('fuzhile:',num,'gele')
        if num == allNum:
            break

    print("\n已完成ｃｏｐｙ.....")


if __name__ == "__main__":

    # 0. 获取永远要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字：")
    oldFolderName = oldFolderName.replace("\\",'/')

    # 1. 创建一个文件夹
    newFolderName = oldFolderName + "-复件"

    if not os.path.exists(newFolderName):  # 如果新文件夹不存在
        os.mkdir(newFolderName)  # 创建新文件夹
    else:
        shutil.rmtree(newFolderName)  # 删除之
        os.mkdir(newFolderName)  # 创建新文件夹

    main(oldFolderName)
