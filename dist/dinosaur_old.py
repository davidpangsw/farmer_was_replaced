

def prepare(inst):
    path = inst[PATH]
    change_hat(Hats.Dinosaur_Hat)

def tend(inst):
    path = inst[PATH]
    for d in path:
        success = move(d)
        if not success:
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)
            move(d)

def create(pos, size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, width)

    path = rect_path_even(size)

    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        SIZE: size,
        PATH: path,
    }

    return inst

def test():
    clear()
    
    L = get_world_size()
    D = max_drones()
    size = (8, 4)

    width, height = size
    for x in range(0, L - width, width):
        for y in range(0, L - height, height):
            inst = create((x, y), size)

            spawn_drone_main(inst) # last one would fail
    inst = create((L-width, L-height), size)
    drone_main(inst)
    

if __name__ == "__main__":
    test()