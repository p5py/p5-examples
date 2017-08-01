# Remap
#
# Use the remap() function to take any number and scale it to a new
# number that is more useful for the project that you are working on.
# For example, use the numbers from the mouse position to control the
# size or color of a shape. In this example, the mouse's x-coördinate
# (numbers between 0 and 360) are scaled to new numbers to define the
# color and size of a circle.

from p5 import *

def setup():
    size(640, 360)
    title("Remap")
    no_stroke()

def draw():
    background(0)

    # Scale the mouse_x value from the range (0, 640) to the
    # equivalent value in the range(0, 175)
    c = remap(mouse_x, (0, width), (0, 175))

    # Scale the mouse_x value the range (0, 640) to the equivalent
    # value in the range(20, 150)
    radius = remap(mouse_x, (0, width), (20, 150))

    fill(255, c, 0)
    circle((width / 2, height / 2), radius)

if __name__ == '__main__':
    run()
