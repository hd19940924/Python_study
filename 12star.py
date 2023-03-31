# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/24 14:16
# @filename :12star.py
# 开发工具 ：PyCharm
lis1=["白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座","水瓶座","双鱼座"]
lis2=["细狗","细狗","细狗","细狗","细狗","细狗","细狗","细狗","细狗","细狗","细狗","细狗"]
d1=dict(zip(lis1,lis2))
print(d1)
flag=True
key=input("请输入您的星座名称：")
for item in d1:
    if key==item:
        flag = True
        print(key,"的性格特点为：",d1.get(key))
        break
    else:
        flag=False
    """else:
        print("输入星座错误")
        break"""
if not flag:
     print("对不起，您输入的星座错误")

