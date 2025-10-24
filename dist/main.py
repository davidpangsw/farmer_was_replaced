import cactus
import gbtc
import sunflower
import pumpkin


clear()

L = get_world_size()

cactus_farm = cactus.create_square((0, 0), 10)
gbtc_farm = gbtc.create((0, 10), (10, L-10))
sunflower_farm = sunflower.create((10, 0), (L-10, L-6))
pumpkin_farm = pumpkin.create((L-6, L-6), 6)