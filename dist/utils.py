DIRECTION_REVERSE_MAP = {
    East: West,
    North: South,
    West: East,
    South: North,
}

def reverse_direction(d):
    return DIRECTION_REVERSE_MAP[d]

def reverse_path(path):
    result = []
    for d in path[::-1]:
        result.append(reverse_direction(d))
    return result

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