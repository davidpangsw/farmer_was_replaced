# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

import grass
import bush
import carrot
from utils import wait_for_harvest

G = Entities.Grass
B = Entities.Bush
C = Entities.Carrots
GBC = [G, B, C]
POS = "position"
MIN_ITEMS = {
    Items.Hay:1000,
    Items.Wood:1000,
    Items.Carrot:1000,
}

def decide_to_plant(inst, poly):
    # decide which one to plant
    # if low on Hay, plant Grass
    if num_items(Items.Hay) < MIN_ITEMS(Items.Hay):
        return G
    # if low on Wood, plant bush
    elif num_items(Items.Wood) < MIN_ITEMS(Items.Wood):
        return B
    # if low on Carrot, plant Carrot
    elif num_items(Items.Carrot) < MIN_ITEMS(Items.Carrot):
        return C
    # if polyculture has suggestion, plant base on it
    elif poly != None:
        return poly
    # else, randomly choose from [G, B, C]
    else:
        return GBC[random() * 3]

def prepare(inst):
    if can_harvest():
        harvest()
    
    if get_ground_type() == Grounds.Soil:
        till()
        
def tend(inst, poly=None):
    # We can assume the tile is either planting G,B, or C
    # In any case, it should be safe to wait until harvest
    wait_for_harvest()

    pos = (get_pos_x(), get_pos_y())
    to_plant = decide_to_plant(poly)
    if to_plant == G:
        grass.prepare(grass.create(pos))
    elif to_plant == B:
        bush.prepare(bush.create(pos))
    else: # C
        carrot.prepare(carrot.create(pos))

def create(pos):
    inst = {
        POS: pos,
    }

    return inst

def test():
    inst = create((get_pos_x(), get_pos_y()))
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()