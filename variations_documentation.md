# Fractal Tree Variations

## Basic Variations

### 1. Symmetric Binary Tree
The standard implementation with equal left and right branches.

### 2. Asymmetric Trees
Different angles or sizes for left and right branches:
```python
# Right branch: 25°, Left branch: 35°
turtle.right(25)
draw_branch(size * 0.8, level - 1)
turtle.left(60)  # 25 + 35 = 60
draw_branch(size * 0.7, level - 1)
```

### 3. Ternary Trees
Three branches at each node:
```python
# Center branch
draw_branch(size * 0.8, level - 1)

# Right branch
turtle.right(30)
draw_branch(size * 0.7, level - 1)

# Left branch
turtle.left(60)
draw_branch(size * 0.7, level - 1)
```

## Color Variations

### 1. Autumn Theme
```python
# Brown to red gradient
red = 139 + (116 * level) // max_level
green = 69 + (20 * level) // max_level
blue = 19
pencolor(red, green, blue)
```

### 2. Winter Theme
```python
# Blue to white gradient
blue_val = 255 - (100 * level) // max_level
pencolor(blue_val, blue_val, 255)
```

### 3. Rainbow Theme
```python
# Cycle through rainbow colors
colors = [(255,0,0), (255,127,0), (255,255,0), (0,255,0), (0,0,255), (75,0,130), (148,0,211)]
pencolor(colors[level % len(colors)])
```

## Advanced Patterns

### 1. Random Variation
Add natural randomness:
```python
import random
angle_variation = random.uniform(-10, 10)
actual_angle = base_angle + angle_variation
```

### 2. Leaf Addition
Add leaves at terminal branches:
```python
if level == 1:  # Terminal branch
    turtle.dot(5, "green")  # Draw a leaf
```

### 3. Seasonal Growth
Animate tree growth over time:
```python
for current_level in range(1, max_level + 1):
    clear_screen()
    draw_branch(size, current_level)
    time.sleep(0.5)
```

## Creative Modifications

1. **Flower Trees**: Add colorful dots at branch ends
2. **Lightning Trees**: Use white/yellow on black background
3. **Coral Trees**: Underwater theme with blue gradients
4. **Crystal Trees**: Sharp angles and metallic colors
5. **Vine Trees**: Curved branches using turtle.circle()
