#
# Mouse 1D
#
# Move the mouse left to right to shift the balance. THe "mouse_x"
# variable is used to control both the size and color of the
# rectangles.

from p5 import *

def setup():
    size(640, 360)
    title("Mouse 1D")
    no_stroke()
    color_mode('RGB', height, height, height)
    rect_mode('CENTER')

def draw():
    background(0)

    r1 = remap(mouse_x, (0, width), (0, height))
    r2 = height - r1

    fill(r1)
    square((width / 2 + r1 / 2, height / 2), r1)

    fill(r2)
    square((width / 2 - r2 / 2, height / 2), r2)

if __name__ == '__main__':
    run()
