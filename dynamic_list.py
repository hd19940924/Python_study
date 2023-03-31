# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/24 17:13
# @filename :dynamic_list.py
# 开发工具 ：PyCharm
lst=[["01","电风扇","美的",600],["02","电视机","乐视",6000],["03","电冰箱","格力",3600]]
print("编号\t\t名称\t\t品牌\t\t价格")
for i in lst:
    for j in i:
        print(j,end="\t\t")
    print()
print("-------------------------------------------------------------------")
for item in lst:
    item[0]="00000"+item[0]
    item[3]="￥{:.2f}".format(item[3])
for i in lst:
    for j in i:
        print(j,end="\t\t")
    print()