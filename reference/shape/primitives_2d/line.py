from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    stroke(0)
    line((108, 72), (306, 72))

    stroke(126)
    line((306, 72), (306, 270))

    stroke(255)
    line((306, 270), (108, 270))

run()
