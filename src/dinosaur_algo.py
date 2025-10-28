"""
This program is implementing a snaking algorithm.
First of all, this is a classic game setup:
- There is a grid of unknown size, but it must be a square of even width. For simplicity, I will use width=16
- A snake of certain length (=1 initially) is moving in the grid. Each time it moves, the tail part is popped and head move forward by 1
- Apples randomly generated on the grid one by one, each time the snake eats an apple (moving from an apple grid to another grid), its length is grown by 1, and the apple is consumed.
- The algorithm aims to eat as many apples as possible, without colliding with snake's body.


# Assume the path would always be:
# Given height and width we are going to travel, width is even
# 0. Let say we are at the bottom left (x0, y0) = (0, 0) for simplicity
# 1. Move to the East to a certain distance (width - 1), now we are at (width - 1, 0)
# 2. Move North to a certain distance (height - 1), now we are at (width - 1, height - 1)
# 3. Move West by 1, now we are at (width - 2, height - 1)
# 4. Move West by (width - 2 - 2k), where k is in [0, (width - 2) / 2), now we are at (2k, height - 1)
# 5. Repeat k times, where d = (height - 2):
#   a. South by d, West by 1, North by d, West by 1
# 6. Now we are in (0, height - 1)
# 7. South by (height - 1)
# 8. We are back to (0, 0), path is done
# path params: pos=(x0, y0), size=(width, height)

# Now, assume we are at (x0, y0), we are given the target=apple position, and several parameters,
# we need to determine a path that goes to the apple and get back to (x0, y0)
# such that we can do that again for a new randomly appeared apple later
# Given L = world_size, and the world is a L*L grid

# Suppose (ax, ay) = apple position
# Our target is when the snake eats apples, it is not occupying any of the bottom row (thus any cell before returning (0, 0)), that it always has a return path.
# - For example:
#     - if the apple is at (3, 4), and the snake starts curling at (6, 0), the curls would accommodate (L-1) * (6-3) + 4 when it reaches the apple.
#     - if the apple is at (2, 4), and the snake starts curling at (6, 0), the curls would accommodate (L-1) * (6-2) + (L - 4) when it reaches the apple.
#     - The difference is because curling must start at even x, while apple can have even or odd x-coordinate.
#     - Sometimes it is impossible because the apple is at far East. In that case, curl starts at (L-1, 0), which is farthest it can start.
#     - After reaching the apple, simply curl back to the (0, 0) as usual
# Write a function that reads input and decides the path, returning an array of directions
"""
from dev import East, North, West, South

def generate_snake_path(width, height, curl_start_x):
    """
    Generate a snaking path from (0,0) that curls at curl_start_x and returns to (0,0).
    width must be even.
    curl_start_x must be even and in range [0, width-1].
    """
    path = []

    # Step 1: Move East to (width-1, 0)
    for _ in range(width - 1):
        path.append(East)

    # Step 2: Move North to (width-1, height-1)
    for _ in range(height - 1):
        path.append(North)

    # Step 3: Move West by 1 to (width-2, height-1)
    path.append(West)

    # Step 4: Move West to curl start position (curl_start_x, height-1)
    # We're at (width-2, height-1), need to reach (curl_start_x, height-1)
    west_moves = (width - 2) - curl_start_x
    for _ in range(west_moves):
        path.append(West)

    # Step 5: Do the curling pattern
    # Number of curls k = curl_start_x / 2
    k = curl_start_x // 2
    d = height - 2

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


def calculate_dimensions(apple_x, apple_y, world_size, snake_length):
    """
    Calculate the minimum width and curl start position needed to accommodate
    the snake when it reaches the apple.

    Returns: (width, height, curl_start_x)
    """
    L = world_size

    # Height is always L (we use full height)
    height = L

    # Find minimum width (must be even) and curl_start_x (must be even)
    # such that the path can accommodate snake_length when reaching apple

    # Try widths from apple_x+1 up to L, ensuring even width
    if (apple_x + 2) % 2 == 0:
        min_width = apple_x + 2
    else:
        min_width = apple_x + 3

    for width in range(min_width, L + 1, 2):  # Step by 2 to keep even
        # For this width, try curl_start positions from width-1 down to 0 (even only)
        for curl_x in range(width - 1, -1, -2):  # Start from rightmost even position
            if curl_x % 2 == 1:
                curl_x -= 1
            if curl_x < 0:
                curl_x = 0

            # Calculate how many cells are available when snake reaches apple
            if apple_x % 2 == 0:
                # Apple has even x-coordinate
                # Capacity: (L-1) * (curl_x - apple_x) + apple_y
                capacity = (L - 1) * (curl_x - apple_x) + apple_y
            else:
                # Apple has odd x-coordinate
                # Capacity: (L-1) * (curl_x - apple_x + 1) + (L - 1 - apple_y)
                capacity = (L - 1) * (curl_x - apple_x + 1) + (L - 1 - apple_y)

            if capacity >= snake_length:
                return (width, height, curl_x)

    # Fallback to full grid if nothing works
    return (L, L, 0)


def decide_path(apple_pos, world_size, snake_length):
    """
    Decide the path to take to eat the apple and return to origin.
    Uses MINIMUM width needed, not full world_size.

    Args:
        apple_pos: tuple (x, y) of apple position
        world_size: size of the square grid (L)
        snake_length: current length of the snake

    Returns:
        list of directions (East, North, West, South)
    """
    apple_x, apple_y = apple_pos

    # Calculate minimum dimensions needed
    width, height, curl_start_x = calculate_dimensions(apple_x, apple_y, world_size, snake_length)

    # Generate path with calculated dimensions
    path = generate_snake_path(width, height, curl_start_x)

    return path
