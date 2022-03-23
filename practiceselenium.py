from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import pandas as pd
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # 定位元素主要应用于一个过滤器

# By所支持的定位器的分类：
#
# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link text'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'
# ————————————————
# 原文链接：https://blog.csdn.net/gufenchen/article/details/98056959

path = r"C:\Users\chulove\chromedriver"
# s = Service(path+"\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

e = Service(path + "\msedgedriver.exe")
driver = webdriver.Edge(service=e)


# 抓取資訊
def func01():
    driver.get("https://tw.appledaily.com/new/realtime")
    time.sleep(1)

    ## 瀏覽器名稱
    print(driver.name)
    print('===============')

    ## 網頁標題
    print(driver.title)
    print('===============')

    ## URL位置
    print(driver.current_url)
    print('===============')

    ## 連線Browser Id
    print(driver.session_id)
    print('===============')

    ## 瀏覽器功能設定選項
    print(driver.capabilities)
    print('===============')

    ## 目標網頁原始碼
    print(driver.page_source)
    print('===============')
    driver.close()


# 移動網框
def func02():
    ## 獲得初始化位置(左上角位置)
    print(driver.get_window_position())
    time.sleep(1)
    ## 設定初始化位置
    print(driver.set_window_position(100, 100))
    time.sleep(1)
    ## 獲得視窗大小
    print(driver.get_window_size())
    time.sleep(1)
    ## 設定視窗大小
    print(driver.set_window_size(1000, 1000))
    time.sleep(1)
    ## 視窗最大化
    driver.maximize_window()
    time.sleep(1)
    ## 視窗最小化
    driver.minimize_window()
    time.sleep(1)
    ## 模擬視窗最小化
    driver.set_window_position(-3000, 0)
    time.sleep(1)
    ## 復原視窗大小
    driver.set_window_position(0, 0)
    time.sleep(1)

    driver.close()


# 把結果存在表格
def func03():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    res = requests.get(url)
    data_list = res.json()

    # 將資料轉 pd.DataFrame類型
    df = pd.DataFrame(data_list)
    print(df.head())

    df.to_csv('result.csv', encoding='utf-8-sig')


# func03()

# 網頁截圖
def func04():
    url = "https://statementdog.com"

    driver.get(url)
    time.sleep(2)

    driver.save_screenshot("./test.png")


# func04()
def func05():
    pattern = "a+b*c"
    string = "aabc , ac , aabbccc abb , dd"
    match = re.findall(pattern, string)
    print(match)

    p2 = "[dor]mit"
    string2 = "admit, commit , emit , omit , permit"
    match02 = re.findall(p2, string2)
    print(match02)

    mysting = "beautiful"
    print(mysting[2::2])


def func06():
    driver.get('https://google.com')

    # class ="gLFyf gsfi" name="q" type="text"
    # locate the search box element
    #search_box = driver.find_element_by_name('q') # DeprecationWarning
    classname = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
    search_box = driver.find_element(By.NAME, 'q')
    input = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    classname.send_keys("依照class名")
    time.sleep(1)
    search_box.send_keys("依照搜尋框")
    time.sleep(1)
    input.send_keys("依照Xpath")
    time.sleep(1)
    # search_box.send_keys('Selenium' + Keys.RETURN)


func06()
driver.close()
