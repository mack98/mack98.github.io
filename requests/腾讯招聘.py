import json
from fake_useragent import UserAgent
import requests

#
ua=UserAgent()

url="https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1608206859895&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
headers = {
    'User-Agent':ua.random
}
response = requests.get(url,headers=headers)
json_res=json.loads(response.text)
#也可以直接 response.json()
Count = json_res.get("Data").get("Count")
#可以写成 json_res['Data']['Count']
posts_datas = json_res.get("Data").get("Posts")
for data in posts_datas:
    BGName=data.get("BGName")
    RecruitPostName=data['RecruitPostName']
    print(Count,"="*8,BGName,"="*8,RecruitPostName,"\n")