# 🌳 Fractal Tree Visualizer

A beautiful, recursive fractal tree visualization built using Python's **Turtle Graphics** library. This project demonstrates how simple recursive algorithms can generate complex, nature-inspired patterns — combining algorithmic thinking, mathematical modeling, and interactive visualization.

> 🎓 Developed as part of the coursework at **Visvesvaraya Technological University (VTU)**

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

## 📖 Overview

The **Fractal Tree Visualizer** generates realistic, tree-like branching structures using recursion. By repeatedly drawing smaller branches at varying angles and lengths, the program creates intricate fractal patterns that closely resemble trees found in nature — all rendered live using Python's Turtle Graphics engine.

This project was built to explore the intersection of **recursion, mathematics, and visualization**, while also providing a fully customizable and interactive drawing experience.

---

## ✨ Features

- 🌲 **Recursive Tree Generation** — Implements a recursive algorithm to build fractal tree structures branch by branch.
- 🐢 **Turtle Graphics Rendering** — Uses Python's built-in Turtle module for smooth, real-time visualization of branches, angles, and patterns.
- 📐 **Algorithmic & Mathematical Modeling** — Controls recursion depth and branch variation through configurable mathematical parameters.
- 🎛️ **Interactive Customization** — Adjust tree depth, branch size/length, branch angle, and drawing speed on the fly.
- 🧩 **Modular Codebase** — Clean separation of configuration, core algorithm, examples, and documentation for easy extension.
- 📚 **Well-Documented** — Includes dedicated docs for the algorithm, API reference, and project structure.

---

## 🗂️ Project Structure

```
Fractal-Tree/
├── Fractal-Tree.py                 # Main entry point for the visualizer
├── fractal_tree_refactored.py      # Refactored/optimized version of the core algorithm
├── config.py                       # Configuration settings (depth, angle, length, speed, colors)
├── basic_usage_example.py          # Simple example script to get started quickly
├── examples_generator.py           # Script to generate multiple tree variations
├── requirements.txt                # Project dependencies
├── API_REFERENCE.md                # Detailed API/function documentation
├── algorithm_documentation.md      # Explanation of the recursive algorithm & math behind it
├── variations_documentation.md     # Documentation on the different tree variations supported
├── PROJECT_STRUCTURE.md            # Overview of file/folder organization
├── LICENSE.txt                     # MIT License
└── README.md                       # Project documentation (this file)
```

> 📄 See [`PROJECT_STRUCTURE.md`](./PROJECT_STRUCTURE.md) for a more detailed breakdown.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- `turtle` module (included with standard Python installation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0PKunal/Fractal-Tree.git
   cd Fractal-Tree
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   

### Topics:

python
turtle
turtle-graphics
fractal
fractal-tree
recursion
algorithm
visualization
mathematics
computer-graphics


### Usage

Run the main script to generate a fractal tree:
```bash
python Fractal-Tree.py
```

Or try the beginner-friendly example:
```bash
python basic_usage_example.py
```

To generate multiple tree variations at once:
```bash
python examples_generator.py
```

### Customization

Tree parameters such as **recursion depth**, **branch length**, **angle**, and **drawing speed** can be adjusted in `config.py` to produce different tree shapes and styles — from sparse saplings to dense, bushy trees.

---

## 🧠 How It Works

The visualizer uses a **recursive function** that:
1. Draws a branch of a given length.
2. Reduces the length by a set ratio for the next level of branches.
3. Rotates the turtle by a defined angle to draw left and right sub-branches.
4. Repeats the process until the maximum recursion depth is reached.

This mirrors the natural branching pattern seen in real trees and is a classic demonstration of **recursion** and **self-similarity** in computer science and mathematics.

> 📄 For an in-depth explanation, see [`algorithm_documentation.md`](./algorithm_documentation.md)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3   |
| Graphics  | Turtle Graphics |
| Paradigm  | Recursive Algorithms |

---

## 🎯 Skills Demonstrated

- Recursive algorithm design
- Mathematical modeling (angles, ratios, recursion depth control)
- Data visualization using Turtle Graphics
- Python programming & modular code design
- Problem-solving and creative/generative design

---

## 📸 Preview

*(Add a screenshot or GIF of the generated fractal tree here for a visual preview!)*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/0PKunal/Fractal-Tree/issues) or submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE.txt](./LICENSE.txt) file for details.

---

## 👤 Author

Sakina Muzzammil

