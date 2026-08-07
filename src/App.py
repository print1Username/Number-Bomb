from src.Windows import Windows
from src.Games import Games

class App:
    def __init__(self):
        self.windows = Windows()
        self.windows.LoadIconFiles('./assets/icon.ico')

        # Number Value
        self.games = Games()
        self.minimum_value = 0
        self.maximum_value = 0
        self.chance_value = 0
        self.number_value = -1

        self.maximum_input = None
        self.minimum_input = None
        self.chance_input = None
        self.number_input = None

        self.game_status = 1

        print('Window loaded successful.')


    def CheckNumberValid(self, input_value):
        if not input_value.isdigit():
            self.windows.ShowError(f"[{input_value}] is not a valid number.")
            return -1

        return int(input_value)


    def SetGameStatus(self, status):
        # Check user status
        if status == 2:
            self.minimum_value = self.CheckNumberValid(self.minimum_input.get())
            self.maximum_value = self.CheckNumberValid(self.maximum_input.get())
            self.chance_value = self.CheckNumberValid(self.chance_input.get())

            if self.minimum_value < 0 or self.maximum_value < 0 or self.chance_value < 0:
                return

            if self.minimum_value >= self.maximum_value:
                self.windows.ShowError("The minimum value must be less than the maximum value.")
                return

            if self.chance_value <= 0:
                self.windows.ShowError("The chance value must be greater than zero.")
                return

            self.games.SetNumber(self.minimum_value, self.maximum_value, self.chance_value)

        self.game_status = status
        self.GameLoop()


    def GameMenu(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Number Bomb')
        self.windows.LoadContent('This is the Number Bomb game, \nyou need to guess the random number \nwith the limited chance.')

        self.minimum_input = self.windows.LoadInsert('Min value')
        self.maximum_input = self.windows.LoadInsert('Max value')
        self.chance_input = self.windows.LoadInsert('chance')

        self.windows.LoadButton('Start', command_func=lambda: self.SetGameStatus(2))


    def GameStart(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Guess Number')
        self.windows.LoadContent('Your Number Value:')
        self.windows.LoadContent(f'range: {self.games.minimum} ~ {self.games.maximum}')
        self.windows.LoadContent(f'chance: {self.games.chance}')


        self.number_input = self.windows.LoadInsert('Guess Number')
        self.windows.LoadButton('Guess', command_func=lambda: self.NumberDeterminate())


    def NumberDeterminate(self):
        self.number_value = self.CheckNumberValid(self.number_input.get())

        if self.number_value < 0:
            return

        if self.number_value < self.games.minimum or self.number_value > self.games.maximum:
            self.windows.ShowError("The guess number must be within the current range.")
            return

        result = self.games.CompareNumber(self.number_value)

        match result:
            case 0:
                self.windows.ShowInfo('Congratulations, you guessed the number.')
                self.SetGameStatus(1)

            case 1:
                self.windows.ShowInfo('Your number is smaller than the random number.')

            case 2:
                self.windows.ShowInfo('Your number is bigger than the random number.')

        if result != 0:
            if self.games.chance <= 0:
                self.windows.ShowInfo('You have no chances left. Game over.')
                self.SetGameStatus(1)
            else:
                self.GameStart()

    def GameLoop(self):
        # Window loop
        match self.game_status:
            case 1:
                self.GameMenu()
            case 2:
                self.GameStart()


    def Run(self):
        self.GameLoop()
        self.windows.mainloop()
