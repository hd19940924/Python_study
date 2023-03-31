# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/24 15:47
# @filename :count_test.py
# 开发工具 ：PyCharm
def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
    return count
def star():
    for i in range(4):
        for j in range(4):
            print("*",end="")
        print()
if __name__=="__main__":
    s="hhhyyyygffrrrd"
    ch=input("请输入要统计的字符串：")
    count=get_count(s,ch,)
    print("{0}在{1}出现了{2}次".format(ch,s,count))
    star()