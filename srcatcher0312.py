import requests

url = "https://www.books.com.tw/products/0010854043?loc=P_br_60nq68yhb_D_2aabdc_B_2"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except ConnectionError:
    print("爬取失敗")

kv = {'user-agent': 'Edge/99.0.1150.36'}
r = requests.get(url, headers=kv)
print("狀態是")
print(r.raise_for_status())


# 如果在處理過程中發生錯誤，則response.raise_for_status()返回HTTPError對象


class ExampleError(BaseException):
    pass

# b = 0
# if b == 0:
#     raise ExampleError("b==0")
