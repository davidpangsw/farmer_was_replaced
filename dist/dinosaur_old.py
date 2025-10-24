from prototype import POS, SIZE
from utils import rect_path_even, move_to, is_contain

PATH = "path"
PATH_INDEX = "path_index"
COUNT = "count"
def step(inst):
    path = inst[PATH]
    index = inst[PATH_INDEX]
    success = move(path[index])
    inst[PATH_INDEX] = (index + 1) % len(path)
    return success

def prepare():
    change_hat(Hats.Dinosaur_Hat)
    step(inst)
    

def tend(inst):
    pos = inst[POS]
    size = inst[SIZE]
    m = measure()
    if is_contain(pos, size, m):
        while (get_pos_x(), get_pos_y()) != m:
            step(inst)
        step(inst)
        inst[COUNT] += 1
        if inst[COUNT] == len(inst[PATH]):
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)
            inst[COUNT] = 0

def create():
    pass


def test():
    clear()
    set_world_size(6)
    L = get_world_size()
    size = L, L
    path = rect_path_even(size)
    change_hat(Hats.Dinosaur_Hat)
    while True:
        for d in path:
            success = move(d)
            if not success:
                change_hat(Hats.Gold_Hat)
                change_hat(Hats.Dinosaur_Hat)
                move(d)

if __name__ == "__main__":
    test()