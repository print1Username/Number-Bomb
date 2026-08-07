import random

class Games:
    def __init__(self):

        # If the user guess the number, the range number will change, and the minimum and maximum still same
        self.minimum = 0
        self.maximum = 0

        self.minimum_range = 0
        self.maximum_range = 0

        self.random_number = 0

        self.chance = 0

    def SetNumber(self, minimum, maximum, chance):
        if minimum > maximum:
            raise ValueError(f"Minimum {minimum} must be less than maximum {maximum}")
        if chance < 0:
            raise ValueError(f"Chance {chance} must bigger than 0")
        else:
            self.minimum = minimum
            self.maximum = maximum

            self.minimum_range = minimum
            self.maximum_range = maximum

            self.chance = chance
            self.ResetGame()


    def ResetGame(self):
        self.random_number = random.randint(self.minimum, self.maximum)


    def CompareNumber(self, number):
        if number == self.random_number:
            print('Guess correct')
        elif number > self.random_number:
            print('Guess number is bigger than the random number')
        elif number < self.random_number:
            print('Guess number is smaller than the random number')