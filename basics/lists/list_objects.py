# List Objects
#
# Demonstrated the syntax for creating a list of custom objects.
#

from p5 import *

unit = 40
modules = []

class Module:
    def __init__(self, xoff, yoff, x, y, speed, unit):
        self.x = x
        self.y = y
        self.xoff = xoff
        self.yoff = yoff
        self.speed = speed
        self.unit = unit
        self.x_direction = 1
        self.y_direction = 1

    def update(self):
        """Custom method for updating variables."""
        self.x = self.x + (self.speed * self.x_direction)
        if self.x > self.unit or self.x < 0:
            self.x_direction = (-1) * self.x_direction
            self.x = self.x + self.x_direction
            self.y = self.y + self.y_direction

        if self.y >= unit or self. y <= 0:
            self.y_direction = (-1) * self.y_direction

    def display(self):
        """Custom method for drawing the object"""
        with push_style():
            fill(255)
            circle((self.xoff + self.x, self.yoff + self.y), 6, mode="CENTER")


def setup():
    size(640, 360)
    no_stroke()
    wide_count = width // unit
    high_count = height // unit

    for y in range(high_count):
        for x in range(wide_count):
            m = Module(x * unit, y * unit, unit / 2, unit / 2,
                       random_uniform(low=0.05, high=0.8), unit)
            modules.append(m)

def draw():
    background(0)
    for mod in modules:
        mod.update()
        mod.display()

if __name__ == '__main__':
    run()
