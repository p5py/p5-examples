from p5 import *

xoff = 0

def setup():
    noise_seed(0)
    stroke(0, 10)

def draw():
    global xoff
    xoff = xoff + 0.01
    n = noise(xoff) * width
    line((n, 0), (n, height))

run()
