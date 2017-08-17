#
# Constrain
#
# Move the mouse across the screen to move the circle. THe program
# constrains the circle to its box.
from p5 import *

easing = 0.05
radius = 24
edge = 100
inner = edge + radius
m = Vector(0, 0)

def setup():
    size(640, 360)
    title("Constrain")
    no_stroke()
    ellipse_mode('RADIUS')
    rect_mode('CORNERS')

def draw():
    background(51)

    if abs(mouse_x - m.x) > 0.1:
        m.x = m.x + (mouse_x - m.x) * easing

    if abs(mouse_y - m.y) > 0.1:
        m.y = m.y + (mouse_y - m.y) * easing

    m.x = constrain(m.x, inner, width - inner)
    m.y = constrain(m.y, inner, height - inner)

    fill(76)
    rect((edge, edge), (width - edge, height - edge))

    fill(255)
    circle(m, radius)

if __name__ == '__main__':
    run()
