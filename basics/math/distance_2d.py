#
# Distance 2D.
#
# Move the mouse across the image to obscure and reveal the matrix.
# Measures the distance from the mouse to each square and sets the
# size proportionally.
#

from p5 import *

max_distance = 0

def setup():
    global max_distance

    size(640, 360)
    title("Distance 2D")

    no_stroke()

    max_distance = dist((0, 0), (width, height))

def draw():
    background(0)

    for x in range(0, width + 1, 40):
        for y in range(0, height + 1, 40):
            sz = dist((mouse_x, mouse_y), (x, y))
            sz = sz / max_distance * 66
            circle((x, y), sz)

if __name__ == '__main__':
    run()
