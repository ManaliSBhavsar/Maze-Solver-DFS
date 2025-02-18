# Maze Solver - Depth First Search (DFS)

This project visualizes a maze solver using the Depth First Search (DFS) algorithm. The maze is represented as a grid where "X" denotes walls and empty spaces are navigable. The algorithm starts at a source point and explores the maze recursively to find the shortest path to the target point, visualizing each step as it proceeds.

## Features:
- **Maze Representation**: A 2D grid-based maze is displayed using Tkinter.
- **DFS Algorithm**: Depth First Search is implemented to find a path from the source to the target.
- **Visualization**: As the DFS algorithm progresses, the path taken is displayed on the canvas with real-time updates.
- **Customizable Maze**: You can easily modify the maze layout by changing the input grid.

## Requirements:
- Python 3.x
- Tkinter (usually included with Python)

## How to Run:
1. Clone the repository
2. Navigate to the project directory
3. Run the program: python maze_solver.py


## Example:
The maze solver will visualize the process of navigating through the maze from the source (yellow) to the target (red). It uses DFS to explore possible paths, backtracking if it hits a dead-end.
