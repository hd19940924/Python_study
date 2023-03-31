# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/27 15:17
# @filename :locust_test.py
# 开发工具 ：PyCharm
from locust import TaskSet,task,HttpUser,HttpLocust
class Locust_demo(TaskSet):
    @task()
    def getBaidu(self):
        self.client.get(url="/", verify=False)
class websitUser(HttpUser):
     tasks = [Locust_demo]
     min_wait = 3000  # 单位为毫秒
     max_wait = 6000  # 单位为毫秒

if __name__ == "__main__":
     import os
     os.system("locust -f locust_test.py --host=https://www.baidu.com")