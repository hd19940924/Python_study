# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/23 14:46
# @filename :year_test.py
# 开发工具 ：PyCharm
year=[82,84,85,80,90,87,00]
print("原列表：",year)
ll=[]
for index,values in enumerate(year):
    #print(index,values)
    if values!=0:
        #print(values)
        print("19"+str(values))
        hh="19"+str(values)
        ll.append(hh)
print(ll)