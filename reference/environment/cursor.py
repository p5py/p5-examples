from p5 import *

def draw():
    if mouse_x < 180:
        cursor('CROSS')
    else:
        cursor('HAND')

run()
