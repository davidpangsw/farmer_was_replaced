
from prototype import PREPARE, TEND, POS, SIZE, PATH
from utils import rect_path_even, reverse_path, wait_for_seed
from drone import spawn_drone_main, drone_main
import sunflower
import gbtc

clear()

def prepare(inst):
    path = inst[PATH]
    change_hat(Hats.Dinosaur_Hat)

def tend(inst):
    path = inst[PATH]
    for d in path:
        success = move(d)
        if not success:
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)
            move(d)

def create(pos, size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, width)

    path = rect_path_even(size)

    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        SIZE: size,
        PATH: path,
    }

    return inst

def test():
    clear()
    
    # only one dinosaur is allowed
    L = get_world_size()
    D = max_drones()
    pos = 0, 0
    size = (8, 4)

    width, height = size
    inst = create(pos, size)
    drone_main(inst)
    

if __name__ == "__main__":
    test()