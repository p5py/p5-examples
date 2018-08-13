from p5 import *

def setup():
    no_loop()

def draw():
    s = "The quick brown fox jumped over the lazy dog."
    fill(51)
    text(s, (10, 10), wrap_at=10)

if __name__ == '__main__':
    run()
