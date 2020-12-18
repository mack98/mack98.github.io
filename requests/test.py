import requests
r = requests.get('https://api.github.com/events')

print(r.url)
#print(r.text,r.encoding)
print(r.content)

