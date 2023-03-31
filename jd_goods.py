# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/24 11:04
# @filename :jd_goods.py
# 开发工具 ：PyCharm
lis=[]
for i in range(0,5):
    goods=input("请输入商品编号和商品名称，每次只能入库一件商品：\n")
    lis.append(goods)
for item in lis:
    print(item)
cart=[]
while True:
    num=input("请输入你想要的商品编号：")
    for item in lis:
        if item.find(num)!=-1:
            cart.append(item)
            break
    if num=="q":
            break
print("你购物车的商品是：")
for m in cart:
    print(m)
for i in range(len(cart)-1,-1,-1):
    print(cart[i])