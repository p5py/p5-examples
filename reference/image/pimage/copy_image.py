from p5 import *

raspberries = load_image("../raspberries-256.jpg")

def setup():
    size(*raspberries.size)
    raspberries[:128, :] = raspberries[128:, :]
    no_loop()

def draw():
    background(raspberries)

if __name__ == '__main__':
    run()
