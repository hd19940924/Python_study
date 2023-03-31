# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/27 17:08
# @filename :score_test.py
# 开发工具 ：PyCharm
try:
    score=int(input("请输入你的成绩："))
    if 0<=score<=100:
       print("分数是，",score)
    else:
       raise Exception("分数不正确")
except Exception as e:
    print(e)
