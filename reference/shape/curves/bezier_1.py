from p5 import *

start_point = (306, 72)
control_point_1 = (36, 36)
control_point_2 = (324, 324)
end_point = (54, 288)

def setup():
    size(360, 360)
    no_loop()

def draw():
    stroke(255, 102, 0)
    line(start_point, control_point_1)
    line(end_point, control_point_2)

    stroke(0)
    bezier(start_point, control_point_1, control_point_2, end_point)

run()
