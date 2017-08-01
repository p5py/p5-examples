from p5 import *

coswave = []

def setup():
    size(640, 360)

    for i in range(width):
        amount = remap(i, (0, width), (0, PI))
        coswave.append(abs(cos(amount)))

    background(255)

def draw():
    background(255)
    for i, cos_value in enumerate(coswave):
        stroke(cos_value * 255)
        line((i, 0), (i, height / 3))

        stroke(cos_value * 255 / 4)
        line((i, height / 3), (i, 2 * height / 3))

        stroke(255 - cos_value * 255)
        line((i, 2 * height / 3), (i, height))
    
run()
