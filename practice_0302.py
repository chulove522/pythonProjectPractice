import pandas as pd
import numpy as np
from datetime import date

class Practice0302:
    def __init__(self, setting =0):
        self.setting = setting
        self.weather = "sunny"
        if self.setting==0:
            exit()
    def trunOn(self):
        self.setting = 1
    def status(self):
        if self.setting == 1:
            return 1
        else:
            return 0
    def thedictionary(self):
        alphabet = dict(
            a="apple",
            b="ball",
            c="cat",
            d="dog",
            e="elephant",
            f="frog"
        )

        print(alphabet["a"])

        alphabet["f"] = "frog"
        alphabet["a"] = "ant"

        print(alphabet["a"])
        print(alphabet)
        print(alphabet["b"])

    def theNames(self):
        data = {'uid':[1,2,3,4,5],
                'name':['Howard','Lily','Kai',
                        'Jojo','Ivan'],
                'age':[25,21,35,18,15]}
        print('\n',(data))

        print('\n',pd.DataFrame(data))

        member = pd.DataFrame(data)

        member

        member.head()

        member.shape

        member['age'].mean()

        member.info()
    #theNames(1)

    def theTestfunc(name, id):
        print('name',name,'id',id)
    theTestfunc('hello',100)

    def applog(name, funcname, date="2022/03/02"):
        print(f"{name} use the {funcname} on {date}")

    applog(name="mike",funcname="running")

    def manyinfos(*info):
        print(info)
    manyinfos("mike","nam","fog","home")

    def manyinfos02(**info):
        print(info)
    manyinfos02(name="mike",id=100,date=date.today())

    def printTheDateToday(self):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        d2 = today.strftime("%d/%m/%y")
        d3 = today.strftime("%m/%d/%y")
        d4 = today.strftime("%b-%d-%Y")
        print(d1)
        print(d2)
        print(d3)
        print(d4)

    #printTheDateToday(1)

    def printGroup(self):
        this_group = "Big Data"
        current_ttl_articles = 4
        is_participating = True

        my_status = [this_group, current_ttl_articles, is_participating]

        print(type(my_status[0]))
        print(type(my_status[1]))
        print(type(my_status[2]))
        print(my_status)

    printGroup(0);
    print("hello")

    class student:
        def __init__(self,name):
            self.name = name
            print("正在構造學生",name)
        def study(self):
            print(self.name,"正在讀書")
    mina = student("mina")
    mina.study()