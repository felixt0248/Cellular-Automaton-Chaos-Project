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
        self.initial_age = r["initial_age"]
        self.time_to_reproduce = r["time_to_reproduce"]
        self.age = self.initial_age

    def move(self):
        self.age += 1
        adj = self.get_adjacent()
        adj_water = list(filter(lambda c: isinstance(c, Water), adj))
        if len(adj_water) != 0:
            move_to = random.choice(adj_water)
            if self.age >= self.time_to_reproduce:
                self.wator.move_cell(self, move_to, Fish(self.wator, self.x, self.y, self.r))
                self.age = self.initial_age
            else:
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
        self.energy -= self.energy_loss
        if self.energy <= 0:
            self.wator.replace_cell(self, Water(self.wator, self.x, self.y))
            return # sharkie dies
        elif self.energy > self.max_energy:
            self.energy = self.max_energy
        adj = self.get_adjacent()
        adj_fish = list(filter(lambda c: isinstance(c, Fish), adj))
        adj_water = list(filter(lambda c: isinstance(c, Water), adj))
        if len(adj_fish) != 0:
            self.energy += self.energy_gain # shark can reproduce while eating the fish because of this ordering
            move_to = random.choice(adj_fish)
            if self.energy >= self.energy_to_reproduce:
                self.wator.move_cell(self, move_to, Shark(self.wator, self.x, self.y, self.r))
            else:
                self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))
        elif len(adj_fish) == 0 and len(adj_water) != 0:
            move_to = random.choice(adj_water)
            self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))
