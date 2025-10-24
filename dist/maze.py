from prototype import PREPARE, TEND, POS
from utils import matrix_of, move_to
from utils import DIRECTIONS, DIRECTION_TO_VECTOR, DIRECTION_REVERSE_MAP

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
    width = inst[WIDTH]
    size = (width, width)
    visited = matrix_of(size, False)
    dfs(size, visited, 0, 0)

def prepare(inst):
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
    move_to(pos)

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
    inst = create((get_pos_x(), get_pos_y()), 10)
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()