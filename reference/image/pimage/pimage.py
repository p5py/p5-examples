from p5 import *

img = load_image('../wave-512.png')

def setup():
    size(512, 512)
    no_loop()

def draw():
    image(img, (0, 0))

if __name__ == '__main__':
    run()
