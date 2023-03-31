# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/3/29 15:01
# @filename :test_py001.py
# 开发工具 ：PyCharm
import pytest
@pytest.fixture(scope="function",autouse=True)
def login():
    print("login in")
    return 2
class Test_py001:
    def test_insert(self,login):
        print("insert")
        assert login>3
    def test_delete(self):
        print("delete")
if __name__=="__main__":
    pytest.main(["-s","test_py001.py"])