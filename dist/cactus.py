# Like other plants, cacti can be grown on soil and harvested as usual.
# However, they come in various sizes and have a strange sense of order.
# If you harvest a fully-grown cactus and all neighboring cacti are in sorted order, it will also harvest all neighboring cacti recursively.
# A cactus is considered to be in sorted order if all neighboring cacti to the North and East are fully grown and larger or equal in size and all neighboring cacti to the South and West are fully grown and smaller or equal in size.
# The harvest will only spread if all adjacent cacti are fully grown and in sorted order. This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.
# You will receive cactus equal to the number of harvested cacti squared. So if you harvest n cacti simultaneously you will receive n**2 Items.Cactus.
# The size of a cactus can be measured with measure(). It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.
# You can also pass a direction into measure(direction) to measure the neighboring tile in that direction of the drone.
# You can swap a cactus with its neighbor in any direction using the swap() command. swap(direction) swaps the object under the drone with the object one tile in the direction of the drone. 

from utils import square_path_even
from prototype import POSITION, ENTITY, PREPARE, TEND, SIZE

IS_GROWN = "is_grown"
IS_SORTED = "is_sorted"
def create_square(pos, width):
    if width % 2 == 1:
        quick_print("Error: width is not even, reduced by 1")
        width -= 1
    size = (width, width)

    # The path is supposed to traverse the whole square once
    # and then go back to the original position
    PATH = square_path_even(width)
    inst = {
        POSITION: pos,
        ENTITY: Entities.Cactus,
        SIZE: size,
    }

    def bubble():
        if not can_harvest():
            inst[IS_GROWN] = False

        if get_pos_x() < inst[POSITION][0] + inst[SIZE][0] - 1:
            dir = East
            if measure() > measure(dir):
                swap(dir)
                inst[IS_SORTED] = False

        if get_pos_y() < inst[POSITION][1] + inst[SIZE][1] - 1:
            dir = North
            if measure() > measure(dir):
                swap(dir)
                inst[IS_SORTED] = False

    def prepare():
        inst[IS_GROWN] = False
        inst[IS_SORTED] = False
        for d in PATH:
            if can_harvest():
                harvest()
            
            if get_ground_type() != Grounds.Soil:
                till()

            plant(inst[ENTITY])

            move(d)
    inst[PREPARE] = prepare

    def tend():
        # bubble sort
        while not (inst[IS_GROWN] and inst[IS_SORTED]):
            inst[IS_GROWN] = True
            inst[IS_SORTED] = True
            for d in PATH:
                bubble()
                move(d)

        harvest()

        # replant
        # no need to till, must be empty soil
        inst[IS_GROWN] = False
        inst[IS_SORTED] = False
        for d in PATH:
            plant(inst[ENTITY])
            move(d)
    inst[TEND] = tend

    return inst

def test():
    obj = create_square(pos=(0, 0), width=10)
    obj[PREPARE]()
    while True:
        obj[TEND]()

if __name__ == "__main__":
    test()