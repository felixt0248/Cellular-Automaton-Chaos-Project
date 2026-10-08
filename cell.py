import random

class Cell:
    def __init__(self, wator, x, y):
        self.x = x
        self.y = y
        self.wator = wator

    def move(self):
        pass

    def get_adjacent(self):
        return self.wator.get_adjacent(self)

class Water(Cell):
    def move(self):
        pass

class Animal(Cell):
    def __init__(self, wator, x, y, r):
        super().__init__(wator, x, y)
        self.r = r # reproductive parameters e.g. energy, etc. for sharks

class Fish(Animal):
    def __init__(self, wator, x, y, r):
        super().__init__(wator, x, y, r)
        self.age = r["initial_age"]
        self.time_to_reproduce = r["time_to_reproduce"]

    def move(self):
        adj = self.get_adjacent()
        adj_water = list(filter(lambda c: isinstance(c, Water), adj))
        if len(adj_water) != 0:
            move_to = random.choice(adj_water)
            self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))

class Shark(Animal):
    def __init__(self, wator, x, y, r):
        super().__init__(wator, x, y, r)
        self.energy = r["initial_energy"]
        self.max_energy = r["max_energy"]
        self.energy_gain = r["energy_gain"]
        self.energy_loss = r["energy_loss"]
        self.energy_to_reproduce = r["energy_to_reproduce"]

    def move(self):
        adj = self.get_adjacent()
        adj_fish = list(filter(lambda c: isinstance(c, Fish), adj))
        adj_water = list(filter(lambda c: isinstance(c, Water), adj))
        if len(adj_fish) != 0:
            move_to = random.choice(adj_fish)
            self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))
        elif len(adj_fish) == 0 and len(adj_water) != 0:
            move_to = random.choice(adj_water)
            self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))
