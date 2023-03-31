# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 10:21
# @filename :test_pytest2.py
# 开发工具 ：PyCharm
import allure
import pytest
@pytest.fixture() # fixture标记的函数可以应用于测试类外部
def before():
    print("------->before")
@pytest.mark.usefixtures("before")
@allure.feature("")
class Test_ABC:
    @allure.story("")
    def setup(self):
        print("------->setup")
    def test_a(self):
        print("------->test_a")
        assert 1
if __name__ == '__main__':
    pytest.main(["-s",  "test_pytest2.py"])

