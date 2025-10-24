from registry import register
from utils import is_plantable

E = Entities.CACTUS
START_POS = "start_pos"
SIZE = "size"
IS_READY = "is_ready"
IS_SORTED = "is_sorted"

def update(obj):
	entity = get_entity_type()
	if entity == E:
		if can_harvest():
			x0, y0 = obj[START_POS]
			w, h = obj[SIZE]
			x, y = get_pos_x(), get_pos_y()
			if x == x0+w-1 and y==y0+h-1:
				pass
			elif y == y0+h-1:
				# can't bubble up
				# bubble right
				if measure() > measure(East):
					swap(East)
					obj[IS_SORTED] = False
			elif x == x0+w-1:
				# can't bubble right
				# bubble up
				if measure() > measure(North):
					swap(North)
					obj[IS_SORTED] = False
			else:
				# bubble right and bubble up
				if measure() > measure(East):
					swap(East)
					obj[IS_SORTED] = False
				if measure() > measure(North):
					swap(North)
					obj[IS_SORTED] = False
		else:
			obj[IS_READY] = False
	elif is_plantable(entity):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(E)
		obj[IS_READY] = False
	else:
		if can_harvest():
			harvest()
		obj[IS_READY] = False
	
def create(pos, size):
	x0, y0 = pos
	w, h = size
	obj = {
		START_POS: pos,
		SIZE: size,
		IS_READY: True,
		IS_SORTED: True
	}

	def start():
		obj[IS_READY] = True
		obj[IS_SORTED] = True
	
	def u():
		update(obj)
	
	def end():
		if obj[IS_READY] and obj[IS_SORTED]:
			harvest()
	
	register(pos, start)
	for x in range(x0, x0+w):
		for y in range(y0, y0+h):
			register((x, y), u)
	register((x0+w-1, y0+h-1), end)
	