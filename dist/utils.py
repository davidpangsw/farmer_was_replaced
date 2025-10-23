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

def array_of(n, value):
    arr = []
    for i in range(n):
        arr.append(value)
    return arr

def matrix_of(size, value):
    matrix = []
    for i in range(size[0]):
        row = []
        for j in range(size[1]):
            row.append(value)
        matrix.append(row)
    return matrix

def reverse_direction(d):
    return DIRECTION_REVERSE_MAP[d]

def reverse_path(path):
    result = []
    for d in path[::-1]:
        result.append(reverse_direction(d))
    return result

# size must be even
def square_path_even(size):
    path = array_of(size-1, East) + [North]
    for i in range(size // 2):
        path += array_of(size-2, North) + [West]
        path += array_of(size-2, South) + [West]
    path[-1] = South
    return path
    