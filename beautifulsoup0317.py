# https://www.nkust.edu.tw/
import requests
import json
import re
from bs4 import BeautifulSoup

response_school = requests.get('https://www.nkust.edu.tw/')

response_school.encoding = 'uft-8'

response_isaac = requests.get("https://isaac60103.github.io/crawl_course/example/beautifulsoup_example.html")
response_isaac.encoding = 'utf-8'



payload = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": "BanQiao",
    "EndStation": "ZhangHua",
    "OutWardSearchDate": "2022/03/17",
    "OutWardSearchTime": "14:30",
    "ReturnSearchDate": "2022/03/17",
    "ReturnSearchTime": "14:30",
    "DiscountType": ""
}


def printtheschool():
    print('status code: {}'.format(response_school.status_code))
    # print('response html is {}'.format(response.text))

    # 超長就不show了

    # use beautifulsoup to analyze html
    soup = BeautifulSoup(response_school.text, 'html.parser')
    print('find the first li tag')
    print(soup.find("li"))

    print('show the first h2 tag content')
    if (soup.find("h2") != " "):
        print(soup.find("h2").text)
    else:
        print("沒有找到h2")
    # 沒有
    print('find the first td tag')
    print(soup.find("td"))
    print('find all li tag')
    print(soup.find_all("li"))


def showteacher():
    # use beautifulsoup to analyze html
    soup = BeautifulSoup(response_isaac.text, 'html.parser')
    print('show the first div tag with id=id1')
    print(soup.find("div", {"id": "id1"}))
    print('find all tag with text= hello_python')
    print(soup.find_all(text="hello_python"))


def findticket():
    response_train = requests.post("https://www.thsrc.com.tw/TimeTable/Search", data=payload)
    traintable = json.loads(response_train.text)

    # "startStation" endStation
    # print('select the start station BanQiao')
    # start = soup.find(text="select_location01")
    # #start.
    # print('show the end station ZhangHua')
    # end = soup.find(text="select_location02")
    for i in traintable['data']['DepartureTable']['TrainItem']:
        print(i)  #所有資料都印
    for i in traintable['data']['DepartureTable']['TrainItem']:
        print("{},{},{}".format(i['TrainNumber'],i['DepartureTime'],i['DestinationTime']))

#findticket()

def printmatch():
    pattern ="信義"
    taipeirequests= requests.get("https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E7%AB%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1%E5%88%97%E8%A1%A8",'html.parser')
    taipeisoup = BeautifulSoup(taipeirequests.text, 'html.parser')
    result = taipeisoup.find_all("td")
    for td in result:
        if pattern in str(td.text):
            print("包含信義的結果有{}".format(td.text))

printmatch()
