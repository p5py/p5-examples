#
# Hue
#
# Hue is the color reflected from or transmitted through an object.
# and is typically referred to as the name of the color (red, blue,
# yellow, etc). Move the cursor vertically over each bar to alter its
# hue.
#

from p5 import *

bar_width = 20
last_bar = None

def setup():
    size(640, 360)
    title("Hue")
    color_mode('HSB', height, height, height)
    no_stroke()
    background(0)

def draw():
    global last_bar
    which_bar = mouse_x // bar_width
    if which_bar is not last_bar:
        bar_x = which_bar * bar_width
        fill(mouse_y, height, height)
        rect((bar_x, 0), bar_width, height)
        last_bar = which_bar

if __name__ == '__main__':
    run()
