from prototype import PREPARE, TEND, POS, SIZE
from utils import wait_for_seed, wait_for_harvest, move_to, rect_path_even
from heapq import heappop, heappush

E = Entities.Sunflower
PQ = "priority queue"
PATH = "path"
def prepare(inst):
    x0, y0 = inst[POS]
    w, h = inst[SIZE]
    pq = inst[PQ]
    path = inst[PATH]
    for d in path:
        if can_harvest():
            harvest()
        
        if get_ground_type() != Grounds.Soil:
            till()

        wait_for_seed(E, 100)
        plant(E)
        heappush(pq, (-measure(), (get_pos_x(), get_pos_y())))
        move(d)

def replant(inst):
    x0, y0 = inst[POS]
    w, h = inst[SIZE]
    pq = inst[PQ]
    path = inst[PATH]

    move_to((x0, y0))
    for d in path:
        if get_entity_type() == Entities.sunflower:
            pass
        else:
            wait_for_seed(E, 100)
            plant(E)
            heappush(pq, (-measure(), (get_pos_x(), get_pos_y())))
        move(d)

def tend(inst):
    pq = inst[PQ]
    if len(pq) < 10:
        replant(inst)
    _, pos = heappop(pq)
    move_to(pos)

    if not can_harvest():
        use_item(Items.Fertilizer)
        use_item(Items.Weird_Substance)
    wait_for_harvest(True)
    harvest()

    # plant back (slow, need to wait it grow)
    # wait_for_seed(E, 100)
    # plant(E)
    # heappush(pq, (-measure(), (get_pos_x(), get_pos_y())))

# width, height in size should be positive
# width should be even
def create(pos, size):
    w, h = size
    if w % 2 == 1:
        w -= 1
        Debug.log("Warning: width not even, decreased by 1")
        size = w, h
    inst = {
        PREPARE: prepare,
        TEND: tend,
        PATH: rect_path_even(size),

        POS: pos,
        SIZE: size,
        PQ: [],
    }

    return inst

def test():
    clear()
    inst = create((get_pos_x(), get_pos_y()), (10, 8))
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()