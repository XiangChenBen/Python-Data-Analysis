from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

#执行API调用并储存响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#处理文章信息
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    #对每篇文章都来个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"ID:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    #对于每篇文章都创建一个字典保存相关信息
    try:
        submission_dic = {
            "title": response_dict["title"],
            "hn_link":f"http://news.ycombinator.com/item?id={submission_id}",
            "comments":response_dict["descendants"],
        }
    except KeyError:
        print(f"there is no comment for {submission_id}")
        continue
    else:
        submission_dicts.append(submission_dic)

#comments排序
submission_dicts = sorted(submission_dicts,
                          key = itemgetter("comments"),
                          reverse=True)

#数据处理
mess_links,comments,labels = [],[],[]
for submission_dic in submission_dicts:
    print(f"\nTitle: {submission_dic['title']}")
    print(f"Discussion link: {submission_dic['hn_link']}")
    print(f"Comments: {submission_dic['comments']}")
    title = submission_dic['hn_link']
    hn_link = submission_dic['title']
    comments.append(submission_dic["comments"])
    mess_links.append(f"<a href='{title}'>{hn_link}</a>")
    labels.append(f"{title}<br />{submission_dic['comments']}")

#数据布置
data = [
    {"type":"bar",
     "x": mess_links,
     "y": comments,
     "hovertext":labels,
     "opacity":0.6,
    }
]

my_layout = {
    "title" : "Hacker_News_Comments_Rank",
    "titlefont": {"size":34},
    "xaxis":{
        "title":"News_Title",
        "titlefont":{"size":24},
        "tickfont":{"size":8},
        "tickangle":45,
    },
    "yaxis":{
            "title":"Number of Comments",
            "titlefont":{"size":24},
            "tickfont":{"size":16},
        },
}

#输出数据表
fig = {"data":data,"layout":my_layout}
offline.plot(fig,filename = "visual_Hacker_New_comments_rank.json")