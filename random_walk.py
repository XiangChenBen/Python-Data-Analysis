from random import choice

class RandomWalk:
    """一个随机生成漫步数据的类"""

    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        self.direction = choice([1,-1])
        self.distance = choice([0,1,2,3,4,5])
        self.step = self.direction*self.distance
        return self.step

    def fill_walk(self):
        while len(self.x_values) <=self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step==0 and y_step==0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


