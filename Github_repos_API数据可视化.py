import requests
from  plotly.graph_objs import Bar
from  plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept":"application/vnd.github.v3+json"}
r= requests.get(url,headers = headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]

#查询所含内容
'''print(f"\nKeys:{len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)'''

#文字输出前排名前列的github项目
for repo_dict in repo_dicts:
    print("\nSelected information about the first repository:")
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Created:{repo_dict['created_at']}")
    print(f"Updated:{repo_dict['updated_at']}")
    print(f"Description:{repo_dict['description']}")

#可视化输出排名前列的github项目

#处理结果
repo_links,stars,labels = [],[],[]
for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])
    descrption = repo_dict["description"]
    owner = repo_dict["owner"]["login"]
    labels.append(f"{owner}<br />{descrption}") #<br />为HTML换行符
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>") #HTML链接

#可视化
data = [{"type":"bar",
         "x":repo_links, #可点击x轴跳转页面
         "y":stars,
         "hovertext":labels,
         "marker":{
             "color":"rgb(60,100,150)",
             "line":{"width":1.5,"color":"rgb(25,25,25)"},
         },
         "opacity":0.6
         }]

my_layout = {
    "title":"Github上最受欢迎的python project",
    "titlefont":{"size":28},
    "xaxis":{"title":"Repository",
             "titlefont":{"size":24},
             "tickfont":{"size":14}
             },
    "yaxis":{"title":"Stars",
             "titlefont":{"size":24},
             "tickfont":{"size":14}
             },
}

fig = {"data":data,"layout":my_layout}
offline.plot(fig,filename = "visual_python_repository_rank.html")