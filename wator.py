import random
from concurrent import futures

from cell import Water, Fish, Shark

class WaTor:
    def __init__(self, starting_params):
        self.x_size = starting_params["x_size"]
        self.y_size = starting_params["y_size"]
        self.n_fish = starting_params["n_fish"]
        self.n_shark = starting_params["n_shark"]
        self.r_fish = starting_params["r_fish"]
        self.r_shark = starting_params["r_shark"]
        self.name = f"x{self.x_size}y{self.y_size}f{self.n_fish}s{self.n_shark}"

        self.grid = self.grid_init() # NOTE: to reference a grid coordinate use self.grid[y][x]
        
        if self.n_fish + self.n_shark > self.x_size * self.y_size:
            raise Exception("too many animals")
        self.place_animals_randomly(Fish, self.n_fish, self.r_fish)
        self.place_animals_randomly(Shark, self.n_shark, self.r_shark)

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

    def replace_cell(self, cell_from, cell_replace):
        self.grid[cell_from.y][cell_from.x] = cell_replace
        if isinstance(cell_from, Fish):
            self.n_fish -= 1
        if isinstance(cell_from, Shark):
            self.n_shark -= 1
        if isinstance(cell_replace, Fish):
            self.n_fish += 1
        if isinstance(cell_replace, Shark):
            self.n_shark += 1

    def colour_grid(self, gen_animation):
        if gen_animation:
            return [[c.get_colour() for c in i] for i in self.grid]

    def simulate_row(self, y):
        for x in range(self.x_size):
            self.grid[y][x].move()

    def simulate_grid_once(self, gen_animation):
        for y in range(self.y_size):
            self.simulate_row(y)
        return (self.n_fish, self.n_shark, self.colour_grid(gen_animation))

    def simulate_n_steps(self, sim_params):
        n = sim_params["simulation_steps"]
        verbose = sim_params["verbose"]
        verbosity_interval = sim_params["verbosity_interval"]
        terminate_trivial = sim_params["terminate_trivial"]
        gen_animation = sim_params["gen_animation"]
        overview = [(self.n_fish, self.n_shark, self.colour_grid(gen_animation))]
        for i in range (n):
            overview.append(self.simulate_grid_once(gen_animation))
            if verbose and i % verbosity_interval == 0 and i != 0:
                print(f"{i} steps complete")
            if terminate_trivial and (self.n_fish == 0 or self.n_shark == 0):
                if verbose:
                    print("simulation done: extinction")
                return overview
        if verbose:
            print("simulation done")
        return self.name, overview

    def simulate_n_worlds(self, sim_params):
        n = sim_params["n_worlds"]
        with futures.ProcessPoolExecutor() as executor:
            fs = [executor.submit(self.simulate_n_steps, sim_params) for _ in range(n)]
            return [f.result() for f in futures.as_completed(fs)]
