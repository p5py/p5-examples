from p5 import *

def draw():
    background(204)

    if focused:
        circle((180, 180), 180, mode='CENTER')
    else:
        line((0, 0), (width, height))
        line((width, 0), (0, height))

run()
