from utils import square_path_even

E = Entities.Cactus
IS_GROWN = "is_grown"
IS_SORTED = "is_sorted"
POS = "position"
SIZE = "size"
PATH = "path"

def bubble(inst):
    pos = inst[POS]
    size = inst[SIZE]

    if not can_harvest():
        inst[IS_GROWN] = False

    if get_pos_x() < pos[0] + size[0] - 1:
        dir = East
        if measure() > measure(dir):
            swap(dir)
            inst[IS_SORTED] = False

    if get_pos_y() < pos[1] + size[1] - 1:
        dir = North
        if measure() > measure(dir):
            swap(dir)
            inst[IS_SORTED] = False

def prepare(inst):
    path = inst[PATH]

    inst[IS_GROWN] = False
    inst[IS_SORTED] = False
    for d in path:
        if can_harvest():
            harvest()

        if get_ground_type() != Grounds.Soil:
            till()

        plant(E)

        move(d)

def tend(inst):
    path = inst[PATH]

    # bubble sort
    inst[IS_GROWN] = True
    inst[IS_SORTED] = True
    for d in path:
        bubble(inst)
        move(d)

    if inst[IS_GROWN] and inst[IS_SORTED]:
        harvest()

        # replant
        # no need to till, must be empty soil
        inst[IS_GROWN] = False
        inst[IS_SORTED] = False
        for d in path:
            plant(E)
            move(d)

def create_square(width):
    if width % 2 == 1:
        quick_print("Error: width is not even, increased by 1")
        width += 1
    size = width, width
    pos = get_pos_x(), get_pos_y()

    path = square_path_even(width)
    inst = {
        POS: pos,
        SIZE: size,
        PATH: path,
    }

    return inst

def test():
    inst = create_square(width=10)
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()