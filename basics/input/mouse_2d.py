#
# Mouse 2D
#
# Moving the mouse changes the position and size of each box.
#
from p5 import *

def setup():
    size(640, 360)
    title("Mouse 2D")
    no_stroke()
    rect_mode('CENTER')

def draw():
    background(51)

    fill(255, 204)
    square((mouse_x, height / 2), mouse_x / 2 + 10)

    fill(255, 204)
    inverse_x = width - mouse_x
    inverse_y = height - mouse_y
    square((inverse_x, height / 2), inverse_y / 2 + 10)

if __name__ == '__main__':
    run()
