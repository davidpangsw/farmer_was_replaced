import carrot_like
E = Entities.Carrot
def create(pos):
	carrot_like.create(pos, E)


def create_rect(pos, size):
	carrot_like.create_rect(pos, size, E)