# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

from prototype import PREPARE, TEND, POS
import grass
import bush
import carrot
from utils import wait_for_harvest
from dev import Entities, Grounds, can_harvest, harvest, get_ground_type, till, get_pos_x, get_pos_y, clear

G = Entities.Grass
B = Entities.Bush
C = Entities.Carrot
GBC = [G, B, C]

def prepare(inst):
    if can_harvest():
        harvest()
    
    if get_ground_type() == Grounds.Soil:
        till()
        
def tend(inst, to_plant):
    # We can assume the tile is either planting G,B, or C
    # In any case, it should be safe to wait until harvest
    wait_for_harvest()

    pos = (get_pos_x(), get_pos_y())
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
        tend(inst, G)

if __name__ == "__main__":
    test()