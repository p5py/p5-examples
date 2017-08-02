from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    p1 = (108, 270)
    p2 = (208, 72)
    p3 = (309, 270)
    triangle(p1, p2, p3)

run()
