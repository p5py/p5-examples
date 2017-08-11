# A simple snake game
#
# Controls:
#   - Arrow keys start the game and control the snake.
#   - Spacebar pauses the game.

from p5 import *

tiles = 25
tile_size = 25
background_color = Color(24)
pause_overlay_color = Color(88, 127)

paused = False

head = Vector(tiles // 2, tiles // 2)
velocity = Vector(0, 0)
tail = []
tail_size = 5
snake_color = Color(161, 181, 108)

food = Vector(int(random_uniform(tiles)), int(random_uniform(tiles)))
food_color = Color(171, 70, 66)

def setup():
    size(tile_size * tiles, tile_size * tiles)
    title("p5 Snake")

    no_stroke()

def draw():
    global head
    global tail
    global tail_size
    global paused

    # Stop right here if the game is paused
    if paused:
        return

    background(background_color)

    fill(snake_color)
    for cell in tail:
        square(cell * tile_size, 0.8 * tile_size)

    head = head + velocity
    if head.x < 0:
        head.x = tiles - 1
    if head.x > tiles - 1:
        head.x = 0

    if head.y < 0:
        head.y = tiles - 1
    if head.y > tiles - 1:
        head.y = 0

    # Pause and reset the game when the snake eats itself.
    if head in tail:
        tail_size = 5
        tail = []
        paused = True

        fill(food_color.lerp(snake_color, 0.7))
        square(head * tile_size, 0.8 * tile_size)

    tail.append(head)
    if len(tail) > tail_size:
        extra_cells = len(tail) - tail_size
        tail = tail[extra_cells:]

    if head == food:
        fill(food_color.lerp(snake_color, 0.3))
        square(head * tile_size, 0.8 * tile_size)
        food.x = floor(random_uniform(0, tiles))
        food.y = floor(random_uniform(0, tiles))
        tail_size += 1

    fill(food_color)
    square(food * tile_size, 0.8 * tile_size)

    if paused:
        background(pause_overlay_color)

def key_pressed(event):
    global paused
    global velocity

    if event.key in ['UP', 'DOWN', 'RIGHT', 'LEFT', 'H', 'J', 'K', 'L']:
        paused = False
        if event.key == 'UP' or event.key == 'K':
            velocity.x = 0
            velocity.y = -1
        elif event.key == 'DOWN' or event.key == 'J':
            velocity.x = 0
            velocity.y = 1
        elif event.key == 'RIGHT' or event.key == 'L':
            velocity.x = 1
            velocity.y = 0
        elif event.key == 'LEFT' or event.key == 'H':
            velocity.x = -1
            velocity.y = 0
    elif event.key == 'SPACE':
        paused = not paused
        if paused:
            # Hide the food before drawing the overlay.
            fill(background_color)
            square(food * tile_size, 0.8 * tile_size)
            background(pause_overlay_color)

if __name__ == '__main__':
    run(frame_rate=15)
