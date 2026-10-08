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
        self.r = r # reproductive parameter e.g. energy for sharks

class Fish(Animal):
    def move(self):
        adj = self.get_adjacent()
        adj_water = list(filter(lambda c: isinstance(c, Water), adj))
        if len(adj_water) != 0:
            move_to = random.choice(adj_water)
            self.wator.move_cell(self, move_to, Water(self.wator, self.x, self.y))

class Shark(Animal):
    def move(self):
        pass
