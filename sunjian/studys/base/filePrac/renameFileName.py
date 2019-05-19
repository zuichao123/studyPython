#coding:utf-8
'''
    重命名文件名
'''
import os

#1. 获取要重命名的文件夹 名字
folder_name =  input("请输入要重命名的文件夹:")
file_name = input("请输入你喜欢的文件名：")

#2. 获取制定的文件夹中的所有 文件名字
file_names = os.listdir(folder_name)

# 跳入当前修改的文件路径中
os.chdir(folder_name)

#3. 重命名
i = 0
for name in file_names:
    print(name)
    old_file_name = folder_name+"/"+name
    new_file_names = old_file_name.split('.')
    new_file_name = file_name+str(i)+"."+new_file_names[1]
    i += 1

    os.rename(old_file_name, new_file_name)