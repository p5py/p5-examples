from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    # Draw white rect using 'RADIUS' mode.
    fill(255)
    rect_mode('RADIUS')
    rect((180, 180), 108, 108)

    # Draw a gray rect using 'CENTER' mode
    fill(100)
    rect_mode('CENTER')
    rect((180, 180), 108, 108)

run()
