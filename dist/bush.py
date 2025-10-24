E = Entities.Bush
POS = "position"

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