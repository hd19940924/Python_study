# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/27 15:35
# @filename :community_test.py
# 开发工具 ：PyCharm
from locust import TaskSet,task,HttpUser
import requests
import json

class test_findHomeGoods(TaskSet):
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，
    @task()
    def findHomeGoods(self):
        # 定义requests的请求头
        url = "https://www.jianyundata.cn/community-dev/api/search/findHomeGoods"

        payload = {"type": 2}
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjAzMjI1MTcyMjc2NDQ1MTg2IiwiY3JlYXRlZCI6MTY3NzQ4MTc4MjI4NywiZXhwIjoxNjc4MDg2NTgyfQ.zv9lPMfIAaivfmP-JImoFn7oUojNwYhaoV1wwqRwktIcBI-NVxs5Yk5san3IIJ3sgvJN0B9f1ztoZJMDaudPNQ"}
        # r是包含所有响应内容的一个对象
        r = self.client.post("/community/api/search/findHomeGoods", json=payload, timeout=30, headers=headers)
        # 这里可以使用assert断言请求是否正确，也可以使用if判断
        assert r.status_code == 200


# 这个类类似设置性能测试，继承HttpLocust
class websitUser(HttpUser):
    # 指向一个上面定义的用户行为类
    tasks = [test_findHomeGoods]
    # 执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
    min_wait = 3000
    max_wait = 6000


if __name__ == "__main__":
     import os
     os.system("locust -f community_test.py --host=https://www.hurdcloud.cn")
