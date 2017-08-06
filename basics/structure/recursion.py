# Recursion.
#
# A demonstration of recursion, which means functions call themselves.
# Notice how the drawCircle() function calls itself at the end of its
# block. It continues to do this until the variable "level" is equal
# to 1.

from p5 import *

def setup():
    size(640, 360)
    no_stroke()

def draw():
    background(204)
    draw_circle(width/2, 280, 6)

def draw_circle(x, radius, level):
    tt = 126 * level / 4
    fill(tt)
    circle((x, height/2), radius * 2)
    if level > 1:
        draw_circle(x - radius / 2, radius / 2, level - 1)
        draw_circle(x + radius / 2, radius / 2, level - 1)

if __name__ == '__main__':
    run()
