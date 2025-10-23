Polyculture

Grass, bushes, trees, and carrots yield ten times more when they have the right plant companion. The companion preference is different for every individual plant and cannot be predicted. Fortunately the companion preference of the plant under the drone can be measured using get_companion(). It returns a list whose first element is the plant type it would like as a companion and the second and third elements are the x and y coordinates of the position where it would like it's companion.

For example if you plant a bush and then call get_companion() it will return something like [Entities.Carrot, 3, 5]. This means that this bush would like to have carrots at position (3,5). So if you plant carrots at (3,5) and then harvest the bush it will yield ten times more wood. The growth stage of the carrot doesn't matter.

The companion preference of a plant can be either Entities.Grass, Entities.Bush, Entities.Tree or Entities.Carrot. Every plant chooses this randomly but it will always choose a plant different from itself. The position can also be any position within 3 moves of the plant except the position of the plant itself.

If there is no plant under the drone that has a companion preference get_companion() will return None. 