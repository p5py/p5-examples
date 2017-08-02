# Random Gaussian.
#
# This sketch draws circles with x and y locations tied to a gaussian
# distribution of random numbers.

from p5 import *

def setup():
    size(640, 360)
    title("Random Gaussian")

    no_stroke()
    fill(255, 10)
    background(0)

def draw():
    # Get a gaussian random number with mean of (width / 2) and
    # standard deviation of 60.
    x = random_gaussian(mean=(width / 2), std_dev=60)

    # Draw a circle at our "normal" random location.
    circle((x, height / 2), 32)

if __name__ == '__main__':
    run()
