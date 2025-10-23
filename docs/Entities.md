# Entities

## Contents

1. Grass
2. Bush
3. Tree
4. Carrots
5. Pumpkin
6. Sunflower
7. Cactus
8. Hedge
9. Treasure
10. Dinosaur

## Grass

Grows automatically. Harvest it to obtain Items.Hay.

Average seconds to grow: 0.5
Grows on: turf

## Bush

A small bush that drops Items.Wood.

Average seconds to grow: 4
Grows on: turf or soil

## Tree

Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

Average seconds to grow: 7
Grows on: turf or soil

## Carrots

Carrots!

Average seconds to grow: 6
Grows on: soil
Plant Cost 1 	Items.Carrot_Seed

## Pumpkin

Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.
When you harvest a pumpkin you get Items.Pumpkin equal to the side length of the mega pumpkin cubed. (A 2x2 pumpkin yields 8 Items.Pumpkin)

Average seconds to grow: 2
Grows on: soil
Plant Cost 1 	Items.Pumpkin_Seed

## Sunflower

Sunflowers collect the power from the sun. Harvesting them will give you Items.Power equal to the square root of the number of sunflowers in the farm.
If you harvest a sunflower that doesn't have the maximum number of petals all the sunflowers will die.

Average seconds to grow: 5
Grows on: soil
Plant Cost 1 	Items.Sunflower_Seed

## Cactus

Cacti come in 10 different sizes. When harvested, all cacti on the field will be harvested. Only those that are in sorted order will drop Items.Cactus.

Average seconds to grow: 1
Grows on: soil
Plant Cost 1 	Items.Cactus_Seed

## Hedge

Part of the maze. Grow a maze by fertilizing a fully grown bush.

## Treasure

A treasure that contains gold equal to the area of the maze in which it is hidden (25 gold on a 5x5 maze). It can be harvested like a plant.

## Dinosaur

A majestic dinosaur. It moves around randomly but won't move for a while after being measured. Harvesting it harvests all adjacent dinosaurs of the same type and makes them drop Items.Bone.

Average seconds to grow: 0.2
Grows on: turf or soil


## Dead_Pumpkin
Not on the wiki but does exists, if you call `get_entity_type()`
A pumpkin that dies simply disappears so you can plant a new one there. 