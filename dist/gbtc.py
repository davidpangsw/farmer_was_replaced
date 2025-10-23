# Plant trees in a checkboard, with Grass, Bush, and Carrots in between
# Make use of polyculture

import grass
import bush
import tree
import carrot
import gbc
from utils import wait_for_harvest, matrix_of, rect_path_even, matrix

G = Entities.Grass
B = Entities.Bush
T = Entities.Tree
C = Entities.Carrots

SIZE = "size"
POLY = "polyculture"
PATH = "path"
GBTCS = "matrix of grass, bush, tree, carrot"

def set_polyculture(inst):
    w, h = inst[SIZE]
    entity, pos = get_companion()
    ci, cj = get_pos_x() - pos[0], get_pos_y() - pos[1]
    if (0 <= ci and ci < w) and (0 <= cj and cj < h):
        inst[POLY][ci][cj] = entity


# Width must be even (if odd, it is increased by 1)
# size must be smaller than or equal to world size
def create(size):
    width, height = size
    if width % 2 == 1:
        quick_print("Warning: width is not even, increased by 1")
        width += 1
    size = (width, height)

    def create_poly_inst(i, j):
        if (i + j) % 2 == 0:
            return tree.create()
        else:
            return gbc.create()

    inst = {
    }
    inst[SIZE] = size
    inst[POLY] = matrix_of(size, None)
    inst[PATH] = rect_path_even(size)
    inst[GBTCS] = matrix(size, create_poly_inst)
    return inst

def prepare(inst):
    path = inst[PATH]
    gbtcs = inst[GBTCS]
    x0, y0 = get_pos_x(), get_pos_y()
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
    x0, y0 = get_pos_x(), get_pos_y()
    for d in path:
        x, y = get_pos_x(), get_pos_y()
        i, j = x - x0, y - y0
        if (i + j) % 2 == 0:
            tree.tend(gbtcs[i][j])
        else:
            gbc.tend(gbtcs[i][j], inst[POLY])
        set_polyculture(inst)
        
        move(d)


def test():
    inst = create(size=(10, 8))
    prepare(inst)
    while True:
        tend(inst)

if __name__ == "__main__":
    test()