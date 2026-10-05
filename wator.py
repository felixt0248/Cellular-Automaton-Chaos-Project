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
        grid = [[Water(x, y) for x in range(self.x_size)] for y in range(self.y_size)]
        return grid

    def place_animals_randomly(self, animal, n_animals, r):
        while n_animals > 0:
            x = random.randint(0, self.x_size - 1)
            y = random.randint(0, self.y_size - 1)
            if isinstance(self.grid[y][x], Water):
                self.grid[y][x] = animal(x, y, r)
                n_animals -= 1
