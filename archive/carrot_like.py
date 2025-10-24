from registry import register
from utils import is_plantable

def update(E):
	if can_harvest():
		harvest()
	entity = get_entity_type()
	if is_plantable(entity):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(E)
		
def create(pos, E, need_till=True):
	if need_till:
		def update():
			if can_harvest():
				harvest()
			entity = get_entity_type()
			if is_plantable(entity):
				if get_ground_type() != Grounds.Soil:
					till()
				plant(E)
		
		register(pos, update)
	else:
		def update():
			if can_harvest():
				harvest()
			entity = get_entity_type()
			if is_plantable(entity):
				plant(E)
		register(pos, update)

def create_rect(pos, size, E):
	for x in range(pos[0], pos[0]+size[0]):
		for y in range(pos[1], pos[1]+size[1]):
			create((x, y), E)