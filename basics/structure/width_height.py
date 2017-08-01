#
# width and height
#
# The width and height (global) variables contain the widt and heigth
# of the display window as defined in the size() function.
#

from p5 import *

def setup():
    size(640, 360)
    no_stroke()

def draw():
    background(127)
    for i in range(0, height, 20):
        fill(129, 206, 15)
        rect((0, i), width, 10)
        fill(255)
        rect((i, 0), 10, height)

if __name__ == '__main__':
    run()
    

