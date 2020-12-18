import requests

#url= 'https://movie.douban.com/chart'
url = 'https://movie.douban.com/top250?start=0&filter='

headers={
# 'Accept':'*/*',

# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Connection':'keep-alive',
# 'Host':'movie.douban.com',
# 'Referer':'https://movie.douban.com/chart',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3858.400 QQBrowser/10.7.4309.400',
# 'X-Requested-With':'XMLHttpRequest'

}
# cookies ={
#     'Cookies':'bid=XI14sSOReWQ; __yadk_uid=094qqZZhYouePeLH1UjYlKZQsCE7G10Q; ll="118209"; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=DE8241984ABF6A0716332B2633926F982|3a5b9af54be668c61d6b9e8f1920b56c; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1606562302%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJSWORgMkTwHs0AmI0tilNiXgTvguTLBdK5ZjEl64NZ3MPqOWBa7mVXQRIYdna3tk%26wd%3D%26eqid%3Db560c7e1001455d6000000065fc231fb%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.949596221.1592703693.1606547914.1606562302.9; __utmb=30149280.0.10.1606562302; __utmz=30149280.1606562302.9.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1376407992.1597202996.1606547915.1606562302.3; __utmb=223695111.0.10.1606562302; __utmz=223695111.1606562302.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __gads=ID=2738e81d9b42aabc-2262ab59f3c40023:T=1606562309:RT=1606562309:R:S=ALNI_Mbm9P5RYwedyr7tUv8anzgjTWwv5w; _pk_id.100001.4cf6=990d7d1f4c7fca45.1597202996.3.1606563219.1606549388.'
# }
r=requests.get(url,headers=headers)
print(r.text)

with open('db.html','w',encoding='utf-8') as f:
    f.write(r.text)


print(r.history)