from turtle import Turtle, Screen
from robotlogic import Robot
import random
import time

window = Screen()

obstacles = []
window.tracer(0, 0)


for x in range(random.randint(20, 40)):
    rand_x = random.randint(-380, 380)
    rand_y = random.randint(-380, 380)

    obstacle = Turtle()
    obstacle.shape("square")
    obstacle.penup()
    obstacle.color("orange")
    obstacle.setposition(rand_x, rand_y)
    obstacles.append(obstacle)

window.update()
robot = Robot(obstacles, window)

robot.robot.penup()
robot.robot.goto(-401, 400)
robot.robot.pendown()

auto = True
while auto:
    robot.move_pattern()
    window.update()
    time.sleep(0.001)

window.mainloop()
