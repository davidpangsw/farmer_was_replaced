def empty_array():
	return []

def false():
	return False

def none():
	return None

def array_of(n, value):
	arr = []
	for i in range(n):
		arr.append(value)
	return arr

def matrix(m, n, creator):
	arr = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(creator())
		arr.append(row)
	return arr

def is_plantable(entity):
	return entity in [None, Entities.Grass, Entities.Dead_Pumpkin]

	
DIRECTION_REVERSE_MAP = {
	East: West,
	North: South,
	West: East,
	South: North,
}

DIRECTION_90_MAP = {
	East: North,
	North: West,
	West: South,
	South: East,
}

def reverse_direction(d):
	return DIRECTION_REVERSE_MAP[d]

def reverse_path(path):
	result = []
	for d in path[::-1]:
		result.append(reverse_direction(d))
	return result

def snake_path(size):
	if size > 2:
		path = []
		path += array_of(size - 1, East)
		path += array_of(size - 1, North)
		path += [West]
		path += array_of(size - 2, South)
		path += array_of(size - 2, West)
		path += [North]
		path += snake_path(size - 2)
		return path
	elif size == 2:
		return [East, North, West]
	else: # size == 1
		return [None]
		
