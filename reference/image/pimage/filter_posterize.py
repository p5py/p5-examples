from p5 import *

img1 = load_image('../raspberries-512.jpg')
img2 = load_image('../raspberries-512.jpg')

def setup():
    size(1024, 512)
    no_loop()

def draw():
    img2.filter('posterize', 2)

    image(img1, (0, 0))
    image(img2, (width / 2, 0))

if __name__ == '__main__':
    run()
