from prototype import PREPARE, TEND

E = Entities.Bush
def create():
    inst = {
    }

    def prepare():
        if can_harvest():
            harvest()
        
        plant(E)
    inst[PREPARE] = prepare

    def tend():
        if can_harvest():
            harvest()
            plant(E)
    inst[TEND] = tend

    return inst

def test():
    obj = create()
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()