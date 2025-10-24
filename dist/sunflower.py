from prototype import PREPARE, TEND, POS, SIZE
from utils import wait_for_seed, wait_for_harvest, move_to
from heapq import heappop, heappush

E = Entities.Sunflower
PQ = "priority queue"
def prepare(inst):
    x0, y0 = inst[POS]
    w, h = inst[SIZE]
    pq = inst[PQ]
    for i in range(w):
        for j in range(h):
            if can_harvest():
                harvest()
            
            if get_ground_type() != Grounds.Soil:
                till()

            wait_for_seed(E, 100)
            plant(E)

            heappush(pq, (-measure(), (get_pos_x(), get_pos_y())))
            move(North)
        for j in range(h):
            move(South)
        move(East)

    for i in range(w):
        move(West)

def tend(inst):
    pq = inst[PQ]
    _, pos = heappop(pq)
    move_to(pos)

    if not can_harvest():
        use_item(Items.Fertilizer)
        use_item(Items.Weird_Substance)
    wait_for_harvest(True)
    harvest()

    wait_for_seed(E, 100)
    plant(E)
    heappush(pq, (-measure(), (get_pos_x(), get_pos_y())))

# width, height in size should be positive
def create(pos, size):
    inst = {
        PREPARE: prepare,
        TEND: tend,

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