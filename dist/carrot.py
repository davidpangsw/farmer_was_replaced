from prototype import PREPARE, TEND, POS
from utils import wait_for_seed

E = Entities.Carrot
def prepare(inst):
    if can_harvest():
        harvest()
    
    if get_ground_type() != Grounds.Soil:
        till()

    wait_for_seed(E, 100)
    plant(E)

def tend(inst):
    if can_harvest():
        harvest()
        wait_for_seed(E, 100)
        plant(E)
        
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