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


spawn_drone_main(pumpkin.create((10, 0), 6))
spawn_drone_main(pumpkin.create((10, 6), 6))
spawn_drone_main(pumpkin.create((10, 12), 6))
spawn_drone_main(gbtc.create((10, 18), (6, L-6)))
drone_main(gbtc.create((16, 0), (L-16, L)))