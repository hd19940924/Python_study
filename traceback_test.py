# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 15:57
# @filename :traceback_test.py
# 开发工具 ：PyCharm
import traceback
try:
  age=int(input("请输入:"))
  score=int(input("请输入:"))
  s=age/score
except :
    traceback.print_exc()
else:
    print(s)
finally:
    print("over")
print("结束了")