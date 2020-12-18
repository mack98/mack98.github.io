import re
import requests



def get_fan():
    url="https://bangumi.bilibili.com/web_api/timeline_global"
    response = requests.get(url)
    title=re.findall('"title":"(.*?)"',response.text)
    print(title)



if __name__ == "__main__":
    get_fan()