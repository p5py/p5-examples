from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    # Default rect_mode is 'CORNER'
    # Draw white rect using 'CORNER' mode.
    fill(255)
    rect_mode('CORNER')
    rect((90, 90), 180, 180)

    # Draw a gray rect using 'CORNERS' mode
    fill(100)
    rect_mode('CORNERS')
    rect((90, 90), (180, 180))

run()
