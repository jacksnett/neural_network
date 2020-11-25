import random
import Perpetron
import Point

point_arr = []


for index in range(200):
    point_arr.append(Point(random.randrange(1, 101), random.randrange(1, 101)))

myPerceptron = Perpetron(point_arr)

myPerceptron.train()
print("-----------------------------------")
