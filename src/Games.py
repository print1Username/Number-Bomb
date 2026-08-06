import random

class Games:
    def __init__(self, min, max):
        self.minimum = min
        self.maximum = max

        self.random_number = 0
        self.insert_number = -1

        self.ResetNumber()

    def ResetNumber(self):
        self.random_number = random.randint(self.minimum, self.maximum)
        self.insert_number = -1

    def InsertNumber(self, number):
        if number == self.random_number:
            return 0
