
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
    # return hamilton_2(size)
    ax, ay = apple_pos[0] - pos[0], apple_pos[1] - pos[1]
    w, h = size
    l = snake_length
    L = get_world_size()

    if ay == 0: # treated as (0, 1), handle exceptional case when snake too short
        k = ceildiv(l - 1, 2 * (h - 1))
        k = min(k, 1)
        w = 2 * k
        if ax >= w:
            w = ax
            if w % 2 == 1:
                w += 1
        return hamilton((min(w, L), h))
    else:
        k = ceildiv(l - ay, 2 * (h - 1))
        k = min(k, 1)
        if ax % 2 == 0:
            w = ax + 2 * k
        else:
            w = ax + 2 * k + 1
        return hamilton((min(w, L), h))
    