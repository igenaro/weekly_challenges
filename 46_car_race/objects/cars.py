import random

class Cars:

    def __init__(self, color, icon, mileage = 0, winner = False, working = True):
        self.color = color
        self.mileage = mileage
        self.icon = icon
        self.winner = winner
        self.working = working

    def advance(self):
        self.mileage += random.randint(1, 3)
    
    def winner_flag(self):
        self.winner = True
    
    def crash(self):
        self.working = False

    def repair(self):
        self.working = True