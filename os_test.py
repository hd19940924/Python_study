# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/22 16:47
# @filename :os_test.py
# 开发工具 ：PyCharm
import os
#os.system("notepad.exe")
#os.system("calc.exe")
#os.startfile()
print(os.getcwd())
print(os.listdir(r"C:\Users\admin\PycharmProjects\Python_study"))
#os.mkdir("tt")
#os.rmdir("tt")
print(os.path.abspath("os_test.py"))
print(os.path.exists("ggg"))
print(os.path.exists("os_test.py"))