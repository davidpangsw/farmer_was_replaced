from prototype import POSITION, ENTITY, PREPARE, TEND, SIZE

def create(pos, size, odd_inst):
    inst = {
        POSITION: pos,
        ENTITY: Entities.Tree,
        SIZE: size,
    }

    def prepare():
        if can_harvest():
            harvest()
        
        plant(inst[ENTITY])
    inst[PREPARE] = prepare

    def tend():
        if can_harvest():
            harvest()
            plant(inst[ENTITY])
    inst[TEND] = tend

    return inst

def test():
    obj = create(pos=(0, 0))
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()