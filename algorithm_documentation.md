# Fractal Tree Algorithm

## Mathematical Foundation

The fractal tree is based on the concept of **self-similarity** and **recursive structures** found in nature. Each branch of the tree contains smaller versions of the entire tree structure.

## Algorithm Steps

### 1. Base Case
```
if level > 0:
    continue drawing
else:
    return (stop recursion)
```

### 2. Draw Current Branch
- Set color based on current recursion level
- Draw forward by the specified size

### 3. Recursive Branching
- Turn right by the branching angle
- Recursively draw right subtree with reduced size
- Turn left by twice the branching angle  
- Recursively draw left subtree with reduced size
- Return to original position and orientation

## Mathematical Properties

### Scaling Factor
Each subsequent level is scaled by a factor (default: 0.8):
```
new_size = current_size × scale_factor
```

### Tree Complexity
The total number of branches follows the formula:
```
total_branches = 2^0 + 2^1 + 2^2 + ... + 2^(level-1) = 2^level - 1
```

### Color Gradient
Color intensity varies with recursion level:
```
green_value = 255 ÷ current_level
```

## Variations

### Different Angles
- **30°**: Natural tree appearance
- **45°**: Bushier, wider spread
- **20°**: Tall, narrow tree
- **60°**: Very wide, short tree

### Scale Factors
- **0.7**: Dense, bushy appearance
- **0.8**: Balanced (default)
- **0.9**: Sparse, elongated branches

## Time Complexity
- **Time**: O(2^n) where n is the recursion level
- **Space**: O(n) for recursion stack depth
