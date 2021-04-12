import json
import plotly.express as px
import pandas as pd

#import data of earthquake
filename = "data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

''''#transfer the data to be readable
readable_file = "data/readable_eq_data_30_day_m1.json"
with open(readable_file,"w") as f:
    json.dump(all_eq_data,f,indent =4)'''

all_eq_dicts = all_eq_data["features"]

mags,titles,longitudes,latitudes = [],[],[],[]

# collect all the magnitudes,titles,longitudes,latitudes
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    mags.append(mag)
    title = eq_dict["properties"]["title"]
    titles.append(title)
    longitude = eq_dict["geometry"]["coordinates"][0]
    longitudes.append(longitude)
    latitude = eq_dict["geometry"]["coordinates"][1]
    latitudes.append(latitude)

#DataFrame 数据封装
data = pd.DataFrame(
    data = zip(longitudes,latitudes,titles,mags),
    columns=["longitude","latitude","position","magnitude"]
)

#set the scatter plot
fig = px.scatter(
    data,
    x = "longitude",
    y = "latitude",
    #panda封装后 不需要： labels = {"x":"Longtitude","y":"Latitudes"},
    range_x = [-190,190],
    range_y = [-90,90],
    width = 800,
    height = 800,
    title="Global Earthquake Scatter Plots",
    size = "magnitude",
    size_max = 10,
    color="magnitude",
    hover_name="position"
)


fig.write_html("global_earthquake")
fig.show()
