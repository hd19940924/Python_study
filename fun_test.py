# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 13:58
# @filename :fun_test.py
# 开发工具 ：PyCharm
"""def func_test(a,b):
     s=a+b
     return s
print(func_test(1,4))
print(func_test(a=1,b=4))
print(func_test(b=1,a=4))

def func1_test(a,b=10):
    s=a+b
    return s
print(func1_test(a=10,b=1))
print(func1_test(a=10))
def arg_test(*args):
    print(args)
arg_test(10)
arg_test(10,20)
def args_test(**args):
    print(args)
args_test(a=10,b=9)
print()
def args_test1(**kwargs):
    print(kwargs)
args_test1(a=9,b="jj")
def args_test2(*args,**kwargs):
    print(args,kwargs)
args_test2(1,a=10)"""
"""try:
     age=input()
     if age>18:
         print("your are adult")
     else:
         print("666")
except:
    print(7777)"""
try:
  age=int(input("请输入"))
  score=int(input("请输入"))
  s=age/score
  print(s)
except ValueError:
    print("invalid literal for int() with ")
except ZeroDivisionError:
    print("除数不能为0")
except BaseException as e:
    print(e)
print("gg")

try:
  age=int(input("请输入"))
  score=int(input("请输入"))
  s=age/score
  print(s)
except :
    print("invalid literal for int()")
print("gg")
try:
  age=int(input("请输入"))
  score=int(input("请输入"))
  s=age/score
  print(s)
except :
    print("invalid literal for int() ")
finally:
    print(666)
