from p5 import *

start = (306, 72)
control_1 = (36, 36)
control_2 = (324, 324)
end = (54, 288)

def setup():
    size(360, 360)
    no_loop()

def draw():
    bezier(start, control_1, control_2, end)
    steps = 10
    for s in range(steps + 1):
        t = s / steps
        bz = bezier_point(start, control_1, control_2, end, t)
        circle(bz, 20)

run()
