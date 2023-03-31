# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/30 14:59
# @filename :tets.yaml.py
# 开发工具 ：PyCharm
# test-yaml.py内容
import os
import yaml

data=[1,2,3]
#data2={"name":"tom","sex":"男"}
# python3.6
data3={
"user": "admin",
"psw": "123456",
}
class Yamlutil:
    # 读取yaml文件
    def read_yaml(self):
        with open(os.getcwd() + "\\test.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
    def write_yaml(self):
        with open(os.getcwd() + "\\test.yaml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data3,stream=f,allow_unicode=True)

if __name__ == '__main__':
    result=Yamlutil().read_yaml()
    Yamlutil().write_yaml()
    print(result)

