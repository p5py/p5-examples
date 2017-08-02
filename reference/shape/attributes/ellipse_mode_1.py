from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    # Draw a white circle with 'RADIUS' mode
    fill(255)
    ellipse_mode('RADIUS')
    circle((450, 180), 100)

    # Draw a gray circle using 'CENTER' mode.
    fill(100)
    ellipse_mode('CENTER')
    circle((450, 180), 100)

run()
