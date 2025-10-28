"""
This program is implementing a snaking algorithm.
First of all, this is a classic game setup:
- There is a grid of unknown size, but it must be a square of even width. For simplicity, I will use width=16
- A snake of certain length (=1 initially) is moving in the grid. Each time it moves, the tail part is popped and head move forward by 1
- Apples randomly generated on the grid one by one, each time the snake eats an apple (moving from an apple grid to another grid), its length is grown by 1, and the apple is consumed.
- The algorithm aims to eat as many apples as possible, without colliding with snake's body.


Assume the path would always be:
Given height and width we are going to travel, width is even
0. Let say we are at the bottom left (x0, y0) = (0, 0) for simplicity
1. Move to the East to a certain distance (width - 1), now we are at (width - 1, 0)
2. Move North to a certain distance (height - 1), now we are at (width - 1, height - 1)
3. Move West by 1, now we are at (width - 2, height - 1)
4. Move West by (width - 2 - 2k), where k is in [0, (width - 2) / 2), now we are at (2k, height - 1)
5. Repeat k times, where d = (height - 2):
  a. South by d, West by 1, North by d, West by 1
6. Now we are in (0, height - 1)
7. South by (height - 1)
8. We are back to (0, 0), path is done
path params: pos=(x0, y0), size=(width, height)
"""
from dev import East, North, West, South

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