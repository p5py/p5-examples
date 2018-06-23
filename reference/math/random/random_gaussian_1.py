from p5 import *

def setup():
    size(360, 360)
    no_loop()

def draw():
    for y in range(height):
        x = random_gaussian() * 54
        line((180, y), (180 + x, y))

run()
