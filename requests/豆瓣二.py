import re
import requests
import os.path

#消息头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3858.400 QQBrowser/10.7.4309.400"

}

#获取详情页url
def get_urls():
    '''
        通过请求获取所有的url 
        return 返回
    '''
    url='https://movie.douban.com/top250?start=0&filter='
    responses = requests.get(url,headers=headers)
    urls=re.findall('<a href="(.*?)" class="">',responses.text)
    print(urls)
    return set(urls)


#获取详情页数据
def get_detail(detail_url):
    res_detail=requests.get(detail_url,headers=headers)
    title=re.search('<span property="v:itemreviewed">(.*?)</span>',res_detail.text).group(1)
    t250_no= re.search('<span class="top250-no">(.*?)</span>',res_detail.text).group(1)
    photo_url=re.search('<img class="media" src="(.*?)" />',res_detail.text).group(1)
    average=re.search('<strong class="ll rating_num" property="v:average">(.*?)</strong>',res_detail.text).group(1)
    votes=re.search('<span property="v:votes">(.*?)</span>',res_detail.text).group(1)
    summary=re.search(r'<span property="v:summary"\s*(class="")*>\s*(.*?)\s*(</span>|<br />)',res_detail.text).group(2)
    dictm={
        "标题":title,
        "预览图":photo_url,
        "简介":summary,
        "评分":average,
        "评分人数":votes,
        "排名":t250_no
    }
    return dictm


#生成csv 文件
def generate_csvfile(data):
    
    with open("code/douban.csv",'a+',encoding="utf-8") as fp:
        if os.path.getsize('code/douban.csv')==0:
            fp.write("标题,预览图,简介,评分,评分人数,排名\n")
        else:
            fp.write(data['标题']+','+
            data['预览图']+','+
            data['排名']+','+
            data['评分']+','+
            data['评分人数']+','+
            data['简介']
            +'\n')


if __name__ == "__main__":
    detail_urls=get_urls()
    for detail_url in detail_urls:
        data=get_detail(detail_url)
        generate_csvfile(data)

