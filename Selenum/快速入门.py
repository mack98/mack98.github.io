from selenium import  webdriver
#导入web驱动
url ="https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput="
#打开Chrome浏览器
driver=webdriver.Chrome()
driver.get(url)
#driver.quit() #退出浏览器
#driver.close() 关闭页面

#根据xpaht提取数据 find_element_by_xpath 一个数据 find_elements_by_xpath 多个数据返回的是list
elements = driver.find_elements_by_xpath('//div[@class="list_item_top"]//h3')

for e in elements:
    print(e.text)
