from p5 import *

start = (306, 72)
control_1 = (36, 36)
control_2 = (324, 324)
end = (54, 288)

def setup():
    size(360, 360)

def draw():
    background(204)
    detail = floor(remap(mouse_x, (0, width), (1, 20)))
    bezier_detail(detail)
    bezier(start, control_1, control_2, end)

run()
