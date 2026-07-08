"""
Basic usage example for the Fractal Tree Generator.
This demonstrates the simplest way to create and display a fractal tree.
"""

from src.fractal_tree import FractalTree


def main():
    """Create and display a basic fractal tree."""

    # Method 1: Use default settings
    print("Generating default fractal tree...")
    default_tree = FractalTree()
    default_tree.generate()

    # Method 2: Custom parameters
    print("Generating custom fractal tree...")
    custom_tree = FractalTree(
        size=100,      # Larger tree
        level=8,       # More recursion levels
        angle=25,      # Smaller branching angle
        scale=0.75     # More dramatic size reduction
    )
    custom_tree.generate()


if __name__ == "__main__":
    main()
