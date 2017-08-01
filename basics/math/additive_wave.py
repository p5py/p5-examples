#
# Additive Wave
# by Daniel Shiffman
#
# Python port: Abhik Pal
#
# Create a more complex wave by adding two waves together.
#

from p5 import *

# How far apart should each horizontal location be spaced.
xspacing = 8

# width of the entire wave
wave_width = None

# total number of waves to add
max_waves = 4

theta = 0

# height of wave
amplitude = []

# values for incrementing X, to be calculated as a function of period
# and `xspacing`.
dx = []

# using an array to store height values for the wave (not entirely
# necessay)
yvalues = []

def setup():
    global wave_width

    size(640, 360)
    title("Additive Wave")

    wave_width = width + 16

    for i in range(max_waves):
        amplitude.append(random_uniform(10, 30))

        period = random_uniform(100, 300)
        dx.append((TWO_PI / period) * xspacing)

def draw():
    background(0)
    calculate_wave()
    render_wave()

def calculate_wave():
    """(Re)calculate the yvalues for the wave
    """
    global theta, yvalues

    # increment theta (try different values of 'angular velocity'
    # here.)
    theta += 0.08

    yvalues = [0] * int(wave_width / xspacing)

    for j in range(max_waves):
        x = theta
        for i in range(int(wave_width / xspacing)):
            if j % 2 == 0:
                yvalues[i] += cos(x) + amplitude[j]
            else:
                yvalues[i] += cos(x) * amplitude[j]
            x += dx[j]

def render_wave():
    """Render the wave"""
    no_stroke()
    fill(255, 127)

    for x, yval in enumerate(yvalues):
        location = x * xspacing, (height / 2) + yval
        circle(location, 8, mode='CENTER')

if __name__ == '__main__':
    run()
