
from prototype import PREPARE, TEND, POS, SIZE, PATH
from utils import rect_path_even, reverse_path, wait_for_seed
from drone import spawn_drone_main, drone_main
import sunflower
import gbtc

clear()
set_world_size(32)
L = get_world_size()
size = L, L
path = rect_path_even(size)
change_hat(Hats.Dinosaur_Hat)
while True:
    for d in path:
        success = move(d)
        if not success:
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)
            move(d)
