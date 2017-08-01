#
# Bezier
#
# The first paramtere for the bezier() function specifies the first
# point in the curve and the last parameter specifies the last point.
# The middle parameters set the control points that define the shape
# of the curve.
#

from p5 import *

def setup():
    size(640, 360)
    stroke(255)
    no_fill()

def draw():
    background(0)
    control_1 = (410, 20)
    control_2 = (440, 300)
    for i in range(0, 200, 20):
        start_point = (mouse_x - (i / 2.0), 40 + i)
        end_point = (240 - (i / 26), 300 + (i / 8))
        bezier(start_point, control_1, control_2, end_point)

run()
