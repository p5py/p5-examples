from p5 import *

img = load_image('../wave-128.png')

def setup():
    size(128, 128)
    no_loop()

def draw():
    image(img, (0, 0))

    img.size = (128, 64)
    image(img, (0, 64))

if __name__ == '__main__':
    run()
