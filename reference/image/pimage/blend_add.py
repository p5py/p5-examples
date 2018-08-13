from p5 import *

img1 = load_image('../src/luminale-512.jpg')
img2 = load_image('../src/grand-theatre-512.jpg')
img3 = load_image('../src/luminale-512.jpg')

img3.blend(img2, 'add')

def setup():
    size(img1.width, int(img1.height * 1.5))
    no_loop()

def draw():
    image(img1, (0, 0), (img1.width // 2, img1.height // 2))
    image(img2, (img1.width // 2, 0), (img1.width // 2, img1.height // 2))
    image(img3, (0, img1.height // 2))

if __name__ == '__main__':
    run()
