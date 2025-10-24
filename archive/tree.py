import grass
import carrot_like
E = Entities.Tree
def create(pos):
	carrot_like.create(pos, E)


def create_rect(pos, size):
	for x in range(pos[0], pos[0]+size[0]):
		for y in range(pos[1], pos[1]+size[1]):
			if x % 2 == 0 and y % 2 == 0:
				create((x, y))
			else:
				grass.create((x, y))