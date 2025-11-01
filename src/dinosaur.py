from prototype import PREPARE, TEND, POS, SIZE, PATH
from utils import rect_path_even, reverse_path, wait_for_seed
from drone import spawn_drone_main, drone_main
from dinosaur_algo import decide_path
import sunflower
import gbtc
from dev import Entities, Hats, clear, get_pos_x, get_pos_y, get_entity_type, measure, move, change_hat, quick_print, max_drones, set_world_size

clear()

FULL_PATH = "full path"
LENGTH = "length"
APPLE_POS = "apple position"


def prepare(inst):
    change_hat(Hats.Dinosaur_Hat)
    # apple at the bottom, length is already 2
    inst[LENGTH] = 2
    inst[APPLE_POS] = measure()

def tend(inst):
    # cur_pos = get_pos_x(), get_pos_y()
    pos = inst[POS]
    apple_pos = inst[APPLE_POS]
    size = inst[SIZE]
    path = decide_path(pos, apple_pos, size, inst[LENGTH])
    for d in path:
        entity = get_entity_type() # see if it is apple
        if entity == Entities.Apple:
            inst[APPLE_POS] = measure()
            move(d) # must be success, because if the entity is an apple, it means we are at pos, and no tails are out there
            inst[LENGTH] += 1
        else:
            success = move(d)
            if not success:
                change_hat(Hats.Gold_Hat)
                wait_for_seed(Entities.Apple, 100)
                change_hat(Hats.Dinosaur_Hat)
                
                inst[APPLE_POS] = measure()
                move(d) # must be success, brand new game with apple under the drone
                inst[LENGTH] = 2

def create(pos, size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)

    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        SIZE: size,
        LENGTH: 0,
        FULL_PATH: rect_path_even(size),
    }

    return inst

def test():
    clear()
    
    # only one dinosaur is allowed
    L = 8
    set_world_size(L)
    pos = 0, 0
    size = (L, L)

    inst = create(pos, size)
    drone_main(inst)
    

if __name__ == "__main__":
    test()