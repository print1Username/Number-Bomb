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


    def SetGameStatus(self, status):
        # Check user status
        if status == 2:
            min_str = self.minimum_input.get()
            max_str = self.maximum_input.get()
            chance_str = self.chance_input.get()

            if not min_str.isdigit() or not max_str.isdigit() or not chance_str.isdigit():
                self.windows.ShowError("Please enter a valid number.")
                return

            self.minimum_value = int(min_str)
            self.maximum_value = int(max_str)
            self.chance_value = int(chance_str)

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

        self.minimum_input = self.windows.LoadInsert('Min')
        self.maximum_input = self.windows.LoadInsert('Max')
        self.chance_input = self.windows.LoadInsert('chance')

        self.windows.LoadButton('Start', command_func=lambda: self.SetGameStatus(2))


    def GameStart(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Guess Number')
        self.windows.LoadContent('Your Number Value:')
        self.windows.LoadContent(f'Range: {self.minimum_value} ~ {self.maximum_value}')
        self.windows.LoadContent(f'Chance: {self.chance_value}')

        self.windows.LoadInsert('Guess Number')
        self.windows.LoadButton('Guess')


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
