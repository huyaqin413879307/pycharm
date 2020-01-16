from selenium import webdriver
browser = webdriver.Chrome(r'C:\Python34\chromedriver_win32\chromedriver.exe')
url_jdf='https://finance.sina.com.cn/realstock/company/sz000725/nc.shtml'
browser.get(url_jdf)
price=browser.find_element_by_id('price')
print(price.text)
name=browser.find_element_by_class_name('c8_name')
print(name.text)