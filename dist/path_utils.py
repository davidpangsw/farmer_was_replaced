
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
    w, h = size
    if w % 2 == 1:
        quick_print("Warning: Cannot create snake path with odd w. Added one")
        w += 1

    # (0, 0)
    path = []
    for x in range(w // 2):
        # (x, 0)
        path += up(h - 1) # (x, h-1)
        path += right(1) # (x+1, h-1)
        path += down(h -1) # (x+1, 0)
        path += right(1) # (x+2, 0)
    # (2(w // 2), 0)

    return path

def snake_opposite(size):
    w, h = size
    if w % 2 == 1:
        quick_print("Warning: Cannot create snake path with odd w. Added one")
        w += 1

    # (w-1, h-1)
    path = []
    for x in range(w // 2):
        # (x, h-1)
        path += down(h - 1) # (x, 0)
        path += left(1) # (x-1, 0)
        path += up(h -1) # (x-1, h-1)
        path += left(1) # (x-2, h-1)
    # (-1, h-1)

    return path

def hamilton(size):
    # (0, 0)
    w, h = size
    if w % 2 == 1:
        quick_print("Warning: Cannot create hamilton cycle with odd w. Added one")
        w += 1
    path = right(1) # (1, 0) 
    path += snake((w - 2, h - 1)) # (w-1, 0)
    path += up(h-1) # (w-1, h-1)
    path += left(w-1) # (0, h-1)
    path += down(h-1) # (0, 0)
    return path

def hamilton_2(size):
    # (0, 0)
    w, h = size
    if w % 2 == 1:
        quick_print("Warning: Cannot create hamilton cycle with odd w. Added one")
        w += 1
    path = right(w - 1) # (w - 1, 0)
    path += up(h - 1) # (w - 1, h - 1)
    path += left(1) # (w - 2, h - 1)
    path += snake_opposite((w - 2, h - 1)) # (0, h - 1)
    path += down(h - 1) # (1, 0)
    return path
