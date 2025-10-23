# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

import grass
import bush
import tree
import carrot
from prototype import PREPARE, TEND

G = Entities.Grass
B = Entities.Bush
T = Entities.Tree
C = Entities.Carrots

MIN_ITEMS = {
    Items.Hay:1000,
    Items.Wood:1000,
    Items.Carrot:1000,
}

def create_gbc():
    inst = {}

    def prepare():
        if can_harvest():
            harvest()
        
        if get_ground_type() == Grounds.Soil:
            till()
    inst[PREPARE] = prepare

    def tend():
        if can_harvest():
            harvest()
        
        # decide which one to plant (base on num_items and polyculture)
        # if low on Hay, plant Grass
        if num_items(Items.Hay) < MIN_ITEMS(Items.Hay):
            # if low on Wood, plant bush
            inst = bush.create()
            bush.prepare(inst)
            bush.plant(inst)
        elif num_items(Items.Wood) < MIN_ITEMS(Items.Wood):
        # if low on Carrot, plant Carrot
        elif num_items(Items.Carrot) < MIN_ITEMS(Items.Carrot):
        # if polyculture has suggestion, plant base on it
        elif poly[i][j] != None:
        # else, plant grass anyway
        else:
            pass
    inst[TEND] = tend

# Width must be even (if odd, it is increased by 1)
# size must be smaller than or equal to world size
def create(size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)

    PATH = rect_path_even(size)
    inst = {
    }

    def prepare():
        x0, y0 = get_pos_x(), get_pos_y()
        for d in PATH:
            x, y = get_pos_x(), get_pos_y()
            i, j = x - x0, y - y0
            if (i + j) % 2 == 0:
                if can_harvest():
                    harvest()
                
                # Only two ground type, no need. (May have more in future updates?)
                # if get_ground_type() not in [Grounds.Turf, Grounds.Soil]:
                #     till()
                    
                if not plant(E):
                    quick_print("Error: unable to plant")
            else:
                odd_inst[PREPARE]()

            move(d)
    inst[PREPARE] = prepare

    def tend():
        x0, y0 = get_pos_x(), get_pos_y()
        for d in PATH:
            x, y = get_pos_x(), get_pos_y()
            i, j = x - x0, y - y0
            if (i + j) % 2 == 0:
                if can_harvest():
                    harvest()
                plant(E)
            else:
                odd_inst[TEND]()

            move(d)
    inst[TEND] = tend

    return inst

def test():
    import bush
    odd_inst = bush.create()
    obj = create(size=(10, 10), odd_inst=odd_inst)
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()