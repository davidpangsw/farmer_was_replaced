from utils import matrix, empty_array

world_size = get_world_size()
FUNCTIONS = "functions"

r = {
	FUNCTIONS: matrix(world_size, world_size, empty_array),
}

def register(pos, f):
	global r
	x, y = pos
	r[FUNCTIONS][x][y].append(f)

def unregister(pos, f):
	global r
	x, y = pos
	r[FUNCTIONS][x][y].remove(f)

def execute(pos):
	x, y = pos
	for f in r[FUNCTIONS][x][y]:
		f()