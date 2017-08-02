# Polar to Cartesian
# by Daniel Shiffman
#
# Python port: Abhik Pal
#
# Convert a polar coördinate (r, theta) to cartesian (x, y):
#
#     x = r * cos(theta)
#     y = r * sin(theta)

from p5 import *

r = None

# angle, angular velocity, accleration
theta = 0
theta_vel = 0
theta_acc = 0.0001

def setup():
    global r

    size(640, 360)
    title("Polar to Cartesian")

    fill(200)
    no_stroke()

    r = height * 0.45

def draw():
    global theta
    global theta_vel

    background(0)

    # Translate the origin point to the center of the screen.
    translate(width / 2, height / 2)

    # Convert polar to cartesian
    x = r * cos(theta)
    y = r * sin(theta)

    circle((x, y), 30)

    # Apply acceleration and velocity to angle (r remains static in
    # this example)
    theta_vel += theta_acc
    theta += theta_vel

if __name__ == '__main__':
    run()
