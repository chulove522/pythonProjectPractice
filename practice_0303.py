import pandas as pd
import numpy as np
import math
from datetime import date


class Practice0303:
    a = b = 1
    c = 'testc'

    def __init__(self):
        print("開始執行")

    s = ['a', 'b', 'c', 'd']

    # str1 = "s[0] + s[1] + s[2] + s[3]\n"
    str1 = ""
    str1 = str1.join(s)
    print(str1)

    # Write a Python program to convert a list of characters into a string.
    my_string = "isaac"
    print(len(my_string))

    def practiceLickyNumber(self):
        b = input()
        s1 = int(b[0]) + int(b[1]) + int(b[2])
        s2 = int(b[-1]) + int(b[-2]) + int(b[-3])
        # 居然可以用負號代表末端的內容
        if s1 == s2:
            print("lucky number")
        else:
            print("regular number")

    def printthedifference(self):
        b = input()
        s1 = int(b[0]) + int(b[1]) + int(b[2])
        s2 = int(b[-1]) + int(b[-2]) + int(b[-3])
        if s1 == s2:
            print("lucky number")
        else:
            print("regular number")

    # printthedifference(1)
    str = "-"
    seq = ("a", "b", "c")  # 字符串序列
    print(str.join(seq))  # a-b-c

    # Python
    # 元组
    # Python的元组与列表类似，不同之处在于元组的元素不能修改。
    #
    # 元组使用小括号，列表使用方括号。
    #
    # 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"

    # Python
    # 字典(Dictionary)
    # 字典是另一种可变容器模型，且可存储任意类型对象。
    #
    # 字典的每个键值
    # key = > value
    # 对用冒号: 分割，每个键值对之间用逗号, 分割
    d = {"key1": "value1", "key2": "value2"}


class PracticeTheMath:

    def trianglearea(self):
        # Heron's Formula - area of a triangle
        Heron = []
        i = 0
        s = 0
        while (i <= 2):
            Heron.append(int(input()))
            s += Heron[i]
            i += 1
        s = s / 2
        s = (s * (s - Heron[0]) * (s - Heron[1]) * (s - Heron[2])) ** 0.5
        print(s)

    # trianglearea(1)

    def printtheprimes(self):
        i = 2
        while i < 100:
            j = 2
            while j <= math.sqrt(i):
                if i % j == 0:
                    break
                j = j + 1
            if j > math.sqrt(i):
                print(i)
            i = i + 1
        # end

    def isaprime(self):
        isPrime = True
        print("請輸入一個數字判定是為質數")
        s = int(input())
        if s >= 2:
            j = 2
            while j <= math.sqrt(s):
                if s % j == 0:
                    isPrime = False
                    break
                else:
                    j = j + 1
        print(isPrime)
        # end

    # printtheprimes(1)
    # isaprime(1)


class Practice02:
    def slicing(self):
        mylist = ['a', 'p', 'p', 'l', 'e']
        print(mylist[2:5])
        print(mylist[:4])
        print(mylist[1:])
        print(mylist[:])
        print(mylist)

        # Use del toDeleteelementsfrom a list
        my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
        # delete 3th item
        del my_list[2]
        # my_list.remove('o')
        print(my_list)
        # delete multiple items from 2th to 4th(including 4th)
        del my_list[1:5]
        print(my_list)

        d = {0: 10, 1: 20}
        print(d)
        d.update({2: 30})
        # d[2]= 30

        print(d)

    slicing(1)
