from prototype import PREPARE, TEND
from utils import wait_for_seed

E = Entities.Carrot
def create():
    inst = {
    }

    def prepare():
        if can_harvest():
            harvest()
        
        if get_ground_type() != Grounds.Soil:
            till()

        wait_for_seed(E, 100)
        plant(E)
    inst[PREPARE] = prepare

    def tend():
        if can_harvest():
            harvest()
            wait_for_seed(E, 100)
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