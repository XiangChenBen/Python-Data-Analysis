from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
point_num = range(rw.num_points - 1)
ax.scatter(rw.x_values[0], rw.y_values[0], c="Red", edgecolor="none", s=100)
ax.scatter(rw.x_values[1:-1], rw.y_values[1:-1], c=point_num, cmap=plt.cm.Blues, edgecolor="none", s=1)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="green", edgecolor="none", s=100)

#隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

