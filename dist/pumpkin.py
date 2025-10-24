from prototype import PREPARE, TEND, POS
from utils import rect_path_even, reverse_path, wait_for_seed
from drone import spawn_drone_main, drone_main
import sunflower
import gbtc

MIN_WATER = 5000
MIN_WATER_LEVEL = 0.5
MIN_FERTILIZER = 5000
E = Entities.Pumpkin
WIDTH = "width"
PATH = "path"
PATH_BACK = "path_back"

def prepare(inst):
    path = inst[PATH]

    for d in path:
        if can_harvest():
            harvest()

        if get_ground_type() != Grounds.Soil:
            till()
        move(d)

    harvest()

def tend(inst):
    path = inst[PATH]
    path_back = inst[PATH_BACK]
    width = inst[WIDTH]

    # While seeds are shared among different drones,
    # 500 * width * width is more than enough. (And hopefully not exhausted in the middle of tending)
    # TODO: any better approach?
    wait_for_seed(E, 500 * width * width)

    # we can assume the whole farm is empty (tilled soil)
    for d in path:
        plant(E)
        move(d)

    is_ready = False
    while not is_ready:
        is_ready = True
        for d in path:
            if not can_harvest():
                is_ready = False

                # if it is a dead pumpkin, replace
                if get_entity_type() == Entities.Dead_Pumpkin:
                    plant(E)

                # water, if water level is low and we have water
                if get_water() < MIN_WATER_LEVEL and num_items(Items.Water) > MIN_WATER:
                    use_item(Items.Water)
                # fertilize, if we have fertilizer
                elif num_items(Items.Fertilizer) > MIN_FERTILIZER:
                    use_item(Items.Fertilizer)
                # wait
                else:
                    pass

            move(d)

    harvest()

def create(pos, width):
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, width)

    path = rect_path_even(size)
    path_back = reverse_path(path)

    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        WIDTH: width,
        PATH: path,
        PATH_BACK: path_back,
    }

    return inst

def test():
    clear()
    
    L = get_world_size()
    D = max_drones()
    width = 6 # max at 6

    X = 0
    for x in range(0, L + 1- width, width):
        for y in range(0, L + 1 - width, width):
            i, j = x // width, y // width
            if (i + j) % 2 == 0:
                inst = create((x, y), width)
            else:
                inst = gbtc.create((x, y), (width, width))
            spawn_drone_main(inst)
        X = x + width
    inst  = sunflower.create((X, 0), (L-X, L))
    drone_main(inst)
    
    

if __name__ == "__main__":
    test()