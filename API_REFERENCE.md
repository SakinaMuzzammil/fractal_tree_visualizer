# 🔧 API Reference

## FractalTree Class

### Constructor

```python
FractalTree(size=80, level=7, angle=30, scale=0.8)
```

#### Parameters
- **size** (int): Initial trunk size in pixels (default: 80)
- **level** (int): Recursion depth, controls tree complexity (default: 7)
- **angle** (int): Branching angle in degrees (default: 30)
- **scale** (float): Size reduction factor for each level (default: 0.8)

### Methods

#### `draw_branch(size, level)`
Recursively draws fractal tree branches.

**Parameters:**
- `size` (float): Current branch size
- `level` (int): Current recursion level

**Returns:** None

#### `generate()`
Generates and displays the complete fractal tree.

**Returns:** None

#### `set_color(level)`
Sets pen color based on recursion level.

**Parameters:**
- `level` (int): Current recursion level

**Returns:** None

#### `save_image(filename)`
Saves the current turtle canvas as an image file.

**Parameters:**
- `filename` (str): Output filename (without extension)

**Returns:** None

## Configuration Module

### Constants

```python
DEFAULT_SIZE = 80
DEFAULT_LEVEL = 7
DEFAULT_ANGLE = 30
DEFAULT_SCALE = 0.8
```

### Color Schemes

```python
COLOR_SCHEMES = {
    'green': lambda level: (0, 255 // level, 0),
    'autumn': lambda level: (255 // level, 165 // level, 0),
    'blue': lambda level: (0, 0, 255 // level),
    'rainbow': lambda level: (255 // level, 128 // level, 64 // level)
}
```

### Tree Presets

```python
TREE_PRESETS = {
    'small': {'size': 60, 'level': 5, 'angle': 25, 'scale': 0.75},
    'medium': {'size': 80, 'level': 7, 'angle': 30, 'scale': 0.8},
    'large': {'size': 100, 'level': 9, 'angle': 35, 'scale': 0.85},
    'bushy': {'size': 70, 'level': 8, 'angle': 45, 'scale': 0.7},
    'sparse': {'size': 90, 'level': 6, 'angle': 20, 'scale': 0.9}
}
```

## Usage Examples

### Basic Usage
```python
from src.fractal_tree import FractalTree

# Create default tree
tree = FractalTree()
tree.generate()
```

### Custom Parameters
```python
# Create custom tree
tree = FractalTree(size=120, level=9, angle=25, scale=0.85)
tree.generate()
```

### Using Presets
```python
from src.config import TREE_PRESETS

# Use a preset configuration
preset = TREE_PRESETS['bushy']
tree = FractalTree(**preset)
tree.generate()
```

### Saving Images
```python
tree = FractalTree()
tree.draw_branch(tree.size, tree.level)
tree.save_image("my_fractal_tree")
```
