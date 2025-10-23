from prototype import POSITION, ENTITY, PREPARE, TEND

def create(pos):
    inst = {
        POSITION: pos,
        ENTITY: Entities.Grass,
    }
    
    # prepare the current cell
    def prepare():
        entity = get_entity_type()
        if can_harvest():
            harvest()
        
        if get_ground_type() == Grounds.Soil:
            till()
    inst[PREPARE] = prepare

    def tend():
        if can_harvest():
            harvest()
    inst[TEND] = tend

    return inst

def test():
    obj = create(pos=(0, 0))
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()