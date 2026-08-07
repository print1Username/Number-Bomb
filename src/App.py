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

        self.maximum_input = None
        self.minimum_input = None
        self.chance_input = None

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
            try:
                self.minimum_value = self.CheckNumberValid(self.minimum_input.get())
                self.maximum_value = self.CheckNumberValid(self.maximum_input.get())
                self.chance_value = self.CheckNumberValid(self.chance_input.get())

            except ValueError:
                return

            if self.minimum_value >= self.maximum_value:
                self.windows.ShowError("The minimum value must be less than the maximum value.")
                return

            if self.chance_value <= 0:
                self.windows.ShowError("The chance value must be greater than zero.")
                return

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
        self.windows.LoadContent(f'range: {self.minimum_value} ~ {self.maximum_value}')
        self.windows.LoadContent(f'chance: {self.chance_value}')

        self.games.SetNumber(self.minimum_value, self.maximum_value, self.chance_value)

        self.windows.LoadInsert('Guess Number')
        self.windows.LoadButton('Guess', command_func=lambda: self.NumberDetermination())


    def NumberDetermination(self):
        pass


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
