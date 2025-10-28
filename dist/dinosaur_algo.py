
from globals.constants import East, North, West, South


def generate_snake_path(width, height, curl_start_x):
    
    path = []

    # Step 1: Move East to (width-1, 0)
    path.extend([East] * (width - 1))

    # Step 2: Move North to (width-1, height-1)
    path.extend([North] * (height - 1))

    # Step 3: Move West by 1 to (width-2, height-1)
    path.append(West)

    # Step 4: Move West to curl start position (curl_start_x, height-1)
    # We're at (width-2, height-1), need to reach (curl_start_x, height-1)
    west_moves = (width - 2) - curl_start_x
    path.extend([West] * west_moves)

    # Step 5: Do the curling pattern
    # Number of curls k = curl_start_x / 2
    k = curl_start_x // 2
    d = height - 2

    for _ in range(k):
        # South by d
        path.extend([South] * d)
        # West by 1
        path.append(West)
        # North by d
        path.extend([North] * d)
        # West by 1
        path.append(West)

    # Step 6: Now at (0, height-1)
    # Step 7: Move South to (0, 0)
    path.extend([South] * (height - 1))

    return path


def calculate_dimensions(apple_x, apple_y, world_size, snake_length):
    
    L = world_size

    # Height is always L (we use full height)
    height = L

    # Find minimum width (must be even) and curl_start_x (must be even)
    # such that the path can accommodate snake_length when reaching apple

    # Try widths from apple_x+1 up to L, ensuring even width
    min_width = apple_x + 2 if (apple_x + 2) % 2 == 0 else apple_x + 3

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
    
    apple_x, apple_y = apple_pos

    # Calculate minimum dimensions needed
    width, height, curl_start_x = calculate_dimensions(apple_x, apple_y, world_size, snake_length)

    # Generate path with calculated dimensions
    path = generate_snake_path(width, height, curl_start_x)

    return path
