# List 2D.
#
# Demonstrates the syntax for creating a two-dimensional (2D) list.
# Values in a 2D list are accessed through two index values. 2D arrays
# are useful for storing images. In this example, each square is
# colored in relation to its distance from the center of the image.

from p5 import *

distances = []
max_distance = None
spacer = 20

def setup():
    global max_distance
    size(640, 360)
    title("List 2D")

    center_of_screen = Vector(width / 2, height / 2)
    max_distance = dist(center_of_screen, (width, height))

    for x in range(width):
        distances.append([])
        for y in range(height):
            distance = dist(center_of_screen, (x, y))
            distances[x].append(distance/max_distance * 255)

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
            fill(distances[x][y])
            square((x, y), spacer)

if __name__ == '__main__':
    run()
