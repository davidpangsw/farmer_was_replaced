Watering

Plants grow faster if they are watered. Soil and turf have a water level ranging from 0 to 1.
The function `get_water()` returns the water level of the ground it is over.

The growth speed of plant growing on tilled soil grows linearly from 1x speed at water level 0 to 5x speed at water level 1.

Soil dries out over time: The water looses 1% of it's current water every so often. So keeping a high water level uses a lot more water than keeping a low water level.

To water your plants you can use water tanks. You can trade empty tanks for wood using trade(Items.Empty_Tank)

A tank can hold 0.25 water.

Tanks fill up automatically. The fill rate is 0.5% of the number of empty tanks per second. So if you have 100 empty tanks one of them will fill every 2 seconds.

Call `use_item(Items.Water)` over any ground to empty a tank and water the ground.
Water evaporation and speedup

Water evaporation is triggered a number of seconds between 0.8 and 1.2 (distributed uniformly) after it was triggered last time. Each time it is triggered, the amount of water is decreased by 1% of the current amount.
For example: if the current water level is 0.5, when evaporation is triggered, the new water level will be 0.495

Water speed up factor is 1 + water_level * 4, that is a plant on a square with water level 0.25 will grow 2 times faster, with level 0.5 - 3 times fast, with level 0.75 - 4 times faster, and with level 1.0 - 5 times faster 