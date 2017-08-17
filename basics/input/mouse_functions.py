#
# Mouse Functions.
#
# Click on the box and drag it across the screen.
#
from p5 import *

box_position = Vector(0, 0)
box_size = 75
over_box = False
locked = False
offset = Vector(0, 0)

def setup():
    size(640, 360)
    title("Mouse Functions")
    box_position.x = width / 2
    box_position.y = height / 2
    rect_mode('RADIUS')

def draw():
    global over_box
    background(0)

    # Test if the cursor is over the box
    mouse_x_in_box = (mouse_x > box_position.x - box_size) and \
                     (mouse_x < box_position.x + box_size)
    mouse_y_in_box = (mouse_y > box_position.y - box_size) and \
                     (mouse_y < box_position.y + box_size)
    over_box = mouse_x_in_box and mouse_y_in_box

    if over_box:
        if not locked:
            stroke(255)
            fill(153)
    else:
        stroke(153)
        fill(153)

    # Draw the box
    square(box_position, box_size)

def mouse_pressed():
    global locked
    global offset

    locked = over_box

    if over_box:
        fill(255)

    offset = Vector(mouse_x, mouse_y) - box_position

def mouse_dragged():
    global box_position

    if locked:
        box_position = Vector(mouse_x, mouse_y) - offset

def mouse_released():
    global locked
    locked = False

if __name__ == '__main__':
    run()
