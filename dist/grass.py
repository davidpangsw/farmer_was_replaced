E = Entities.Grass

def prepare(inst):
    if can_harvest():
        harvest()

    if get_ground_type() == Grounds.Soil:
        till()

def tend(inst):
    if can_harvest():
        harvest()

def create():
    inst = {
    }

    return inst

def test():
    inst = create()
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()