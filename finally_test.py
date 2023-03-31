# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 15:50
# @filename :finally_test.py
# 开发工具 ：PyCharm
try:
  age=int(input("请输入:"))
  score=int(input("请输入:"))
  s=age/score
except BaseException as e:
    print("出错了")
    print(e)
else:
    print(s)
finally:
    print("over")
print("结束了")