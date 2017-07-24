from p5 import *

distances = []
max_distance = None
spacer = 20

def setup():
    global max_distance
    size(640, 360)

    center_of_screen = Vector(width / 2, height / 2)
    max_distance = dist(center_of_screen, (width, height))

    for x in range(width):
        distances.append([])
        for y in range(height):
            distance = dist(center_of_screen, (x, y))
            distances[x].append(distance/max_distance * 255)

    no_stroke()

def draw():
    background(255)
    for y in range(0, height, spacer):
        for x in range(0, width, spacer):
            fill(distances[x][y])
            square((x, y), spacer)

run()
    
