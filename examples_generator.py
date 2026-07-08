"""
Examples of different fractal tree variations.
Run this script to generate multiple tree examples.
"""

import turtle
import os
from src.fractal_tree import FractalTree
from src.config import TREE_PRESETS


def clear_screen():
    """Clear the turtle screen."""
    turtle.clear()


def generate_examples():
    """Generate multiple fractal tree examples."""

    # Create examples directory if it doesn't exist
    if not os.path.exists('examples'):
        os.makedirs('examples')

    # Generate trees with different presets
    for preset_name, params in TREE_PRESETS.items():
        print(f"Generating {preset_name} tree...")

        clear_screen()
        tree = FractalTree(**params)
        tree.draw_branch(tree.size, tree.level)

        # Save the image
        tree.save_image(f"examples/{preset_name}_tree")

        input(f"Press Enter to continue to next example...")


if __name__ == "__main__":
    generate_examples()
