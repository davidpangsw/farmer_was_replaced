from utils import matrix, none, false

DIRS = {
	East: (1, 0),
	North: (0, 1),
	West: (-1, 0),
	South: (0, -1),
}

DIRS_REVERSE = {
	East: West,
	North: South,
	West: East,
	South: North,
}

def dfs(x0, y0, w, h, visited):
	x, y = get_pos_x(), get_pos_y()
	i, j = x-x0, y-y0
	visited[i][j] = True
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	for dir in DIRS:
		if not can_move(dir):
			continue
		dx, dy = DIRS[dir]
		if i + dx >= w or i + dx < 0:
			continue
		if j + dy >= h or j + dy < 0:
			continue
		if visited[i+dx][j+dy]:
			continue
		move(dir)
		success = dfs(x0, y0, w, h, visited)
		if success:
			return True
		move(DIRS_REVERSE[dir])
	return False

def test():
	L = get_world_size()
	M, N = L, L
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	
	while True:
		clear()
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, substance)
	
	
		visited = matrix(M, N, false)
		dfs(0, 0, M, N, visited)

if __name__ == "__main__":
	test()


