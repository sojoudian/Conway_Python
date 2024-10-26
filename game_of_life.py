import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class GameOfLife:
    def __init__(self, size=50, random_init=True):
        self.size = size
        if random_init:
            self.grid = np.random.choice([0, 1], size=(size, size), p=[0.85, 0.15])
        else:
            self.grid = np.zeros((size, size))
    
    def get_neighbors(self, i, j):
        """Count the number of live neighbors for a cell."""
        total = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                row = (i + x) % self.size
                col = (j + y) % self.size
                total += self.grid[row, col]
        return total
    
    def next_generation(self):
        """Calculate the next generation based on Conway's rules."""
        new_grid = self.grid.copy()
        for i in range(self.size):
            for j in range(self.size):
                neighbors = self.get_neighbors(i, j)
                # Rules of Life
                if self.grid[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i, j] = 0
                else:
                    if neighbors == 3:
                        new_grid[i, j] = 1
        self.grid = new_grid
        return self.grid

def create_animation():
    # Initialize the game
    game = GameOfLife(size=50)
    fig, ax = plt.subplots()
    
    # Create the initial plot
    img = ax.imshow(game.grid, interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    
    def update(frame):
        game.next_generation()
        img.set_array(game.grid)
        return [img]
    
    # Create the animation
    anim = FuncAnimation(fig, update, frames=200, interval=100, blit=True)
    plt.show()

if __name__ == "__main__":
    create_animation()

# Example patterns you can add manually:
def add_glider(game, x, y):
    """Add a glider pattern at position (x, y)"""
    glider = np.array([[0, 1, 0],
                      [0, 0, 1],
                      [1, 1, 1]])
    game.grid[x:x+3, y:y+3] = glider

def add_blinker(game, x, y):
    """Add a blinker pattern at position (x, y)"""
    game.grid[x:x+3, y] = 1
