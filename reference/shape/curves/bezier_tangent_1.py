from p5 import *

start = (306, 72)
control_1 = (36, 36)
control_2 = (324, 324)
end = (54, 288)

def setup():
    size(360, 360)
    no_loop()

def draw():
    bezier(start, control_1, control_2, end)
    steps = 10
    for s in range(steps + 1):
        t = s / steps

        # Get the location of the point.
        bpoint = bezier_point(start, control_1, control_2, end, t)

        # Get the tangent points
        tangent = bezier_tangent(start, control_1, control_2, end, t)

        # Calculate an angle from the tangent points
        a = atan2(tangent.y, tangent.x) + PI
        tpoint = 108 * cos(a) + bpoint.x, 108 * sin(a) + bpoint.y

        stroke(255, 102, 0)
        line(bpoint, tpoint)

        stroke(0)
        circle(bpoint, 20)

run()
