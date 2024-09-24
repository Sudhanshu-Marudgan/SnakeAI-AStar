# SnakeAI with A* Algorithm


## Overview 

This project implements an AI-controlled Snake game using the A* search algorithm to optimize pathfinding and ensure that the snake navigates the grid effectively while avoiding collisions. The AI snake autonomously plays the classic Snake game by finding the optimal path to reach the apple using A* algorithm, and continues to grow with each apple it consumes.


<p></p>


## Features

- **AI-Powered Snake:** The snake uses the A* search algorithm to intelligently find the shortest path to the apple.
- **Dynamic Grid Environment:** The game is built using a dynamic grid system, where the snake and apple are rendered in real-time.
- **Pygame Interface:** The game uses Pygame for graphical rendering, ensuring smooth visuals and gameplay.
- **Pathfinding:** The snake's path is recalculated dynamically as it moves, ensuring it adapts to changes in the environment.


## How It Works

- **Snake Movement:** The snake begins in the center of the grid and moves toward the apple. The A* algorithm calculates the optimal path based on the snake's current position and the apple's position.
- **Apple Placement:** The apple is placed randomly on the grid, avoiding the snake's current position.
- **Pathfinding with A\* Algorithm:** The A* algorithm ensures that the snake finds the shortest, collision-free path to the apple.


## A* Algorithm

The A* algorithm is used to determine the optimal path by considering both the distance from the snake’s current position to the goal (apple) and the cost of moving through each square on the grid. The algorithm recalculates the path after each movement or when the apple is consumed.


## Getting Started

## Prerequisites

Make sure you have the following installed on your system:
- **Python 3.x**
- **Pygame:** Install using the command:
  ```bash
    pip install pygame
    ```
- **Numpy:** Install using the command:
   ```bash
    pip install numpy
    ```


## Running the Code

1. Clone the Repository:
   ```bash
   git clone https://github.com/Sudhanshu-Marudgan/SnakeAI-AStar.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SnakeAI-AStar
   ```
3. Run the code:
   ```bash
   python snake_ai.py
   ```

The game will open in a new window, and the AI snake will begin navigating the grid towards the apple.


## Contributing

Feel free to fork this project and contribute by submitting a pull request.
contributions are always welcome!
  
