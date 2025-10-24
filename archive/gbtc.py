# GRASS, BUSH, TREE, CARROT

from utils import matrix, empty_array, none
from registry import register
import grass
import bush
import tree
import carrot
import carrot_like

min_hay = 20000
min_wood = 20000
POLY = "polyculture"
G, B, T, C = Entities.GRASS, Entities.BUSH, Entities.TREE, Entities.CARROT

def create(pos, size):
	x0, y0 = pos
	w, h = size
	obj = {
		POLY: matrix(w, h, none)
	}

	def set_companion():
		comp = get_companion()
		if comp == None:
			return
		# print(comp)
		cx, cy = comp[1]

		i, j = cx-x0, cy-y0
		if i >= 0 and i < w and j >= 0 and j < h:
			obj[POLY][i][j] = comp[0]
	
	def update_evens():
		carrot_like.update(Entities.Tree)
		set_companion()

	def update_odds():
		x, y = get_pos_x(), get_pos_y()
		i, j = x - x0, y - y0
		if num_items(Items.HAY) < min_hay:
			grass.update()
			return
		if num_items(Items.WOOD) < min_wood:
			carrot_like.update(Entities.Bush)
			return

		# polyculture
		if obj[POLY][i][j] == G:
			grass.update()
		if obj[POLY][i][j] == B:
			carrot_like.update(Entities.Bush)
		elif obj[POLY][i][j] == C:
			carrot_like.update(Entities.Carrot)
		else:
			carrot_like.update(Entities.Carrot)
		obj[POLY][i][j] = None
		set_companion()
	

	for x in range(x0, x0+w):
		for y in range(y0, y0+h):
			if x % 2 == 0 and y % 2 == 0:
				register((x, y), update_evens)
			else:
				register((x, y), update_odds)

				

def test():
	from registry import execute
	clear()
	w, h = 6, 6
	create((0, 0), (w, h))

	while True:
		for x in range(w):
			for y in range(h):
				execute((x, y))
				move(North)
			for y in range(h):
				move(South)
			move(East)
		for x in range(w):
			move(West)

if __name__ == "__main__":
	test()