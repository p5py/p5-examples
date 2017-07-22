#
# Color Variables (Homage to Albers).
#
# This example creates variables for colors that may be referred to in
# the program by a name, rather than a number.
#

from p5 import *

bgcolor = Color(51, 0, 0)
inside = Color(204, 102, 0)
middle = Color(204, 153, 0)
outside = Color(153, 51, 0)

def setup():
    size(640, 360)
    no_stroke()

def draw():
    background(bgcolor)
    with push_matrix():
        translate(80, 80)

        fill(outside)
        square((0, 0), 200)

        fill(middle)
        square((40, 60), 120)

        fill(inside)
        square((60, 90), 80)

    with push_matrix():
        translate(360, 80)

        fill(inside)
        square((0, 0), 200)

        fill(outside)
        square((40, 60), 120)

        fill(middle)
        square((60, 90), 80)

if __name__ == '__main__':
    run()
