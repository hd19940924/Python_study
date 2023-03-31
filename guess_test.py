# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/27 10:23
# @filename :guess_test.py
# 开发工具 ：PyCharm
import random
def guess(num,guess_num):
    if num==guess_num:
        return  0
    elif guess_num>num:
        return  1
    else:
        return -1
num=random.randint(1,100)
for i in range(1,10):
    guess_num=int(input("请输入你心里的数："))
    result=guess(num,guess_num)
    if result==0:
        print("猜对了")
        break
    elif result==1:
        print("猜小了")
    else :
        print("猜小了")
else:
 print("您已猜错10次，游戏结束!")


