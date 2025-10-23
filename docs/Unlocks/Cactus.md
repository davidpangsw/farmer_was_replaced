Like other plants, cacti can be grown on soil and harvested as usual.

However, they come in various sizes and have a strange sense of order.

If you harvest a fully-grown cactus and all neighboring cacti are in sorted order, it will also harvest all neighboring cacti recursively.

A cactus is considered to be in sorted order if all neighboring cacti to the North and East are fully grown and larger or equal in size and all neighboring cacti to the South and West are fully grown and smaller or equal in size.

The harvest will only spread if all adjacent cacti are fully grown and in sorted order. This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.

You will receive cactus equal to the number of harvested cacti squared. So if you harvest n cacti simultaneously you will receive n**2 Items.Cactus.

The size of a cactus can be measured with measure(). It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.

You can also pass a direction into measure(direction) to measure the neighboring tile in that direction of the drone.

You can swap a cactus with its neighbor in any direction using the swap() command. swap(direction) swaps the object under the drone with the object one tile in the direction of the drone. 