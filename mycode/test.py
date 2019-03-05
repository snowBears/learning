# _*_ coding:utf-8 _*_
# x=input("输入number:")
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError("snow has dinner")
#     if x >=0:
#         return x
#     else:
#         return -x
# y=my_abs(x)
# print(y)


import unittest
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
import time


class Test(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        time.sleep(1)
        print("结束")

    def test01(self):
        print("01测试")

    def test02(self):
        print("02测试")

    def testAdd(self):
        print("Add方法")

    def test03(self):
        print("03测试")


if __name__ == '__main__':
    unittest.main()


