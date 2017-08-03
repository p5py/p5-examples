# Noise 1D
#
# Using 1D Perlin Noise to assign location.

from p5 import *

xoff = 0
xincrement = 0.01

def setup():
    size(640, 360)
    background(0)
    no_stroke()

def draw():
    global xoff

    # create an alpha blended background
    background(0, 10)

    # get a noise value based on xoff and scale it according to the
    # window's width
    n = noise(xoff) * width

    # with each cycle, increment xoff
    xoff = xoff + xincrement

    # Draw the circle at the value produced by perlin noise.
    fill(200)
    circle((n, height / 2), 64)

if __name__ == '__main__':
    run()
