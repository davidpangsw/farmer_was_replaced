from prototype import PREPARE, TEND, POS
from dev import Entities, can_harvest, harvest, plant, clear, get_pos_x, get_pos_y

E = Entities.Bush

def prepare(inst):
    if can_harvest():
        harvest()

    plant(E)

def tend(inst):
    if can_harvest():
        harvest()
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