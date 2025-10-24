Mazes

Items.Weird_Substance, which is obtained by fertilizing plants, has a strange effect on bushes. If the drone is over a bush and you call use_item(Items.Weird_Substance, amount) the bush will grow into a maze of hedges.
The size of the maze depends on the amount of Items.Weird_Substance used (the second argument of the use_item() call).
Without maze upgrades, using n Items.Weird_Substance will result in an nxn maze. For each maze upgrade level you need to use an extra n Items.Weird_Substance to get the same effect.
So to make a full field maze:

plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)


For some reason the drone can't fly over the hedges, even though they don't look that high.

There is a treasure hidden somewhere in the hedge. Use harvest() on the treasure to receive gold equal to the area of the maze. (For example, a 5x5 maze will yield 25 gold.)

If you use harvest() anywhere else the maze will simply disappear.

get_entity_type() is equal to Entities.Treasure if the drone is over the treasure and Entities.Hedge everywhere else in the maze.

Mazes do not contain any loops unless you reuse the maze (see below how to reuse a maze). So there is no way for the drone to end up in the same position again without going back.

You can check if there is a wall by trying to move through it. move() returns True if it succeeded and False otherwise.

If you have no idea how to get to the treasure, take a look at Hint 1. It shows you how to approach a problem like this.

For an extra challenge you can also reuse the maze by using the same amount of Items.Weird_Substance on the treasure again. This will increase the amount of gold in the treasure by one full maze and move it to a random position in the maze.

Using measure() on a treasure returns the position, that it will move to, as a tuple. next_x, next_y = measure()

Each time the treasure is moved, a random wall may be removed from the maze. So reused mazes can contain loops.

Note that loops in the maze make it much more difficult because it means that you can get to the same location again without moving back. Reusing a maze doesn't give you more gold than just harvesting and spawning a new maze. This is 100% an extra challenge that you can just skip. It's only worth it if the extra information and the shortcuts help you solve the maze faster.

The same maze can be solved a maximum of 300 times. This corresponds to 299 relocations. After that, using weird substance on the treasure won't increase the gold in it anymore and measure() will return None. 