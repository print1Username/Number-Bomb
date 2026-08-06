import random

class Games:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

        self.random_number = 0
        self.insert_number = -1

        self.chance = 0

    def SetNumber(self, minimum, maximum, chance):

        if self.minimum > self.maximum:
            raise ValueError(f"Minimum {self.minimum} must be less than maximum {self.maximum}")
        if chance < 0:
            raise ValueError(f"Chance {self.chance} must bigger than 0")

        self.minimum = minimum
        self.maximum = maximum
        self.chance = chance
        self.ResetNumber()

    def ResetNumber(self):
        self.random_number = random.randint(self.minimum, self.maximum)
        self.insert_number = -1

    def InsertNumber(self, number):
        self.insert_number = number
