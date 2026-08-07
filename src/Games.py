import random


class Games:
    def __init__(self):

        # If the user guess the number, the range number will change, and the minimum and maximum still same
        self.minimum = 0
        self.maximum = 0

        self.random_number = 0

        self.chance = 0

    def SetNumber(self, minimum, maximum, chance):
        if minimum < 0 or maximum < 0:
            raise ValueError('Invalid range')
        if minimum > maximum:
            raise ValueError(f"Minimum {minimum} must be less than maximum {maximum}")
        if chance < 0:
            raise ValueError(f"Chance {chance} must bigger than 0")
        else:
            self.minimum = minimum
            self.maximum = maximum

            self.chance = chance
            self.ResetGame()

            print('Value set successfully')


    def ResetGame(self):
        self.random_number = random.randint(self.minimum, self.maximum)
        print('Game reset successfully')


    def CompareNumber(self, number):
        if number == self.random_number:
            print('Guess correct')
            return 0

        elif number < self.random_number:
            print('Guess number is smaller than the random number')
            self.minimum = number + 1
            self.chance -= 1
            return 1

        elif number > self.random_number:
            print('Guess number is bigger than the random number')
            self.maximum = number - 1
            self.chance -= 1
            return 2

        else:
            return -1


    def PrintNumber(self):
        return self.minimum, self.maximum, self.chance