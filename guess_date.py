# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/23 11:50
# @filename :guess_date.py
# 开发工具 ：PyCharm
import random
r=random.randint(1,100)
print("---------------------------------------")
print("游戏开始")
for i in range(1,11):
    id=int(input("请输入一个数："))
    if id<r:
        print("猜小了")
    elif id>r:
        print("猜大了")
    else:
        print("恭喜你！")
        break
print("您一共猜了{0}次".format(i))
if i<3:
    print("你真聪明")
elif i<7:
    print("继续努力啊！！")
else:
    print("行不行啊，细狗！")
print("----------------------------------------")
print("游戏结束")