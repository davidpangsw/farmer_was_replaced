from utils import reverse_direction, reverse_path, snake_path
from prototype import POSITION, ENTITY, PREPARE, TEND, SIZE

IS_SORTED = "is_sorted"
def create(pos, size):
    inst = {
        POSITION: pos,
        ENTITY: Entities.CACTUS,
        SIZE: size,
    }

    FORWARD_PATH = snake_path(size, East)
    BACKWARD_PATH = snake_path(size, South)

    def swap_dir(dir, prev_measure):
        is_swapped = False
        m = measure()
        if dir in [West, South]:
            if m < prev_measure:
                swap(dir)
                is_swapped = True
                m = prev_measure
        else: # prev_d in [East, North]
            if m > prev_measure:
                swap(dir)
                is_swapped = True
                m = prev_measure
        return is_swapped, m

    def tend_cell(prev_d, prev_measure):
        if prev_d == None:
            m = measure()
        else:
            is_swapped, m = swap_dir(reverse_direction(prev_d), prev_measure)
            if is_swapped:
                inst[IS_SORTED] = False
        return m

    def prepare():
        inst[IS_SORTED] = True
        prev_d, prev_measure = None, -1
        for d in FORWARD_PATH:
            if can_harvest():
                harvest()
            
            if get_ground_type() != Grounds.Soil:
                till()

            plant(inst[ENTITY])

            m = tend_cell()
            prev_measure, prev_d = m, d
            move(d)
        
        prev_d, prev_measure = None, -1
        for d in BACKWARD_PATH:
            m = tend_cell()
            prev_measure, prev_d = m, d
            move(d)
    inst[PREPARE] = prepare

    def tend():
        # we can assume the whole farm is planted with cactus

        prev_d, prev_measure = None, -1
        while True:
            inst[IS_SORTED] = True
            for d in FORWARD_PATH:
                m = tend_cell()
                prev_measure, prev_d = m, d
                move(d)
            
            for d in BACKWARD_PATH:
                m = tend_cell()
                prev_measure, prev_d = m, d
                move(d)
            
            if inst[IS_SORTED]:
                break
        
        harvest()
    inst[TEND] = tend

    return inst

def test():
    obj = create(pos=(0, 0), size=(10, 10))
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()