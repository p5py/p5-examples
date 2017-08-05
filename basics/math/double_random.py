#
# Double Random
# by Ira Greenberg
#
# Python port: Abhik Pal
#
# Using two random() calls and the point() function to create an
# irregular sawtooth line.

from p5 import *

total_points = 300
steps = total_points + 1

def setup():
    size(640, 360)
    title("Double Random")
    background(0)
    stroke(255)

def draw():
    background(0)

    rand = 0
    for i in range(1, steps):
        x = (width / steps) * i
        y = (height / 2)  + random_uniform(-rand, rand)
        point(x, y)

        rand += random_uniform(-5, 5)

if __name__ == '__main__':
    run(frame_rate=1)
