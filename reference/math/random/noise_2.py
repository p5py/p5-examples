from p5 import *

noise_scale = 0.02

def draw():
    background(0)

    for x in range(width):
        noise_val = noise((mouse_x + x) * noise_scale, mouse_y * noise_scale)
        stroke(noise_val * 255)
        line((x, mouse_y + noise_val * 288), (x, height))

run()
