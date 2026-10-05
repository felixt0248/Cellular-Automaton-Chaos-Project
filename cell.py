class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass

    def get_adjacent(self):
        pass

class Water(Cell):
    def move(self):
        pass

class Animal(Cell):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r # reproductive parameter e.g. energy for sharks

class Fish(Animal):
    def move(self):
        pass

class Shark(Animal):
    def move(self):
        pass
