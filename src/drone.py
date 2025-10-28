from utils import move_to, sqrt_floor
from prototype import POS, PREPARE, TEND
from dev import spawn_drone
def drone_main(inst):
    pos = inst[POS]
    prepare = inst[PREPARE]
    tend = inst[TEND]

    move_to(pos)
    prepare(inst)
    stop = None
    while stop == None:
        stop = tend(inst)

# Note: suppose drones are threadsafe: they work concurrently, but only one at a time
# inst is made a copy here (local variable)
def spawn_drone_main(inst):
    def f():
        drone_main(inst)
    return spawn_drone(f)
