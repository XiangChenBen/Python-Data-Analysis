from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()
die2 = Die(10)
results = []
frequencies = {}
total_roll_num =50000

for roll_num in range(total_roll_num):
    result = die1.roll()+die2.roll()
    results.append(result)

for key in range(2,die1.num_sides+die2.num_sides+1):
    frequencies[key] = results.count(key)

x_values = list(range(2,die1.num_sides+die2.num_sides+1))
frequencies_value = [value for key,value in frequencies.items()]
data = [Bar(x=x_values,y=frequencies_value)]

x_axis_config = {"title":"结果","dtick":1}
y_axis_config = {"title":"结果的频率"}
my_layout = Layout(title = f"掷一个D{die1.num_sides}和一个D{die2.num_sides} {total_roll_num}次的结果",
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({"data":data,"layout":my_layout},filename=f"D{die1.num_sides}&D{die2.num_sides}.html")



