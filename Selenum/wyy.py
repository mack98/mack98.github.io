#_author:{Administrator}
#date:{2020/12/18}

from selenium import  webdriver

url="https://music.163.com/#/song?id=1804615128"
driver = webdriver.Chrome()
driver.get(url)
driver.switch_to.frame("g_iframe")
elements = driver.find_elements_by_xpath('//div[@class="itm"]//div[@class="cntwrap"]//div[@class="cnt f-brk"]')


for d in elements:
    print("=="*8,"\n")
    print(d.text)

#driver.quit()