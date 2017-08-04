from p5 import *

xoff = 0

def draw():
    global xoff
    background(204)
    xoff = xoff + 0.01
    n = noise(xoff) * width
    line((n, 0), (n, height))

run()
