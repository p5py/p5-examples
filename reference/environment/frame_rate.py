from p5 import *

def setup():
    set_frame_rate(30)

def draw():
    background(204)
    line((0, 0), (width, height))
    print(frame_rate)

run()
