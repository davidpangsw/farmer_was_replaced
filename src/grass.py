from prototype import PREPARE, TEND, POS
from dev import Entities, Grounds, can_harvest, harvest, get_ground_type, till, clear, get_pos_x, get_pos_y

E = Entities.Grass

def prepare(inst):
    if can_harvest():
        harvest()

    if get_ground_type() == Grounds.Soil:
        till()

def tend(inst):
    if can_harvest():
        harvest()

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