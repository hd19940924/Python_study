# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 10:49
# @filename :test_autouse.py
# 开发工具 ：PyCharm
import pytest
@pytest.fixture(autouse=True) # 设置为默认运行
def before():
     print("------->before")
class Test_ABC:
    def setup(self):
         print("------->setup")
    def test_a(self):
         print("------->test_a")
         assert 1
if __name__ == '__main__':
     pytest.main(["-s","test_autouse.py"])




