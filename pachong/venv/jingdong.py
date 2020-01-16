import requests
url = "https://finance.sina.com.cn/realstock/company/sz000725/nc.shtml"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1:1000])
except:
    print("爬取失败")