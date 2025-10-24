import grass
import bush
import carrot
import pumpkin
import tree
import gbtc
import sunflower
import cactus
from registry import execute

clear()

L = get_world_size()

# L x L
# tree.create_rect((0, 0), size)
cactus.create((0, 0), (10, 10))
pumpkin.create((L-6, L-6), 6)
gbtc.create((0, 10), (10, L-10))
sunflower.create_rect((L-6, 0), (6, L - 6))

while True:
	for x in range(L):
		for y in range(L):
			execute((x, y))
			move(North)
		move(East)
	