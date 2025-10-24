from utils import move_to
from prototype import POS, PREPARE, TEND
def drone_main(inst):
    pos = inst[POS]
    prepare = inst[PREPARE]
    tend = inst[TEND]

    move_to(pos)
    prepare(inst)
    while True:
        tend(inst)

def spawn_drone_main(inst):
    def f():
        drone_main(inst)
    spawn_drone(f)