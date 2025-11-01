
from utils import ceildiv
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
    