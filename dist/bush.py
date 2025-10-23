E = Entities.Bush

def prepare(inst):
    if can_harvest():
        harvest()

    plant(E)

def tend(inst):
    if can_harvest():
        harvest()
        plant(E)

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