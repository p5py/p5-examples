# Linear Interpolation.
#
# Move the mouse across the screen and the symbol will follow. Between
# drawing each frame of the animation, the ellipse moves part of the
# distance (0.05) from its current position toward the cursor using
# the lerp() function
#
# This is the same as the Easing under input only with lerp() instead.

from p5 import *

x, y = 0, 0

def setup():
    size(640, 360)
    title("Interpolate")
    no_stroke()

def draw():
    global x
    global y

    background(51)

    # lerp() calculates a number between two numbers at a specific
    # increment. The `amount` parameter is teh amount to interpoate
    # between thw two values where 0 is equal to the first point, 0.1
    # is very near the first point, 0.5 is half-way between, etc.
    #
    # Here we are moving 5% of the way to the mouse location each
    # frame.
    #
    x = lerp(x, mouse_x, 0.05)
    y = lerp(y, mouse_y, 0.05)

    fill(255)
    circle((x, y), 33)

if __name__ == '__main__':
    run()
