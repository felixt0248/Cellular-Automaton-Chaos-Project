import random

from cell import Water, Fish, Shark

class WaTor:
    def __init__(self, x_size, y_size, n_fish, n_shark, r_fish, r_shark):
        self.x_size = x_size
        self.y_size = y_size
        self.n_fish = n_fish
        self.n_shark = n_shark

        self.grid = self.grid_init() # NOTE: to reference a grid coordinate use self.grid[y][x]
        self.place_animals_randomly(Fish, n_fish, r_fish)
        self.place_animals_randomly(Shark, n_shark, r_shark)

    def grid_init(self):
        grid = [[Water(self, x, y) for x in range(self.x_size)] for y in range(self.y_size)]
        return grid

    def place_animals_randomly(self, animal, n_animals, r):
        while n_animals > 0:
            x = random.randint(0, self.x_size - 1)
            y = random.randint(0, self.y_size - 1)
            if isinstance(self.grid[y][x], Water):
                self.grid[y][x] = animal(self, x, y, r)
                n_animals -= 1

    def get_adjacent(self, cell):
        x = cell.x
        y = cell.y
        return (self.grid[(y+1)%self.y_size][x], self.grid[y][(x+1)%self.x_size], self.grid[y-1][x], self.grid[y][x-1])

    # also responsible for swapping the coords stored within cells
    def move_cell(self, cell_from, cell_to, cell_replace):
        self.grid[cell_to.y][cell_to.x] = cell_from
        self.grid[cell_from.y][cell_from.x] = cell_replace
        cell_from.x = cell_to.x
        cell_from.y = cell_to.y
        if isinstance(cell_to, Fish):
            self.n_fish -= 1
        if isinstance(cell_replace, Fish):
            self.n_fish += 1
        if isinstance(cell_replace, Shark):
            self.n_shark += 1

    def simulate_row(self, y):
        for x in range(self.x_size):
            self.grid[y][x].move()

    def simulate_grid_once(self):
        for y in range(self.y_size):
            self.simulate_row(y)

    def simulate_n_steps(self, n):
        for _ in range (n):
            self.simulate_grid_once()
