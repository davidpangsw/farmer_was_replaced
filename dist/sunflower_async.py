from prototype import PREPARE, TEND, POS, SIZE, PATH
from utils import wait_for_seed, wait_for_harvest, move_to, rect_path_even
from drone import spawn_drone_main

E = Entities.Sunflower

STATE = "Control State" # -1 if planting; otherwise is the measure of petals to be collected
LEVEL_TO_XYS = "level to (x, y)'s"

def add_measure(inst, measure, pos):
    inst[LEVEL_TO_XYS][measure].append(pos)
def pop_measure(inst, measure):
    l = inst[LEVEL_TO_XYS][measure]
    if l:
        return l.pop()
    else:
        return None

# width, height in size should be positive
# width should be even
def create(pos, size):
    w, h = size
    if w % 2 == 1:
        w -= 1
        quick_print("Warning: width not even, decreased by 1")
        size = w, h
    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        SIZE: size,
        PATH: rect_path_even(size),
        STATE: -1,
    }
    # measure() must be in [7, 15], so no worry
    inst[LEVEL_TO_XYS] = {
        15: [],
        14: [],
        13: [],
        12: [],
        11: [],
        10: [],
         9: [],
         8: [],
         7: [],
    }
    return inst

def prepare(inst):
    # x0, y0 = inst[POS]
    # w, h = inst[SIZE]
    path = inst[PATH]
    for d in path:
        if can_harvest():
            harvest()
        
        if get_ground_type() != Grounds.Soil:
            till()

        wait_for_seed(E, 100)
        plant(E)
        add_measure(inst, measure(), (get_pos_x(), get_pos_y()))
        move(d)

def tend(inst):
    state = ctrl[CTRL_STATE]

    if state == -1:
        replant(inst)
    else:
        pos = pop_measure(inst, state)
        while pos != None:
            move_to(pos)

            if not can_harvest():
                use_item(Items.Fertilizer)
                use_item(Items.Weird_Substance)
            wait_for_harvest(True)
            harvest()
            pos = pop_measure(inst, state)
    return True # notify caller to finish the farming

def replant(inst):
    x0, y0 = inst[POS]
    # w, h = inst[SIZE]
    path = inst[PATH]

    move_to((x0, y0))
    for d in path:
        if get_entity_type() == Entities.Sunflower:
            pass
        else:
            wait_for_seed(E, 100)
            plant(E)
            add_measure(inst, measure(), (get_pos_x(), get_pos_y()))
        move(d)

def test():
    clear()

    L = 32
    width, height = 8, 4
    I, J = L // width, L // height # 4, 8
    
    count = 0
    insts = []
    for i in range(I):
        insts.append([])
        for j in range(J):
            x, y = i * width, j * height
            inst = create((x, y), (width, height))
            insts[i].append(inst)
            count += 1



if __name__ == "__main__":
    test()