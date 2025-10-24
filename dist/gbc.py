# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

from prototype import PREPARE, TEND, POS
import grass
import bush
import carrot
from utils import wait_for_harvest

G = Entities.Grass
B = Entities.Bush
C = Entities.Carrot
GBC = [G, B, C]

def decide_to_plant(inst, poly):
    # decide which one to plant
    # if low on Hay, plant Grass
    if num_items(Items.Hay) < num_items(Items.Wood):
        return G
    # if low on Wood, plant bush
    elif num_items(Items.Wood) < num_items(Items.Carrot):
        return B
    # if low on Carrot, plant Carrot
    elif num_items(Items.Carrot) < num_items(Items.Pumpkin):
        return C
    # if polyculture has suggestion, plant base on it
    elif poly != None:
        return poly
    # else, randomly choose from [G, B, C]
    else:
        return GBC[int(random() * 3)]

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
    to_plant = decide_to_plant(inst, poly)
    if to_plant == G:
        grass.prepare(grass.create(pos))
    elif to_plant == B:
        bush.prepare(bush.create(pos))
    else: # C
        carrot.prepare(carrot.create(pos))

def create(pos):
    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
    }

    return inst

def test():
    clear()
    inst = create((get_pos_x(), get_pos_y()))
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()