from registry import register, execute
from utils import is_plantable

E = Entities.PUMPKIN
COUNT = 'count'

WATER_MIN = 2000
WATER_LEVEL_MIN = 0.5
FERT_MIN = 500
def update(obj):
	entity = get_entity_type()
	
	if entity != E and can_harvest():
		harvest()
	
	if is_plantable(entity):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(E)
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(E)
		# watering
		if get_water() < WATER_LEVEL_MIN and num_items(Items.Water) > WATER_MIN:
			use_item(Items.Water)
		# fertilizing
		elif num_items(Items.Fertilizer) > FERT_MIN:
			use_item(Items.Fertilizer)
		else:
			do_a_flip()
		
	obj[COUNT] += 1

def create(pos, size):
	x, y = pos
	obj = {
		COUNT: 0,
	}

	def start():
		obj[COUNT] = 0
	
	def u():
		update(obj)
	
	def end():
		if obj[COUNT] == size * size:
			harvest()

	register(pos, start)
	for i in range(size):
		for j in range(size):
			register((x+i, y+j), u)
	register((x+size-1, y+size-1), end)


def test():
	clear()
	create((0, 0), 6)

	while True:
		for x in range(6):
			for y in range(6):
				execute((x, y))
				move(North)
			for y in range(6):
				move(South)
			move(East)
		for x in range(6):
			move(West)

if __name__ == "__main__":
	test()