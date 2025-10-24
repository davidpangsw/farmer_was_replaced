import cactus
import gbtc
import sunflower
import pumpkin
from prototype import POS, PREPARE, TEND
from utils import move_to
from drone import spawn_drone_main, drone_main


clear()

L = get_world_size()


x = 0
width = 10
spawn_drone_main(cactus.create_square((x, 0), width))
spawn_drone_main(gbtc.create((x, 10), (width, L-10)))
x += width

width = 6
spawn_drone_main(pumpkin.create((x, 0), width))
spawn_drone_main(sunflower.create((x, 6), (width, 6)))
spawn_drone_main(pumpkin.create((x, 12), width))
spawn_drone_main(gbtc.create((x, 18), (width, L-18)))
x += width

width = L-16
# split the remaining drones
D = max_drones()
d = num_drones()
a = D - d + 1 # available drones
height = L // a
for i in range(a-1):
    spawn_drone_main(gbtc.create((x, i * height), (width, height)))
drone_main(gbtc.create((x, (a-1) * height), (width, height)))