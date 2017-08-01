#
# Distance 1D
#
# Move the mouse left or right to control the speed and direction of
# the moving shapes.

from p5 import *

xpos = []

thin = 8
thick = 36

def setup():
    size(640, 360)
    title("Distance 1D")

    no_stroke()
    for _ in range(4):
        xpos.append(width / 2)

def draw():
    background(0)

    mx = mouse_x * 0.4 - width / 5.0

    fill(204)
    rect((xpos[0], 0), thin, height / 2)

    fill(102)
    rect((xpos[1], 0), thick, height / 2)

    fill(204)
    rect((xpos[2], height / 2), thin, height / 2)

    fill(102)
    rect((xpos[3], height / 2), thick, height / 2)

    xpos[0] += mx / 16
    xpos[1] += mx / 64
    xpos[2] -= mx / 16
    xpos[3] -= mx / 64

    for i, lim in enumerate([thin, thick, thin, thick]):
        if xpos[i] < (-lim):
            xpos[i] = width
        elif xpos[i] > width:
            xpos[i] = (-lim)

if __name__ == '__main__':
    run()
