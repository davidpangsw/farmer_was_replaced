import cactus


clear()

L = get_world_size()

cactus_farm = cactus.create_square(width=10)
gbtc_farm = gbtc.create(size=(10, L-10))
sunflower_farm = sunflower.create((L-6, 0), (6, L-6))
pumpkin_farm = pumpkin.create(width=6)