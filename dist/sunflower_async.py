from prototype import PREPARE, TEND, POS, SIZE, PATH
from utils import wait_for_seed, wait_for_harvest, move_to, rect_path_even
from drone import spawn_drone_main

E = Entities.Sunflower

CH_CTRL = "Channel of Control"
GET_CH_CTRL = "Get Channel of Control"
CTRL_STATE = "Control State" # None initially; -1 if planting; otherwise is the measure of petals to be collected
CTRL_NOTIFY = "Control Notify()" # receive id that notify it has completed the job and is waiting
CTRL_COUNT = "Control Count"
CTRL_TOTAL = "Control Total"
LEVEL_TO_XYS = "level to (x, y)'s"

globals = {
    CH_CTRL: {}
}

def get_ch_ctrl():
    return globals[CH_CTRL]

def wait_for_state_change(inst, prev_state):
    ctrl = inst[GET_CH_CTRL]()
    state = ctrl[CTRL_STATE]
    while state == prev_state:
        do_a_flip()
        state = ctrl[CTRL_STATE]

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
def create(pos, size, ch_ctrl):
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

        GET_CH_CTRL: get_ch_ctrl,
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
    wait_for_state_change(inst, None)

    # x0, y0 = inst[POS]
    # w, h = inst[SIZE]
    path = inst[PATH]
    ctrl = inst[GET_CH_CTRL]()
    for d in path:
        if can_harvest():
            harvest()
        
        if get_ground_type() != Grounds.Soil:
            till()

        wait_for_seed(E, 100)
        plant(E)
        add_measure(inst, measure(), (get_pos_x(), get_pos_y()))
        move(d)
    notify(ctrl)
    wait_for_state_change(inst, -1)

def tend(inst):
    ctrl = inst[GET_CH_CTRL]()
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
    notify(ctrl)

    # wait for state change
    wait_for_state_change(inst, state)

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

def create_ch_ctrl():
    ch_ctrl = {
        CTRL_STATE: None,
        CTRL_COUNT: None,
        CTRL_TOTAL: None,
    }
    ch_ctrl[CTRL_NOTIFY] = notify

    return ch_ctrl

# Only call this after state, that is, state cannot be None
def notify(ch_ctrl):
    ch_ctrl[CTRL_COUNT] -= 1
    if ch_ctrl[CTRL_COUNT] > 0:
        return
    ch_ctrl[CTRL_COUNT] = ch_ctrl[CTRL_TOTAL]

    # switch state
    state = ch_ctrl[CTRL_STATE]
    if state == -1: # to planting state
        ch_ctrl[CTRL_STATE] = 15
    else: # level harvested
        if state == 7:
            ch_ctrl[CTRL_STATE] = -1
        else:
            ch_ctrl[CTRL_STATE] -= 1    

def test():
    clear()

    L = get_world_size()
    width = 8
    ch_ctrl = create_ch_ctrl()

    count = 0
    for x in range(0, L + 1 - width, width):
        for y in range(0, L + 1 - width, width):
            inst = create((x, y), (width, width), ch_ctrl)
            d = spawn_drone_main(inst)
            if d:
                count += 1
    ch_ctrl[CTRL_COUNT] = count
    ch_ctrl[CTRL_TOTAL] = count
    ch_ctrl[CTRL_STATE] = -1

    # main drone just stay (We have more than enough drones)
if __name__ == "__main__":
    test()