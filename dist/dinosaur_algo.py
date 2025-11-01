
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
    L = get_world_size()
    ax, ay = apple_pos[0] - pos[0], apple_pos[1] - pos[1] # note: can be negative
    ax, ay = ax % L, ay % L
    length = snake_length

    height = L
    width = ceildiv(length, height)
    if width % 2 == 1:
        width += 1

    if ax > width:
        # at (0, 0)
        path = right(ax + 1 - width) # (ax + 1 - width, 0)
        path += generate_snake_path((width, height)) # (ax + 1, 0)
    else: # ax <= width
        width = ax + 1
        if width % 2 == 1:
            width += 1
        path = generate_snake_path((width, height))
    return path
    