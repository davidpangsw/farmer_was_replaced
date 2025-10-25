from prototype import PREPARE, TEND, POS, WIDTH
from utils import matrix_of, move_to, sqrt_floor
from utils import DIRECTIONS, DIRECTION_TO_VECTOR, DIRECTION_REVERSE_MAP
from drone import spawn_drone_main, drone_main



clear()
L = get_world_size()

width = L

pos = inst[POS]
width = inst[WIDTH]
move_to((pos[0] + width // 2, pos[1] + width // 2))

plant(Entities.Bush)
substance = width * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)

search(inst)
harvest()
move_to(pos)