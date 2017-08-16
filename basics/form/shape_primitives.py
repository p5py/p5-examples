#
# Shape primitives
#
# The basic shape primitives are triangle(), rect(), square(), quad(),
# ellipse(), circle(), and arc(). Each of these functions requires a
# number of parametes to determine the shpae's position and size.
#

from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    no_loop()

def draw():
    background(0)

    fill(204)
    triangle((18, 18), (18, 360), (81, 360))

    fill(102)
    square((81, 81), 63)

    fill(204)
    quad((189, 18), (216, 18), (216, 360), (144, 360))

    fill(255)
    circle((252, 144), 72)

    fill(204)
    triangle((288, 18), (351, 360), (288, 360))

    fill(255)
    arc((479, 300), 280, 280, PI, TWO_PI)

if __name__ == '__main__':
    run()
