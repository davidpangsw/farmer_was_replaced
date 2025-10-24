from prototype import PREPARE, TEND, POS

E = Entities.Tree

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