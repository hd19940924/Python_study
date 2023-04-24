
import re
import requests
import xlwt
import xlrd
import os
def test():
    url4='https://www.mainchance.net/yueshu/'

    url='https://www.mainchance.net/yueshu/92312996565/'

    url2=re.findall('https://www.mainchance.net/yueshu/(.*?)/',url)[0]

    req=requests.get(url)

    req.encoding='gbk'

    shuming=re.findall('<h1>(.*?)</h1>',req.text)[0]

    mulu=re.findall('.html">(.*?)</ a></li>',req.text,re.S)
#print(len(mulu))
    for i in range(11,len(mulu)):
     print(mulu[i])

    wangzhi = re.findall(f'< a href="/yueshu/{url2}/(.*?).html">', req.text,re.S)
    for i in range (11,len(wangzhi)):
       print(f'{url4}{url2}/{wangzhi[i]}.html')
    dict1={}
    for i in range(11,len(mulu)):
        dict1[mulu[i]]=f'{url4}{url2}/{wangzhi[i]}.html'
    for k,v in dict1.items():
       print(k,v)
test()

