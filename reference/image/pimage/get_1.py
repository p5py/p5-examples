from p5 import *

lake = load_image('../lake-512.jpg')

def setup():
    size(512, 512)
    no_stroke()
    no_loop()

def draw():
    image(lake, (0, 0))

    c = lake[440, 20]
    fill(c)
    square((128, 128), 256)

if __name__ == '__main__':
    run()
