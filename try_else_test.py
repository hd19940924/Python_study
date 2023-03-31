# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 15:23
# @filename :try_else_test.py
# 开发工具 ：PyCharm
try:
  age=int(input("请输入"))
  score=int(input("请输入"))
  s=age/score
except ValueError:
    print("invalid literal for int() with ")
except ZeroDivisionError:
    print("除数不能为0")
except BaseException as e:
    print("出错了")
    print(e)
else:
    print(s)