import cactus
import gbtc
import sunflower
import pumpkin


clear()

L = get_world_size()

def drone_main(inst):
    pos = inst[POS]
    prepare = inst[PREPARE]
    tend = inst[TEND]

    move_to(pos)
    prepare(inst)
    while True:
        tend(inst)

def spawn_drone_main(inst):
    def f():
        drone_main(inst)
    spawn_drone(f)

spawn_drone_main(cactus.create_square((0, 0), 10))
spawn_drone_main(gbtc.create((0, 10), (10, L-10)))
spawn_drone_main(sunflower.create((10, 0), (L-10, L-6)))
drone_main(pumpkin.create((L-6, L-6), 6))