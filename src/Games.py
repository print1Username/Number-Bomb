import random

class Games:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

        self.random_number = 0
        self.insert_number = -1

    def SetNumber(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.ResetNumber()

        if self.minimum > self.maximum:
            raise ValueError(f"Minimum {self.minimum} must be less than maximum {self.maximum}")

    def ResetNumber(self):
        self.random_number = random.randint(self.minimum, self.maximum)
        self.insert_number = -1

    def InsertNumber(self, number):
        self.insert_number = number
