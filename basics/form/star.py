# Star
#
# The star() function created for this example is capable of drawing a
# wide range of different forms. Try placing different numbers into
# the star() function calls within setup() to explore.
#

from p5 import *

star_one = None
star_two = None
start_three = None

def star(x, y, radius_1, radius_2, num_points):
    angle = TWO_PI / num_points
    half_angle = angle / 2
    st = PShape()
    with st.edit():
        a = 0
        while a < TWO_PI:
            vert = (x + cos(a) * radius_2,
                    y + sin(a) * radius_2)
            st.add_vertex(vert)
            vert = (x + cos(a + half_angle) * radius_1,
                    y + sin(a + half_angle) * radius_1)
            st.add_vertex(vert)
            a = a + angle

    return st

def setup():
    global star_one
    global star_two
    global star_three

    size(640, 360)

    star_one = star(0, 0, 5, 70, 3)
    star_one.translate(width * 0.2, height * 0.5)

    star_two = star(0, 0, 80, 100, 40)
    star_two.translate(width * 0.5, height * 0.5)

    star_three = star(0, 0, 30, 70, 5)
    star_three.translate(width * 0.8, height * 0.5)


def draw():
    background(102)
    star_one.rotate(0.005)
    draw_shape(star_one)

    star_two.rotate(0.0025)
    draw_shape(star_two)

    star_three.rotate(-0.01)
    draw_shape(star_three)

if __name__ == '__main__':
    run()
