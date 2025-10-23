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

# width must be even and positive
def square_path_even(width):
    return rect_path_even((width, width))

# width must be even and positive
# height must be at least 2
# The path is supposed to traverse the whole rectangle once
# and then go back to the original position
def rect_path_even(size):
    width, height = size
    if not (width % 2 == 0 and width > 0 and height >= 2):
        quick_print("Error: invalid path. width must be even and positive and height must be at least 2")
        return []
    path = array_of(width-1, East) + [North]
    for i in range(width // 2):
        path += array_of(height-2, North) + [West]
        path += array_of(height-2, South) + [West]
    path[-1] = South
    return path

def clamp(size, max_size)
    return (min(size[0], max_size[0]), min(size[1], max_size[1]))

def verify_entity_cost(entity, reserve_multiplier):
    costs = get_cost(entity)
    for item in costs:
        if num_items(item) < costs[item] * reserve_multiplier:
            return False
    return True

def wait_for_seed(entity, reserve_multiplier):
    while not verify_entity_cost(entity, reserve_multiplier):
        # print takes 1 second, it waits like doing a flip
        print("Warning: Cannot afford seed for {}".format(entity))
        # do_a_flip()
