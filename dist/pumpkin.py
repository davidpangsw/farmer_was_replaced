from utils import reverse_direction, reverse_path, rectangle_path
from prototype import POSITION, ENTITY, PREPARE, TEND, SIZE

def create(pos, size):
    inst = {
        POSITION: pos,
        ENTITY: Entities.Pumpkin,

        SIZE: size,
    }

    FORWARD_PATH, BACKWARD_PATH = rectangle_path(size)


    def prepare():
        for d in FORWARD_PATH:
            if can_harvest():
                harvest()
            
            if get_ground_type() != Grounds.Soil:
                till()

            plant(inst[ENTITY])
            move(d)
        
        for d in BACKWARD_PATH:
            # if it is a dead pumpkin, replace

            # water, fertilize, wait until mature
            while not can_harvest():
                do_a_flip()
            
            move(d)
        
        harvest()
    inst[PREPARE] = prepare

    def tend():
        # we can assume the whole farm is empty (tilled soil)
        for d in FORWARD_PATH:
            plant(inst[ENTITY])
            move(d)
        
        for d in BACKWARD_PATH:
            # if it is a dead pumpkin, replace

            # water, fertilize, wait until mature
            while not can_harvest():
                do_a_flip()
            
            move(d)
        
        harvest()
    inst[TEND] = tend

    return inst

def test():
    obj = create(pos=(0, 0), size=(6, 6))
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()