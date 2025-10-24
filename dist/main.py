import cactus
import gbtc
import sunflower
import pumpkin
from prototype import POS, PREPARE, TEND
from utils import move_to
from drone import spawn_drone_main, drone_main


clear()

L = get_world_size()


spawn_drone_main(sunflower.create((0, 0), (10, 2)))
spawn_drone_main(cactus.create_square((0, 2), 10))
spawn_drone_main(gbtc.create((0, 12), (10, L-12)))


spawn_drone_main(pumpkin.create((11, 0), 6))
spawn_drone_main(gbtc.create((11, 6), (6, L-6)))
drone_main(gbtc.create((17, 0), (L-16, L)))