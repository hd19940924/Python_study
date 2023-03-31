# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/27 16:50
# @filename :quene_test.py
# 开发工具 ：PyCharm
import queue
queue_list = queue.Queue()
for i in range(1, 10):
        queue_list.put_nowait(i)

print(queue_list)
def get_root(self):
   if not self.parent.queue_list.empty():
            data = self.parent.queue_list.get()
            print("queue data:{}".format(data))
            response = self.client.get('',name='get_root')
dd=get_root()
print(dd)
