from registry import register
from utils import is_plantable

E = Entities.GRASS

def update():
	entity = get_entity_type()
	if entity == E:
		if can_harvest():
			harvest()
	elif is_plantable(entity) :
		if get_ground_type() == Grounds.Soil:
			till()
	else:
		if can_harvest():
			harvest()
			if get_ground_type() == Grounds.Soil:
				till()

def create(pos):
	register(pos, update)