from p5 import *
recording = True

def setup():
    size(640, 360)
    no_stroke()
    background(204)

def draw():
    if not recording:
        return

    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    global recording
    if event.key == 'SPACE':
        recording = not recording
    background(204)

run()
