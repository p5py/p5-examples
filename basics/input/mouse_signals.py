#
# Mouse Signals.
#
# Move and click the mouse to generate signals. The top row is the
# signal from mouse_x, the middle row is the signal from mouse_y and
# the bottom row is the signal from mouse_is_pressed.

from p5 import *

xvals = []
yvals = []
bvals = []

array_idx = 0

def setup():
    size(640, 360)
    for _ in range(width):
        xvals.append(0)
        yvals.append(0)
        bvals.append(0)

def draw():
    global xvals
    global yvals
    global bvals
    global array_idx

    background(102)

    for idx in range(1, width):
        xvals[idx - 1] = xvals[idx]
        yvals[idx - 1] = yvals[idx]
        bvals[idx - 1] = bvals[idx]

    xvals[-1] = mouse_x
    yvals[-1] = mouse_y
    bvals[-1] = 0 if mouse_is_pressed else 255

    fill(255)
    no_stroke()
    rect((0, height/3), width, height / 3 + 1);

    for idx in range(1, width):
        stroke(255)
        point(idx, xvals[idx] / 3)

        stroke(0)
        point(idx, height / 3 + yvals[idx] / 3)

        stroke(255)
        line((idx, 2 * height / 3 + bvals[idx] / 3),
             (idx, 2 * height / 3 + bvals[idx - 1] / 3))

if __name__ == '__main__':
    run()
