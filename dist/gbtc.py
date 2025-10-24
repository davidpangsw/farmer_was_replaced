# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

from prototype import PREPARE, TEND, POS, SIZE
import grass
import bush
import tree
import carrot
import gbc
from utils import wait_for_harvest, matrix_of, rect_path_even, matrix

G = Entities.Grass
B = Entities.Bush
T = Entities.Tree
C = Entities.Carrot
POLY = "polyculture"
PATH = "path"
GBTCS = "matrix of grass, bush, tree, carrot"

def decide_to_plant(inst, poly):
    # decide which one to plant
    # if low on Hay, plant Grass
    if num_items(Items.Hay) < num_items(Items.Carrot):
        return G
    # if low on Wood, plant bush
    elif num_items(Items.Wood) < num_items(Items.Carrot):
        return B
    # if low on Carrot, plant Carrot
    elif num_items(Items.Carrot) < num_items(Items.Pumpkin):
        return C
    # if polyculture has suggestion, plant base on it
    elif poly != None:
        return poly
    # else, randomly choose from [G, B, C]
    else:
        return GBC[int(random() * 3)]

def set_polyculture(inst):
    x0, y0 = inst[POS]
    w, h = inst[SIZE]
    comp = get_companion()
    if comp == None:
        return
    entity, pos = comp
    ci, cj = pos[0] - x0, pos[1] - y0
    if (0 <= ci and ci < w) and (0 <= cj and cj < h):
        inst[POLY][ci][cj] = entity


# Width must be even (if odd, it is increased by 1)
# size must be smaller than or equal to world size
def create(pos, size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)
    x0, y0 = pos

    def create_poly_inst(i, j):
        cell_pos = (x0 + i, y0 + j)
        if (i + j) % 2 == 0:
            return tree.create(cell_pos)
        else:
            return gbc.create(cell_pos)

    inst = {
        PREPARE: prepare,
        TEND: tend,

        POS: pos,
        SIZE: size,
        POLY: matrix_of(size, None),
        PATH: rect_path_even(size),
        GBTCS: matrix(size, create_poly_inst),
    }
    return inst

def prepare(inst):
    path = inst[PATH]
    gbtcs = inst[GBTCS]
    x0, y0 = inst[POS]
    for d in path:
        x, y = get_pos_x(), get_pos_y()
        i, j = x - x0, y - y0
        if (i + j) % 2 == 0:
            tree.prepare(gbtcs[i][j])
        else:
            gbc.prepare(gbtcs[i][j])

        # safe because prepare() will also plant in G, B, T, C
        set_polyculture(inst)

        move(d)


def tend(inst):
    path = inst[PATH]
    gbtcs = inst[GBTCS]
    x0, y0 = inst[POS]
    for d in path:
        x, y = get_pos_x(), get_pos_y()
        i, j = x - x0, y - y0
        if (i + j) % 2 == 0:
            tree.tend(gbtcs[i][j])
        else:
            to_plant = decide_to_plant(inst, poly)
            gbc.tend(gbtcs[i][j], to_plant)
        set_polyculture(inst)
        
        move(d)


def test():
    clear()
    inst = create((get_pos_x(), get_pos_y()), (10, 8))
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()