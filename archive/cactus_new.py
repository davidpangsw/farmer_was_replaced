from utils import reverse_direction, reverse_path, snake_path, square_path
from prototype import POSITION, ENTITY, PREPARE, TEND, SIZE

IS_SORTED = "is_sorted"
def create(pos, width):
	inst = {
		POSITION: pos,
		ENTITY: Entities.CACTUS,
		SIZE: (width, width),
	}
	
	FORWARD_PATH = snake_path((width, width), (East, North)) + [None]
	BACKWARD_PATH = snake_path((width, width), (West, South)) + [None]
	
	def swap_dir(dir):
		is_swapped = False
		m = measure()
		md = measure(dir)
		if dir in [West, South]:
			if m < md:
				swap(dir)
				is_swapped = True
				m = md
		else: # dir in [East, North]
			if m > md:
				swap(dir)
				is_swapped = True
				m = md
		return is_swapped, m

	def prepare():
		inst[IS_SORTED] = True
		for i in range(len(FORWARD_PATH)):
			d = FORWARD_PATH[i]
			
			# clear and plant
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(inst[ENTITY])
			
			# tend
			if i < width:
				m = measure()
			else:
				is_swapped, m = swap_dir(South)
				if is_swapped:
					inst[IS_SORTED] = False
			if d != None:
				move(d)
		
		prev_d = None
		for d in BACKWARD_PATH:
			# tend
			if i < width:
				m = measure()
			else:
				is_swapped, m = swap_dir(South)
				if is_swapped:
					inst[IS_SORTED] = False
			prev_measure, prev_d = m, d
			if d != None:
				move(d)
	inst[PREPARE] = prepare

	def tend():
		# we can assume the whole farm is planted with cactus

		prev_d, prev_measure = None, -1
		while True:
			inst[IS_SORTED] = True
			for d in FORWARD_PATH:
				m = tend_cell(prev_d, prev_measure)
				prev_measure, prev_d = m, d
				if d != None:
					move(d)
			
			for d in BACKWARD_PATH:
				m = tend_cell(prev_d, prev_measure)
				prev_measure, prev_d = m, d
				if d != None:
					move(d)
			
			if inst[IS_SORTED]:
				break
		
		harvest()
	inst[TEND] = tend

	return inst

def test():
	clear()
	obj = create((0, 0), (10, 10))
	obj[PREPARE]()
	while True:
		obj[TEND]()

if __name__ == "__main__":
	test()