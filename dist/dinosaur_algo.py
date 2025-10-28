

def generate_snake_path(size):
    width, height = size
    path = []

    # Step 1: Move East to (width-1, 0)
    for _ in range(width - 1):
        path.append(East)

    # Step 2: Move North to (width-1, height-1)
    for _ in range(height - 1):
        path.append(North)

    # Step 3: Move West by 1 to (width-2, height-1)
    path.append(West)

    # Step 5: Do the curling pattern
    d = height - 2
    k = (width / 2) // d

    for _ in range(k):
        # South by d
        for _ in range(d):
            path.append(South)
        # West by 1
        path.append(West)
        # North by d
        for _ in range(d):
            path.append(North)
        # West by 1
        path.append(West)

    # Step 6: Now at (0, height-1)
    # Step 7: Move South to (0, 0)
    for _ in range(height - 1):
        path.append(South)

    return path


def calculate_dimensions(pos, apple_pos, size, snake_length):
    W, H = size
    ax, ay = (apple_pos[0] - pos[0], apple_pos[1] - pos[1])
    length = snake_length

    height = H - 1

    area = length + (ay - 1)
    q, r = area // height, area % height
    if r != 0:
        q += 1
    width = q
    width += ax - 1

    return width, height

def decide_path(pos, apple_pos, size, snake_length):
    width, height = calculate_dimensions(pos, apple_pos, size, snake_length)
    return generate_snake_path(width, height)