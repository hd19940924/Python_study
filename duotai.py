# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/22 13:39
# @filename :duotai.py
# 开发工具 ：PyCharm
class Animal(object):
    def eat(self):
        print("动物要吃东西")
class Dog(Animal):
    def eat(self):
       print("狗子要吃东西")
class Cat(Animal):
    def eat(self):
        print("喵星人要吃东西")
#print(type(Animal))#打印输出Animal对象的类型
#print(type(Dog))#
animal=Animal()
animal.eat()
dog=Dog()
dog.eat()
cat=Cat()
cat.eat()
def fun(animal):
    animal.eat()
fun(Dog())
fun(Cat())
fun(Animal())