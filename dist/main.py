
clear()

L = get_world_size()

cactus_farm = cactus.create((0, 0), (10, 10))
gbtc_farm = gbtc.create((0, 10), (10, L-10))
sunflower_farm = sunflower.create((L-6, 0), (6, L-6))
pumpkin_farm = pumpkin.create(pos=(L-6, L-6), size=(6, 6))