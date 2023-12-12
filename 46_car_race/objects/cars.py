import random

class Cars:

    def __init__(self, color, mileage = 0):
        self.color = color
        self.mileage = mileage

    def advance(self):
        self.mileage += random.randint(1, 3)