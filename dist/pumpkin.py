from utils import rect_path_even, reverse_path, wait_for_seed
from prototype import PREPARE, TEND, SIZE


MIN_WATER = 5000
MIN_WATER_LEVEL = 0.5
MIN_FERTILIZER = 5000
E = Entities.Pumpkin
def create(width):
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, width)
    inst = {
        SIZE: size,
    }

    PATH = rect_path_even(size)
    PATH_BACK = reverse_path(PATH)


    def prepare():
        for d in PATH:
            if can_harvest():
                harvest()
            
            if get_ground_type() != Grounds.Soil:
                till()
            move(d)
        
        harvest()
    inst[PREPARE] = prepare

    def tend():
        # While seeds are shared among different drones,
        # 500 * width * width is more than enough. (And hopefully not exhausted in the middle of tending)
        # TODO: any better approach?
        wait_for_seed(E, 500 * width * width)

        # we can assume the whole farm is empty (tilled soil)
        for d in PATH:
            plant(E)
            move(d)
        
        for d in PATH_BACK:
            while not can_harvest():
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
                    do_a_flip()
            
            move(d)
        
        harvest()
    inst[TEND] = tend

    return inst

def test():
    obj = create(width=6)
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()