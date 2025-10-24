from utils import move_to, sqrt_floor
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

def split_world_squares(width=None):
    L = get_world_size()
    if width == None:
        D = max_drones()
        width = L // sqrt_floor(D)

    result = []
    for x in range(0, L - width, width):
        row = []
        for y in range(0, L - width, width):
            i, j = x // width, y // width
            row.append((x, y), width)
        result.append(row)
    return result