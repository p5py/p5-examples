from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    start_point = (108, 72)
    control_point_1 = (288, 18)
    control_point_2 = (288, 270)
    end_point = (108, 270)

    stroke(255, 102, 0)
    line(start_point, control_point_1)
    line(end_point, control_point_2)

    stroke(0)
    bezier(start_point, control_point_1, control_point_2, end_point)

run()
