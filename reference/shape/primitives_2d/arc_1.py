from p5 import *

def draw():
    no_loop()

    arc((180, 198), 180, 180, 0, HALF_PI)
    no_fill()
    arc((180, 198), 216, 216, HALF_PI, PI)
    arc((180, 198), 251, 251, PI, PI + QUARTER_PI)
    arc((180, 198), 288, 288, PI + QUARTER_PI, TWO_PI)

run()
