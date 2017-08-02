from p5 import *

def draw():
    if mouse_is_pressed:
        no_cursor()
    else:
        cursor('HAND')

run()
