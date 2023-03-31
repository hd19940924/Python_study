# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 9:28
# @filename :test_pytest.py
# 开发工具 ：PyCharm
import pytest
class Test_ABC:
    @pytest.fixture( )#变量调用
    def before(self):
        print("------->before")
        return "success"
    def test_a(self,before): # ️ test_a方法传入了被fixture标识的函数，已变量的形式
        print("------->test_a")
        print(before)
       # print(before())
        assert 1
if __name__ == '__main__':
    pytest.main(["-s","test_pytest.py"])
