# _author:{Administrator}
# date:{2020/12/18}

import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# from fake_useragent import UserAgent


url = "https://www.bilibili.com/v/douga/?spm_id_from=333.851.b_7072696d6172794368616e6e656c4d656e75.1"
driver = webdriver.Chrome()
driver.get(url)
elements = driver.find_elements_by_xpath('//div[@class="spread-module"]//p[@class="t"]')
#element =  driver.find_element_by_xpath('//*[@id="douga_mad"]/div[2]/div[1]/div[2]/div[1]/a/p[1]')
#print(elements.text)

for data in elements:
    print("==" * 8)
    print(data.text)
#driver.quit()
