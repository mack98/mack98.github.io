import re
import requests
from lxml import etree
import urllib3
import os.path
import csv

#requests.packages.urllib3.disable_warnings()


url="https://maoyan.com/board/4?offset=10"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

cookies={
    'Cookie': '__mta=108418493.1608164684564.1608164684564.1608165052799.2; uuid_n_v=v1; uuid=42D090E03FFE11EB938EB13948D660ED2497CD3435CD4FCB821021F3846F2A95; _csrf=c35eac321f9b7c7713bbef010b6306e8161855866c554e9816af5aadb6a9f699; _lxsdk_cuid=1766e15b1bac8-010876c3e64ace-c791e37-144000-1766e15b1bac8; _lxsdk=42D090E03FFE11EB938EB13948D660ED2497CD3435CD4FCB821021F3846F2A95; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1608164684; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1608165052; _lxsdk_s=1766e15b1bb-a16-57c-ab8%7C%7C5'

}


#爬取 页面信息
def get_yemian(url):
    data=requests.get(url,headers=headers,cookies=cookies,verify=False)
   # print(data.text)

    html= etree.HTML(data.text)
    list=html.xpath('//dd')
    for l in list:
        dd=etree.HTML(etree.tostring(l))
        print(dd)
        index=dd.xpath('//i/text()')
        name=dd.xpath('//p[@class="name"]/a/text()')[0]
        star=dd.xpath('//p[@class="star"]/text()')[0].strip()
        releasetime=dd.xpath('//p[@class="releasetime"]/text()')[0]
        print(name,'='*8,star,'='*8,releasetime,"="*8,index[0])
        pf=index[1]+index[2]
        list=[index[0],name,star,releasetime,pf]
        yield list
    #print(list)
#存储csv
def save_csvfile(data):
     with open("code/my.csv",'a',encoding="utf-8") as fp:
            if os.path.getsize('code/my.csv')==0:
                fp.write("排名,名字,演员,上映时间,评分\n")
            else:
                f=csv.writer(fp)
                f.writerow(data)

if __name__ == "__main__":
    datas = get_yemian(url)
    for data in datas:
        save_csvfile(data)























































































































































































































































































































































































































































































































































































































































































































