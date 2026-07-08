"""
Configuration settings for the Fractal Tree Generator.
"""

# Default tree parameters
DEFAULT_SIZE = 80
DEFAULT_LEVEL = 7
DEFAULT_ANGLE = 30
DEFAULT_SCALE = 0.8

# Color schemes
COLOR_SCHEMES = {
    'green': lambda level: (0, 255 // level, 0),
    'autumn': lambda level: (255 // level, 165 // level, 0),
    'blue': lambda level: (0, 0, 255 // level),
    'rainbow': lambda level: (255 // level, 128 // level, 64 // level)
}

# Preset configurations for different tree styles
TREE_PRESETS = {
    'small': {'size': 60, 'level': 5, 'angle': 25, 'scale': 0.75},
    'medium': {'size': 80, 'level': 7, 'angle': 30, 'scale': 0.8},
    'large': {'size': 100, 'level': 9, 'angle': 35, 'scale': 0.85},
    'bushy': {'size': 70, 'level': 8, 'angle': 45, 'scale': 0.7},
    'sparse': {'size': 90, 'level': 6, 'angle': 20, 'scale': 0.9}
}
