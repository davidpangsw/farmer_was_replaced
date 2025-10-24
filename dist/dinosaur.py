from utils import rect_path_even, move_to

clear()
set_world_size(6)
L = get_world_size()
size = L, L
path = rect_path_even(size)
change_hat(Hats.Dinosaur_Hat)
while True:
    for d in path:
        success = move(d)
        if not success:
            change_hat(Hats.Gold_Hat)
            change_hat(Hats.Dinosaur_Hat)
            move(d)