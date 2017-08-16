#
# Pie Chart
#
# Uses the art() function to generate a pie chart from teh data stored
# in a list.
#
from p5 import *

angles = [30, 10, 45, 35, 60, 38, 75, 67]

def setup():
    size(640, 360)
    no_stroke()
    no_loop()

def draw():
    background(100)
    pie_chart(300, angles)

def pie_chart(diameter, data):
    last_angle = 0
    for i, d in enumerate(data):
        gray = remap(i, (0, len(data)), (0, 255))
        fill(gray)
        arc((width / 2, height / 2), diameter, diameter, last_angle,
            last_angle + radians(d))
        last_angle += radians(d)

if __name__ == '__main__':
    run()
