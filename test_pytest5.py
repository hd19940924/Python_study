# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 13:05
# @filename :test_pytest5.py
# 开发工具 ：PyCharm
import allure
import pytest
import os
@pytest.fixture()

def begin():
    print("begin")
    return "begin"
@allure.feature("开始测试")
def test_then(begin):
    print("then")
    print(begin)
@allure.feature("继续测试")
def test_next(begin):
    print("next")
    print(begin)
"""@pytest.mark.usefixtures("begin")
class Test_ABC:
    def run(self):
        print("run")"""
#if __name__=="__main__":
   # pytest.main(["-s","test_pytest5.py"])
if __name__ == '__main__':   # pytest运行模式
    pytest.main(['-vs',"--alluredir=./temp","test_pytest5.py"])  #生成json数据，生成后可以在temp文件查看
    os.system('allure generate ./temp -o ./reportnew/ --clean') #将json数据生成，报告存至report文件
