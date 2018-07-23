from p5 import *

soyuz = load_image('../soyuz-256.jpg')

def setup():
    size(*soyuz.size)
    no_loop()

def draw():
    white = Color(255, 255, 255)
    for px in range(16, width, 16):
        for py in range(16, height, 16):
            soyuz[px, py] = white

    image(soyuz, (0, 0))

if __name__ == '__main__':
    run()
