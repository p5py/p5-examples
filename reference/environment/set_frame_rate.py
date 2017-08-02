from p5 import *

position = 0

def setup():
    set_frame_rate(4)

def draw():
    global position
    position += 3

    background(204)
    line((position, 72), (position, 288))

    if position > width:
        position = 0

run()
