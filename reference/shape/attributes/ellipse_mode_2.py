from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    # Draw a white ellipse using 'CORNER' mode
    fill(255)
    ellipse_mode('CORNER')
    ellipse((90, 90), 180, 180)

    # Draw a white ellipse using 'CORNERS' mode
    fill(100)
    ellipse_mode('CORNERS')
    ellipse((90, 90), (180, 180))

run()
