from turtle import Turtle
import time

SOUTH = 270
NORTH = 90
EAST = 0
WEST = 180
NORTH_BORDER = 400
EAST_BORDER = 400
SOUTH_BORDER = -400
WEST_BORDER = -400
PATTERN = 20
FORWARD = 5


class Robot:

    def __init__(self, obstacles, window):
        self.robot = Turtle()
        self.obstacles = obstacles
        self.window = window

    def move_pattern(self):
        self.robot.forward(FORWARD)
        self.ob_av()
        self.check_for_end()

    def check_for_end(self):
        if self.robot.xcor() > EAST_BORDER:
            time.sleep(0.1)
            self.window.update()
            self.robot.setheading(SOUTH)
            self.robot.forward(PATTERN)
            self.robot.setheading(WEST)
        elif self.robot.xcor() < WEST_BORDER:
            time.sleep(0.01)
            self.window.update()
            self.robot.setheading(SOUTH)
            self.robot.forward(PATTERN)
            self.robot.setheading(EAST)

    def ob_av(self):
        obstacle_cors = [(obstacle.xcor(), obstacle.ycor()) for obstacle in self.obstacles]
        xcor = self.robot.xcor()
        ycor = self.robot.ycor()
        for cors in obstacle_cors:
            x_dif = cors[0] - xcor
            y_dif = cors[1] - ycor
            if 0 <= x_dif < 22:
                if 0 <= y_dif < 22:
                    self.around(21 - y_dif, 21 + x_dif, SOUTH, EAST, NORTH)
                elif -22 < y_dif <= 0:
                    self.around(21 + y_dif, 21 + x_dif, NORTH, EAST, SOUTH)
            elif -22 < x_dif <= 0:
                if 0 <= y_dif < 22:
                    self.around(21 - y_dif, 21 - x_dif, SOUTH, WEST, NORTH)
                elif -22 < y_dif <= 0:
                    self.around(21 + y_dif, 21 - x_dif, NORTH, WEST, SOUTH)

    def around(self, vert_dist, hori_dist, first_deg, sec_deg, third_deg):
        time.sleep(0.02)
        self.window.update()
        self.robot.setheading(first_deg)
        self.robot.forward(vert_dist)
        time.sleep(0.02)
        self.window.update()
        self.robot.setheading(sec_deg)
        self.robot.forward(hori_dist)
        time.sleep(0.02)
        self.window.update()
        self.robot.setheading(third_deg)
        self.robot.forward(vert_dist)
        self.robot.setheading(sec_deg)
        time.sleep(0.02)
        self.window.update()
