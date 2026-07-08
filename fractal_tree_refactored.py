"""
Fractal Tree Generator
A beautiful recursive fractal tree implementation using Python's turtle graphics.

Author: Kunal (@0PKunal)
"""

import turtle
from typing import Tuple


class FractalTree:
    """A class to generate and customize fractal trees."""

    def __init__(self, size: int = 80, level: int = 7, angle: int = 30, scale: float = 0.8):
        """
        Initialize the fractal tree parameters.

        Args:
            size (int): Initial trunk size
            level (int): Recursion depth (complexity)
            angle (int): Branching angle in degrees
            scale (float): Size reduction factor for each level
        """
        self.size = size
        self.level = level
        self.angle = angle
        self.scale = scale

        # Setup turtle
        turtle.speed('fastest')
        turtle.right(-90)  # Face upward
        turtle.colormode(255)

    def set_color(self, level: int) -> None:
        """Set pen color based on recursion level."""
        if level > 0:
            green_intensity = 255 // level
            turtle.pencolor(0, green_intensity, 0)

    def draw_branch(self, size: float, level: int) -> None:
        """
        Recursively draw fractal tree branches.

        Args:
            size (float): Current branch size
            level (int): Current recursion level
        """
        if level > 0:
            self.set_color(level)

            # Draw the trunk
            turtle.forward(size)

            # Draw right branch
            turtle.right(self.angle)
            self.draw_branch(self.scale * size, level - 1)

            # Draw left branch
            turtle.left(2 * self.angle)
            self.draw_branch(self.scale * size, level - 1)

            # Return to original position
            turtle.right(self.angle)
            turtle.backward(size)

    def generate(self) -> None:
        """Generate and display the fractal tree."""
        self.draw_branch(self.size, self.level)
        turtle.done()

    def save_image(self, filename: str) -> None:
        """Save the current turtle canvas as an image."""
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file=f"{filename}.eps")
        print(f"Tree saved as {filename}.eps")


def main():
    """Main function to create and display the fractal tree."""
    # Create default fractal tree
    tree = FractalTree()

    # Generate the tree
    tree.generate()


if __name__ == "__main__":
    main()
