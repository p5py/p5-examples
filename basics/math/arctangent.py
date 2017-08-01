#
# Arctangent
#
# Move the mouse to change the direction of the eyes. The atan2()
# function computes the angle from each eye to the cursor.
#

from p5 import *

eyes = []

class Eye:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size / 2
        self.angle = 0

    def update(self, mx, my):
        self.angle = atan2(my - self.y, mx - self.x)

    def display(self):
        with push_matrix():
            translate(self.x, self.y)

            fill(255)
            circle((0, 0), self.size)

            rotate(self.angle)
            fill(153, 204, 0)

            circle((self.size / 2, 0), self.size / 2)


def setup():
    size(640, 360)
    title("Arctan Example")

    no_stroke()

    e1 = Eye(250, 16, 120)
    e2 = Eye(164, 185, 80)
    e3 = Eye(420, 230, 220)

    eyes.extend([e1, e2, e3])

def draw():
    background(102)
    for eye in eyes:
        eye.update(mouse_x, mouse_y)
        eye.display()

if __name__ == '__main__':
    run()
