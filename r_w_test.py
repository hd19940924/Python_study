# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/23 10:11
# @filename :r_w_test.py
# 开发工具 ：PyCharm
fp=open(r"C:\soft\hello.txt","a+")
#print("hello,world",file=fp)
fp.write("hello,world")
fp.close()
with open(r"C:\soft\hello.txt","a+") as f:
    f.write("llll")
print(bin(8))
print(oct(8))
print(hex(8))
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))

print("hi,{0}".format("bob"))
print("f")
pwd=input("请输入密码：")
if pwd.isdigit():
       print("输入数据合法")

else:
       print("输入数据不合法")
print("-------------------------------")
print("输入数据合法" if pwd.isdigit() else "输入数据不合法" )
