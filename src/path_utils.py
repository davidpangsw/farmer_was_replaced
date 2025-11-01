from dev import East, South, West, North
from dev import get_world_size

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
    path = up(height - 1)

    for x in range(width // 2):
        path += up(height - 1)
        path += right(1)
        path += down(height -1)
        path += right(1)

    return path

def hamilton(L):
    # (0, 0)
    path = right(1) # (1, 0) 
    path += snake((L - 2, L - 1)) # (L-1, 0)
    path += up(L-1)
    path += left(L-1)
    path += down(L-1)
    return path
