#
# Sine
#
# Smoothly scaling size with the sin() function.

from p5 import *

diameter = None
angle = 0

def setup():
    global diameter

    size(640, 360)
    title("Sine")

    diameter = height - 10

    no_stroke()
    fill(255, 204, 0)

def draw():
    global angle

    background(0)

    d1 = 10 + (sin(angle) * diameter / 2) + diameter / 2;
    d2 = 10 + (sin(angle + PI / 2) * diameter / 2) + diameter / 2;
    d3 = 10 + (sin(angle + PI) * diameter / 2) + diameter / 2;

    circle((0, height / 2), d1 / 2)
    circle((width / 2, height / 2), d2 / 2)
    circle((width, height / 2), d3 / 2)

    angle += 0.04

if __name__ == '__main__':
    run()
