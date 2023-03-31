# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 11:03
# @filename :test_pytest3.py
# 开发工具 ：PyCharm
import pytest
#@pytest.fixture(scope='function', autouse=True)
@pytest.fixture(scope='class', autouse=True)

def login():
    print('登录系统')

@pytest.mark.xfail(2 > 1, reason="标注为预期失败") # 标记为预期失败函数test_b
def test_01():
    print('测试用例一')
class TestCase:
    @pytest.mark.skip()
    def test_03(self):
        print('测试用例三')
    @pytest.mark.skipif(condition=2>1,reason="跳过")
    def test04(self):
        print('测试用例四')

if __name__ == '__main__':
     pytest.main(["-s","test_pytest3.py"])

