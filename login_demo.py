# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/23 11:41
# @filename :login_demo.py
# 开发工具 ：PyCharm
for i in range(3):
    qq = input("请输入QQ号：")
    pwd = input("请输入密码：")

    if qq == "234" and pwd == "123":
        print("登录成功")
    else:
        print("用户名或密码有误，登录失败！,你还有{}次机会".format(2 - i))
