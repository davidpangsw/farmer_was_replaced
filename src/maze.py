from prototype import PREPARE, TEND, POS
from utils import matrix_of, move_to, sqrt_floor
from utils import DIRECTIONS, DIRECTION_TO_VECTOR, DIRECTION_REVERSE_MAP
from drone import spawn_drone_main, drone_main
from dev import (
    Entities, Items, Unlocks, North, East,
    get_entity_type, can_move, move, get_pos_x, get_pos_y,
    can_harvest, harvest, plant, use_item, num_unlocked, clear
)

WIDTH = "width"

def dfs(size, visited, i, j):
    if get_entity_type() == Entities.Treasure:
        return True
    
    visited[i][j] = True
    
    for dir in DIRECTIONS:
        if not can_move(dir):
            continue
        dx, dy = DIRECTION_TO_VECTOR[dir]
        i1, j1 = i+dx, j+dy
        if not (0 <= i1 and i1 < size[0] and 0 <= j1 and j1 < size[1]):
            continue
        if visited[i1][j1]:
            continue
        move(dir)
        success = dfs(size, visited, i1, j1)
        if success:
            return True
        move(DIRECTION_REVERSE_MAP[dir])
    
    return False


def search(inst):
    pos = inst[POS]
    width = inst[WIDTH]

    size = (width, width)
    visited = matrix_of(size, False)
    dfs(size, visited, get_pos_x() - pos[0], get_pos_y() - pos[1])

def prepare(inst):
    for _ in range(10):
        print("Waiting...")
    pos = inst[POS]
    width = inst[WIDTH]

    move_to((pos[0] + width // 2, pos[1] + width // 2))
    if can_harvest():
        harvest()

def tend(inst):
    pos = inst[POS]
    width = inst[WIDTH]

    plant(Entities.Bush)
    substance = width * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    search(inst)
    harvest()
    move_to((pos[0] + width // 2, pos[1] + width // 2))

def create(pos, width):
    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        WIDTH: width,
    }
    return inst


def test():
    clear()
    L = 32
    width = 6
    for x in range(0, L + 1 - width, width):
        for y in range(0, L + 1 - width, width):
            inst = create((x, y), width)
            spawn_drone_main(inst)
            move(North)
        move(East)

if __name__ == "__main__":
    test()