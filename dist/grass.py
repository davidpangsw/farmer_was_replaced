from prototype import PREPARE, TEND

E = Entities.Grass
def create():
    inst = {
    }
    
    # prepare the current cell
    def prepare():
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
    obj = create()
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()