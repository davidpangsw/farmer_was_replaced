DIRECTION_REVERSE_MAP = {
    East: West,
    North: South,
    West: East,
    South: North,
}

DIRECTION_90_MAP = {
    East: North,
    North: West,
    West: South,
    South: East,
}

def reverse_direction(d):
    return DIRECTION_REVERSE_MAP[d]

def reverse_path(path):
    result = []
    for d in path[::-1]:
        result.append(reverse_direction(d))
    return result

def snake_path(size, dir):
    path = []
    for i in range(size[0] - 1)
        path += [dir] * (size[1] - 1) + [DIRECTION_90_MAP(dir)]
        dir = reverse_direction(dir)
    path += [dir] * (size[1] - 1)

    path += [None]
    return path

def rectangle_path(size):
    forward = []
    dir = North
    for i in range(size[0] - 1)
        forward += [dir] * (size[1] - 1) + [East]
        dir = reverse_direction(dir)
    forward += [dir] * (size[1] - 1)
    backward = reverse_path(forward)

    forward += [None]
    backward += [None]
    return forward, backward