from p5 import *

distribution = [abs(random_gaussian()) * 54 for _ in range(360)]

def draw():
    no_loop()
    background(204)
    stroke(0)

    translate(width / 2, height / 2)

    for di in distribution:
        rotate(TWO_PI / len(distribution))
        line((0, 0), (di, 0))

run()
