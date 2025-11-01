
def up(n):
    arr = []
    for _ in range(n):
        arr.append(North)
    return arr
def down(n):
    arr = []
    for _ in range(n):
        arr.append(South)
    return arr
def left(n):
    arr = []
    for _ in range(n):
        arr.append(West)
    return arr
def right(n):
    arr = []
    for _ in range(n):
        arr.append(East)
    return arr

def snake(size):
    width, height = size

    # (0, 0)
    path = []
    for x in range(width // 2):
        # (x, 0)
        path += up(height - 1) # (x, h-1)
        path += right(1) # (x+1, h-1)
        path += down(height -1) # (x+1, 0)
        path += right(1) # (x+2, 0)
    # (2(w // 2), 0)

    return path

def hamilton(size):
    # (0, 0)
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: Cannot create hamilton cycle with odd width. Added one")
        width += 1
    path = right(1) # (1, 0) 
    path += snake((width - 2, height - 1)) # (width-1, 0)
    path += up(height-1) # (width-1, height-1)
    path += left(width-1) # (0, height-1)
    path += down(height-1) # (0, 0)
    return path
