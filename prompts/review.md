The language is a subset of python, which means some syntax doesn't work. Here is the list


```py
# doesn't work, you cannot multiply an array with a number. use a normal for loop to append, or use the method written in utils
[East] * (width - 1)

# doesn't work, use normal if/else
min_width = apple_x + 2 if (apple_x + 2) % 2 == 0 else apple_x + 3

# Don't work. Don't use any bitwise operator
x = x & 1

# Doesn't work. Never import dev using mutliple line and brackets. import in a single line (I don't care how long)
from dev import (
    Entities, Grounds, Items, Debug,
    can_harvest, harvest, get_ground_type, till, plant, measure,
    get_pos_x, get_pos_y, move, get_entity_type, use_item, clear
)

```
fix the files in `src/`, not `dist/`