# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/24 10:10
# @filename :find_goods.py
# 开发工具 ：PyCharm
import requests
import json

#url = "https://www.jianyundata.cn/community-dev/api/search/findHomeGoods"
url="https://www.hurdcloud.cn/community/api/search/findHomeGoods"

payload = {"type": 2}
print(type(payload))
headers = {
    "content-type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjAzMjI1MTcyMjc2NDQ1MTg2IiwiY3JlYXRlZCI6MTY3NzEzOTg1NDM2NCwiZXhwIjoxNjc3NzQ0NjU0fQ.xMb_Syf7CVgP7PNmscSYJ2-fiJeAD8TLPOTTHimPuy7g8QTq-mMMCMUja1LXyGaPApQO1a_LAB7rQaasWnuQjw"
}
headers1={
    "content-type": "application/json",
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjAzMjI1MTcyMjc2NDQ1MTg2IiwiY3JlYXRlZCI6MTY3NzQ4MTc4MjI4NywiZXhwIjoxNjc4MDg2NTgyfQ.zv9lPMfIAaivfmP-JImoFn7oUojNwYhaoV1wwqRwktIcBI-NVxs5Yk5san3IIJ3sgvJN0B9f1ztoZJMDaudPNQ"}
p=json.dumps(payload) #dict转化成json
print(type(p))
#response = requests.request("POST", url, json=payload, headers=headers)
response = requests.request("POST", url, data=p, headers=headers)
r=requests.request("POST", url, data=payload, headers=headers)
r1=requests.request("POST", url, json=payload, headers=headers)
r2=requests.request("post",url,json=payload,headers=headers1)
#r=requests.request("POST", url, data=json.loads(payload), headers=headers)
print(r2.text)
#print(response.text)
#print(r.text)
#print(r1.text)