#
# Easing
#
# MOve the mouse across the screen and the symbol will follow. Between
# drawing each frame of the animation, the program calculated the
# difference between the position of the symbol and the cursor. If the
# distance is larger than 1 pixel, the symbol moves part of the
# distance (0.05) from its current position toward the cursor.
#

from p5 import *

position = Vector(0, 0)
easing = 0.05

def setup():
    size(640, 360)
    title("Easing")
    no_stroke()

def draw():
    global position
    background(51)

    target = Vector(mouse_x, mouse_y)
    delta = target - position
    position = position + easing * delta

    circle(position, 66)

if __name__ == '__main__':
    run()
