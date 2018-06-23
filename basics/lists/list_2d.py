# List 2D.
#
# Demonstrates the syntax for creating a two-dimensional (2D) list.
# Values in a 2D list are accessed through two index values. 2D arrays
# are useful for storing images. In this example, each square is
# colored in relation to its distance from the center of the image.

from p5 import *

colors = []
spacer = 20

def setup():
    global max_distance
    size(640, 360)
    title("List 2D")

    for x in range(width):
        colors.append([])
        for y in range(height):
            colors[x].append(random_gaussian(127, 31))

    no_stroke()
    no_loop()

def draw():
    background(0)

    # This embedded loop skips over values in the list based on the
    # spacer variable, so there are more values in the array than are
    # drawn here. Change the value of the spacer variable to change
    # the density of the squares
    for y in range(0, height, spacer):
        for x in range(0, width, spacer):
            fill(colors[x][y])
            square((x, y), spacer)

if __name__ == '__main__':
    run()
