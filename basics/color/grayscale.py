#
# Grayscale conversion.
#
# Convert colors to grayscale. A color gradient is shown on the top
# with all the colors converted to grayscale on the bottom.
#
# Usage:
# - Press <S> to randomize the start color.
# - Press <E> to randomize the end color.
# - Press <UP> to increase the number of colored bands
# - Press <DOWN> to decrease the number of colored bands
#

from p5 import *

start_color = Color(255)
end_color = Color(0)
lerp_bands = 5

def setup():
    size(640, 360)
    no_stroke()
    background(0)

def draw():
    background(0)
    for bi in range(lerp_bands):
        lerp_amount = bi/(lerp_bands - 1)
        band_color = start_color.lerp(end_color, lerp_amount)
        band_location = remap(bi, (0, lerp_bands), (0, width))

        fill(band_color)
        rect((band_location, 0), width/lerp_bands, height/2)

        fill(band_color.gray)
        rect((band_location, height/2), width/lerp_bands, height/2)

def key_pressed(event):
    global lerp_bands

    if event.key == 's':
        start_color.r = random_uniform(0, 255)
        start_color.g = random_uniform(0, 255)
        start_color.b = random_uniform(0, 255)

    elif event.key == 'e':
        end_color.r = random_uniform(0, 255)
        end_color.g = random_uniform(0, 255)
        end_color.b = random_uniform(0, 255)

    elif event.key == 'UP':
        lerp_bands = constrain(lerp_bands + 1, 3, 100)
    elif event.key == 'DOWN':
        lerp_bands = constrain(lerp_bands - 1, 3, 100)

if __name__ == '__main__':
    run()
