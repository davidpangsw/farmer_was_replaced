from utils import rect_path_even
from prototype import PREPARE, TEND, SIZE

E = Entities.Tree
# Width must be even (if odd, it is increased by 1)
# size must be smaller than or equal to world size
def create(size, odd_inst):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)

    PATH = rect_path_even(size)
    inst = {
        SIZE: size,
    }

    def prepare():
        x0, y0 = get_pos_x(), get_pos_y()
        for d in PATH:
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
                odd_inst[PREPARE]()

            move(d)
    inst[PREPARE] = prepare

    def tend():
        x0, y0 = get_pos_x(), get_pos_y()
        for d in PATH:
            x, y = get_pos_x(), get_pos_y()
            i, j = x - x0, y - y0
            if (i + j) % 2 == 0:
                if can_harvest():
                    harvest()
                plant(E)
            else:
                odd_inst[TEND]()

            move(d)
    inst[TEND] = tend

    return inst

def test():
    import bush
    odd_inst = bush.create()
    obj = create(size=(10, 10), odd_inst=odd_inst)
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()