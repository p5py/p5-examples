from p5 import *

lake = load_image("../lake-512.jpg")
new_lake = lake[256:, :]

def setup():
    size(*lake.size)
    no_loop()

def draw():
    background(lake)
    image(new_lake, (0, 0))

if __name__ == '__main__':
    run()
