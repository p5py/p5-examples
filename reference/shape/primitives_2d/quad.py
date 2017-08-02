from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    p1 = (136, 111)
    p2 = (309, 72)
    p3 = (248, 226)
    p4 = (108, 273)
    quad(p1, p2, p3, p4)

run()
