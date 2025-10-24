# The Farmer Was Replaced - Built-in Functions Reference

## Overview

This document provides a complete reference of all built-in functions available in "The Farmer Was Replaced" game. Each function includes its syntax, description, parameters, return values, and operation cost.

**Operation Cost**: Functions consume "operations" which affect execution time. Lower-cost functions (1 operation) are essentially free, while higher-cost functions (200 operations) take more time to execute.

---

## Movement & Interaction Functions

### move(direction)
Relocates the drone by one tile in the specified cardinal direction.

**Parameters:**
- `direction`: East, West, North, or South

**Returns:**
- `True` if the drone has moved
- `False` otherwise

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
move(North)
move(East)
```

---

### swap(direction)
Exchanges the drone's entity with an adjacent entity in the specified direction.

**Parameters:**
- `direction`: East, West, North, or South

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

---

## Harvesting & Planting Functions

### harvest()
Removes the entity underneath the drone.

**Parameters:**
- None

**Returns:**
- `True` if an entity was removed
- `False` otherwise

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
if can_harvest():
    harvest()
```

---

### can_harvest()
Checks if the plant under the drone is mature and ready to be harvested.

**Parameters:**
- None

**Returns:**
- `True` if there is an entity under the drone that is ready to be harvested
- `False` otherwise

**Operation Cost:**
- 1 operation

---

### plant(entity)
Places the specified entity below the drone.

**Parameters:**
- `entity`: The type of entity to plant (e.g., Entities.Bush, Entities.Carrot, etc.)

**Returns:**
- `True` if planting succeeded
- `False` otherwise

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
plant(Entities.Bush)
plant(Entities.Carrot)
```

---

## Ground Operations

### till()
Converts ground to soil or reverts soil back to grassland.

**Parameters:**
- None

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

**Example:**
```python
till()  # Convert to soil
plant(Entities.Carrot)
```

---

## Position & Map Information Functions

### get_pos_x()
Retrieves the current x-coordinate of the drone.

**Parameters:**
- None

**Returns:**
- Number representing the current x coordinate of the drone

**Operation Cost:**
- 1 operation

---

### get_pos_y()
Retrieves the current y-coordinate of the drone.

**Parameters:**
- None

**Returns:**
- Number representing the current y coordinate of the drone

**Operation Cost:**
- 1 operation

**Example:**
```python
x = get_pos_x()
y = get_pos_y()
quick_print("Position: " + (x, y))
```

---

### get_world_size()
Determines the current dimensions of the farm.

**Parameters:**
- None

**Returns:**
- The side length of the grid in the north to south direction (and east to west, as the grid is square)

**Operation Cost:**
- 1 operation

**Example:**
```python
size = get_world_size()
# Farm is size x size tiles
```

---

## Entity & Ground Detection Functions

### get_entity_type()
Identifies the type of entity below the drone.

**Parameters:**
- None

**Returns:**
- `None` if the tile is empty
- The type of the entity under the drone (e.g., Entities.Bush, Entities.Carrot)

**Operation Cost:**
- 1 operation

**Example:**
```python
entity = get_entity_type()
if entity == Entities.Bush:
    harvest()
```

---

### get_ground_type()
Identifies the type of ground beneath the drone.

**Parameters:**
- None

**Returns:**
- The type of the ground under the drone (e.g., Grounds.Soil, Grounds.Grassland)

**Operation Cost:**
- 1 operation

**Example:**
```python
ground = get_ground_type()
if ground == Grounds.Grassland:
    till()
```

---

### measure()
Can measure some values on some entities. The effect of this depends on the entity.

overloads:
measure() measures the entity under the drone.
measure(direction) measures the neighboring entity in the direction of the drone.

returns the number of petals of a sunflower.
returns the next position for a treasure.
returns the size of a cactus.
returns the number corresponding to the type of a dinosaur.
returns None for all other entities.

takes the time of 1 operation to execute.

example usage:
```python
num_petals = measure()
```

---

### get_companion()
Retrieves the companion preference of the plant under the drone.

**Parameters:**
- None

**Returns:**
- List of the form `[companion_type, companion_x_position, companion_y_position]`
- `None` if no plant under drone or plant has no companion preference

**Operation Cost:**
- 1 operation

**Example:**
```python
companion = get_companion()
if companion != None:
    comp_type = companion[0]
    comp_x = companion[1]
    comp_y = companion[2]
```

---

## Inventory & Resources Functions

### num_items(item)
Counts the quantity of a specific item in your inventory.

**Parameters:**
- `item`: The item type to count (e.g., Items.Carrot, Items.Wood)

**Returns:**
- The number of `item` currently in your inventory

**Operation Cost:**
- 1 operation

**Example:**
```python
carrots = num_items(Items.Carrot)
wood = num_items(Items.Wood)
```

---

### use_item(item, n=1)
Applies or uses an item from inventory n times.

**Parameters:**
- `item`: The item to use
- `n`: Number of times to use the item (default: 1)

**Returns:**
- `True` if an item was used
- `False` otherwise

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
# Use fertilizer on the current tile
use_item(Items.Fertilizer)

# Use water tank multiple times
use_item(Items.Water_Tank, 5)
```

---

### get_water()
Measures the soil moisture level under the drone.

**Parameters:**
- None

**Returns:**
- The water level under the drone as a number between `0` and `1`
- `0` = completely dry
- `1` = fully watered

**Operation Cost:**
- 1 operation

**Example:**
```python
water_level = get_water()
if water_level < 0.5:
    use_item(Items.Water_Tank)
```

---

### trade(item, n=1)
Attempts to purchase item(s) from the shop.

**Parameters:**
- `item`: The item to purchase
- `n`: Number of items to purchase (default: 1, requires Multi_Trade unlock for n > 1)

**Returns:**
- `True` if the purchase was successful
- `False` otherwise

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
# Buy one carrot seed
trade(Items.Carrot_Seed)

# Buy multiple (requires Multi_Trade unlock)
trade(Items.Pumpkin_Seed, 10)
```

---

## Unlocks & Research Functions

### unlock(unlock)
Activates a research node in the unlock tree.

**Parameters:**
- `unlock`: The unlock to activate (e.g., Unlocks.Carrots, Unlocks.Speed)

**Returns:**
- `True` if the unlock was successful
- `False` otherwise (insufficient resources or already unlocked)

**Operation Cost:**
- 200 operations if successful
- 1 operation if failed

**Example:**
```python
unlock(Unlocks.Carrots)
unlock(Unlocks.Speed)
```

---

### num_unlocked(thing)
Checks the unlock or upgrade status of a feature.

**Parameters:**
- `thing`: The unlock, entity, or feature to check

**Returns:**
- For upgradable items: `1` plus the number of times upgraded
- For non-upgradable unlocks: `1` if unlocked, `0` if locked
- For entities/features: `1` if available, `0` if not

**Operation Cost:**
- 1 operation

**Example:**
```python
if num_unlocked(Unlocks.Carrots) > 0:
    plant(Entities.Carrot)

# Check upgrade level
speed_level = num_unlocked(Unlocks.Speed)
```

---

### get_cost(thing)
Retrieves the resource requirements for purchasing or unlocking something.

**Parameters:**
- `thing`: The item, entity, or unlock to check

**Returns:**
- A dictionary with items as keys and numbers (quantities) as values
- Empty dictionary `{}` if no cost or already unlocked

**Operation Cost:**
- 1 operation

**Example:**
```python
cost = get_cost(Unlocks.Carrots)
# Returns: {Items.Hay: 100, Items.Wood: 50}

for item in cost:
    required = cost[item]
    current = num_items(item)
    quick_print(str(item) + ": " + current + "/" + required)
```

---

## Time & Performance Functions

### get_time()
Retrieves the current game time.

**Parameters:**
- None

**Returns:**
- The time in seconds since the start of the game

**Operation Cost:**
- 1 operation

**Example:**
```python
start_time = get_time()
# ... do work ...
end_time = get_time()
elapsed = end_time - start_time
```

---

### get_tick_count()
Counts the total number of operations performed.

**Parameters:**
- None

**Returns:**
- The number of operations performed since the start of execution

**Operation Cost:**
- 0 operations (free!)

**Example:**
```python
start_ops = get_tick_count()
# ... do work ...
end_ops = get_tick_count()
operations_used = end_ops - start_ops
```

---

## Output & Display Functions

### print(something)
Displays a value as smoke above the drone with animation.

**Parameters:**
- `something`: The value to display (string, number, etc.)

**Returns:**
- `None`

**Operation Cost:**
- 1 second (real-time, unaffected by speed upgrades)

**Note:**
- Use sparingly as it takes real-time to execute
- Good for debugging but slows down execution

**Example:**
```python
print("Hello World")
print(get_pos_x())
```

---

### quick_print(something)
Logs a value to the output page without animation.

**Parameters:**
- `something`: The value to log

**Returns:**
- `None`

**Operation Cost:**
- 1 operation

**Note:**
- Much faster than print()
- Preferred for debugging and monitoring

**Example:**
```python
quick_print("Starting harvest loop")
quick_print("Position: "+(get_pos_x(), get_pos_y()))
```

---

### do_a_flip()
Makes the drone perform a flip animation.

**Parameters:**
- None

**Returns:**
- `None`

**Operation Cost:**
- 1 second (real-time, unaffected by speed upgrades)

**Example:**
```python
do_a_flip()  # Celebrate!
```

---

## Standard Python Functions

These work as in Python. Operation costs noted where relevant.

### Collection Functions
- `range(end)`, `range(start, end)`, `range(start, end, step)` - 1 operation
- `len(collection)` - 1 operation
- `list(collection)` - `1 + len(collection)` operations
- `set(collection)` - `1 + len(collection)` operations
- `dict()` - 1 operation

### Math Functions
- `min(a, b)` or `min(sequence)` - Variable cost
- `max(a, b)` or `max(sequence)` - Variable cost
- `abs(number)` - Variable cost
- `random()` - Returns 0-1, costs 1 operation

### List Methods
- `list.append(element)` - Add to end
- `list.insert(index, element)` - Insert at position
- `list.pop(index=-1)` - Remove and return element
- `list.remove(element)` - Remove first occurrence

---

## Game Control Functions

### clear()
Resets the entire farm and returns the drone to the starting position.

**Parameters:**
- None

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

**Note:**
- Removes all entities from the farm
- Resets ground types
- Resets drone position to origin

**Example:**
```python
clear()  # Start fresh
```

---

### timed_reset()
Initiates a timed leaderboard run.

**Parameters:**
- None

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

**Note:**
- Used for competitive leaderboard attempts
- Tracks completion time for ranking

---

### set_execution_speed(speed)
Controls the speed at which the program executes.

**Parameters:**
- `speed`: The execution speed multiplier (higher = faster)

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

**Example:**
```python
set_execution_speed(10)  # 10x speed
```

---

### set_farm_size(size)
Adjusts the size of the farm grid.

**Parameters:**
- `size`: The desired side length of the square farm grid

**Returns:**
- `None`

**Operation Cost:**
- 200 operations

**Note:**
- Must be unlocked through research
- Larger farms allow more complex operations but take more time to traverse

**Example:**
```python
set_farm_size(5)  # 5x5 farm
```

---

## Control Flow

Standard Python control flow: `if`/`elif`/`else`, `while`, `for`, `break`, `continue`, `def`

**Example:**
```python
def harvest_field():
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        move(North)
```

---

## Enumeration Objects

### Grounds

Available ground types:

- `Grounds.Turf`
- `Grounds.Soil`

**Usage:**
```python
if get_ground_type() == Grounds.Turf:
    till()
```

---

### Unlocks

Available research unlocks in the technology tree:

**Basic Unlocks:**
- `Unlocks.Variables`
- `Unlocks.Operators`
- `Unlocks.Loops`
- `Unlocks.Lists`
- `Unlocks.Senses`
- `Unlocks.Cost_Lists`
- `Unlocks.Debug`

**Farming Unlocks:**
- `Unlocks.Grass`
- `Unlocks.Plant`
- `Unlocks.Carrots`
- `Unlocks.Trees`
- `Unlocks.Pumpkins`
- `Unlocks.Sunflowers`

**Advanced Unlocks:**
- `Unlocks.Watering`
- `Unlocks.Fertilizer`
- `Unlocks.Polyculture` (companion planting)
- `Unlocks.Mazes`

**Utility Unlocks:**
- `Unlocks.Speed` (upgradable)
- `Unlocks.Expand` (farm size)
- `Unlocks.Multi_Trade` (bulk purchases)
- `Unlocks.Auto_Unlock` (automatic research)
- `Unlocks.Reset`
- `Unlocks.Timed_Reset` (leaderboards)

**Usage:**
```python
if num_unlocked(Unlocks.Carrots) == 0:
    cost = get_cost(Unlocks.Carrots)
    # Check if we can afford it
    can_afford = True
    for item in cost:
        if num_items(item) < cost[item]:
            can_afford = False
    if can_afford:
        unlock(Unlocks.Carrots)
```

---

## Operators & Constants

Standard Python operators: `+`, `-`, `*`, `/`, `%`, `**`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `not`, `=`, `+=`, `-=`, `*=`, `/=`

Constants: `True`, `False`, `None`

There are no bitwise operators. There is no "is" operator.

---

## Language Limitations

Based on the game's constraints:

1. **No multi-line strings**: Must use single-line strings only
2. **No f-strings or format()**: Use `+` to concatenate strings
3. **No import statements**: All built-in functions are available by default
4. **Python-like but not Python**: This is a custom language inspired by Python

---

## Tips for Efficient Code

1. **Check before expensive operations**: Use 1-operation checks before 200-operation actions
   ```python
   if can_harvest():  # 1 operation
       harvest()       # 200 operations
   ```

2. **Use quick_print for debugging**: Avoid `print()` in production code
   ```python
   quick_print("Debug info")  # 1 operation
   # Instead of:
   # print("Debug info")  # 1 second real-time
   ```

3. **Cache repeated calculations**: Store results instead of recalculating
   ```python
   world_size = get_world_size()  # Cache this
   for i in range(world_size):
       # Use world_size instead of calling get_world_size() each time
       pass
   ```

4. **Monitor operation count**: Use `get_tick_count()` to optimize
   ```python
   start = get_tick_count()
   # ... your code ...
   end = get_tick_count()
   quick_print("Operations used: " + (end - start))
   ```

---

## Common Patterns

### Grid Traversal
```python
# Scan entire farm
world_size = get_world_size()
for y in range(world_size):
    for x in range(world_size):
        # Process tile
        if can_harvest():
            harvest()
        if x < world_size - 1:
            move(East)
    if y < world_size - 1:
        move(South)
        # Move to start of next row
        for x in range(world_size - 1):
            move(West)
```

### Resource Management
```python
# Ensure minimum stock
def ensure_stock(item, minimum):
    current = num_items(item)
    if current < minimum:
        needed = minimum - current
        trade(item, needed)
```

### Conditional Planting
```python
# Plant based on ground type
ground = get_ground_type()
if ground == Grounds.Turf:
    plant(Entities.Grass)
elif ground == Grounds.Soil:
    plant(Entities.Carrot)
```

---

*This reference document is based on official wiki documentation and community research. All function behaviors are subject to game updates.*


## Other
can_move(dir)
return True if can move in a maze