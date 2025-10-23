from utils import rect_path_even

E = Entities.Tree

ODD_INST = "odd_instance"
PATH = "path"
def prepare(inst):
    path = inst[PATH]
    odd_inst = inst[ODD_INST]

    x0, y0 = get_pos_x(), get_pos_y()
    for d in path:
        x, y = get_pos_x(), get_pos_y()
        i, j = x - x0, y - y0
        if (i + j) % 2 == 0:
            if can_harvest():
                harvest()

            # Only two ground type, no need. (May have more in future updates?)
            # if get_ground_type() not in [Grounds.Turf, Grounds.Soil]:
            #     till()

            if not plant(E):
                quick_print("Error: unable to plant")
        else:
            prepare(odd_inst)

        move(d)

def tend(inst):
    path = inst[PATH]
    odd_inst = inst[ODD_INST]

    x0, y0 = get_pos_x(), get_pos_y()
    for d in path:
        x, y = get_pos_x(), get_pos_y()
        i, j = x - x0, y - y0
        if (i + j) % 2 == 0:
            if can_harvest():
                harvest()
            plant(E)
        else:
            tend(odd_inst)

        move(d)

# Width must be even (if odd, it is increased by 1)
# size must be smaller than or equal to world size
def create(size, odd_inst):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)

    path = rect_path_even(size)
    inst = {
        PATH: path,
        ODD_INST: odd_inst,
    }

    return inst

def test():
    import bush
    odd_inst = bush.create()
    inst = create(size=(10, 10), odd_inst=odd_inst)
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()