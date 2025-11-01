"""
This program is implementing a snaking algorithm.
First of all, this is a classic game setup:
- There is a grid of unknown size, but it must be a square of even width. For simplicity, I will use width=16
- A snake of certain length (=1 initially) is moving in the grid. Each time it moves, the tail part is popped and head move forward by 1
- Apples randomly generated on the grid one by one, each time the snake eats an apple (moving from an apple grid to another grid), its length is grown by 1, and the apple is consumed.
- The algorithm aims to eat as many apples as possible, without colliding with snake's body.


"""
from utils import ceildiv
from dev import get_world_size
from path_utils import up, down, left, right, hamilton, hamilton_2


def generate_snake_path(size):
    width, height = size
    path = []

    path += up(height - 1)

    for x in range(width // 2):
        path += up(height - 1)
        path += right(1)
        path += down(height -1)
        path += right(1)

    return path


def decide_path(pos, apple_pos, size, snake_length):
    return hamilton_2(size)
    ax, ay = apple_pos[0] - pos[0], apple_pos[1] - pos[1]
    l = snake_length
    w, h = size
    k = ceildiv(l - ay, 2 * (h - 1))

    if ax % 2 == 0:
        return hamilton((ax + 2*k, h))
    else:
        return hamilton((ax + 2*k +1, h))
    