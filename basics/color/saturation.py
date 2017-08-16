#
# Saturation
#
# Saturation is the strength or purity of the color and represents the
# amount of gray in proportion to the hue. A "saturated" color is pure
# and an "unsaturated" color has a large percentage of gray. Move the
# cursor vertically over each bar to alter its saturation.
#

from p5 import *

bar_width = 20
last_bar = None

def setup():
    size(640, 360)
    title("Saturation")
    color_mode('HSB', width, height, 100)
    no_stroke()
    background(0)

def draw():
    global last_bar
    which_bar = mouse_x // bar_width
    if which_bar is not last_bar:
        bar_x = which_bar * bar_width
        fill(bar_x, mouse_y, 66)
        rect((bar_x, 0), bar_width, height)
        last_bar = which_bar

if __name__ == '__main__':
    run()
