import requests
import json

#查询响应
#url = "https://api.github.com/rate_limit"
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r= requests.get(url)
print(f"Status code: {r.status_code}")

response_dict = r.json()

#整理成能看懂的
readable_file = "readable_file.json"
with open(readable_file,"w") as f:
    json.dump(response_dict,f,indent=4)

