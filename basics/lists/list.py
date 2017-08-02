# List
#
# A list is a data type in Python that can be used to group together
# other values. Lists might contain values of different types but
# usually the items have the same type. Each piece of data in a list
# is identified by an index number representing its position in the
# list. Lists are zero based, which means that the first element in
# the array is [0], the second element is [1], and so on. In this
# example, a list named "coswav" is created and filled with the cosine
# values. This data is displayed three separate ways on the screen.

from p5 import *

coswave = []

def setup():
    size(640, 360)
    title("List")

    for i in range(width + 1):
        amount = remap(i, (0, width), (0, PI))
        coswave.append(abs(cos(amount)))

    no_loop()

def draw():
    for i, cos_value in enumerate(coswave):
        stroke(cos_value * 255)
        line((i, 0), (i, height / 3))

        stroke(cos_value * 255 / 4)
        line((i, height / 3), (i, 2 * height / 3))

        stroke(255 - cos_value * 255)
        line((i, 2 * height / 3), (i, height))

if __name__ == '__main__':
    run()
