# Conway's Game of Life

A Python implementation of Conway's Game of Life, featuring an animated visualization of the cellular automaton. This implementation includes random initialization and support for adding classic patterns like gliders and blinkers.

## 🎮 Features

- Interactive visualization using Matplotlib
- Random grid initialization
- Toroidal grid (edges wrap around)
- Support for classic patterns (gliders, blinkers)
- Configurable grid size
- Clean, object-oriented implementation

## 🛠️ Requirements

- Python 3.7+
- NumPy
- Matplotlib

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/sojoudian/Conway_Python.git
cd Conway_Python/
```

2. Install required packages:
```bash
python3 -m venv env && source env/bin/activate
pip install numpy matplotlib
```

## 🚀 Usage

### Basic Usage

Run the simulation with default settings:

```python
python game_of_life.py
```

### Custom Initialization

```python
from game_of_life import GameOfLife, create_animation

# Create a game with custom size
game = GameOfLife(size=75)

# Add some classic patterns
add_glider(game, 10, 10)
add_blinker(game, 20, 20)

# Start the animation
create_animation()
```

## 🎲 Game Rules

The Game of Life follows four simple rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## 🏗️ Project Structure

```
game_of_life/
├── game_of_life.py    # Main implementation
├── README.md          # This file
└── requirements.txt   # Package dependencies
```

## 🎯 Class Overview

### GameOfLife

The main class that handles the game logic:

- `__init__(size=50, random_init=True)`: Initialize the game grid
- `get_neighbors(i, j)`: Count live neighbors for a cell
- `next_generation()`: Calculate the next generation of cells

### Helper Functions

- `create_animation()`: Set up and run the Matplotlib animation
- `add_glider(game, x, y)`: Add a glider pattern at specified coordinates
- `add_blinker(game, x, y)`: Add a blinker pattern at specified coordinates

## 🎨 Customization

You can customize various aspects of the simulation:

```python
# Change grid size
game = GameOfLife(size=100)

# Initialize with empty grid
game = GameOfLife(random_init=False)

# Modify animation speed
anim = FuncAnimation(fig, update, frames=200, interval=50)  # Faster animation
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Add new patterns
2. Improve visualization
3. Optimize performance
4. Add new features
5. Fix bugs

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- John Conway for creating the Game of Life
- NumPy and Matplotlib development teams
- The cellular automata community

## 📫 Contact

For questions and feedback:
- Create an issue in the repository
- Send a pull request
- Contact: http://maziar.email

---
Made with ❤️  by Maziar

