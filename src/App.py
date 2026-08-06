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

        self.game_status = 1

        print('Window loaded successful.')


    def SetGameStatus(self, status):
        # Check user status
        if status == 2:
            min_str = self.minimum_input.get()
            max_str = self.maximum_input.get()

            if not min_str.isdigit() or not max_str.isdigit():
                self.windows.ShowError("Please enter a valid number.")
                return

            self.minimum_value = int(min_str)
            self.maximum_value = int(max_str)

            if self.minimum_value >= self.maximum_value:
                self.windows.ShowError("The minimum value must be less than the maximum value.")
                return


        self.game_status = status
        self.GameLoop()


    def GameMenu(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Number Bomb')
        self.windows.LoadContent('This is the Number Bomb game,')

        self.minimum_input = self.windows.LoadInsert('Min')
        self.maximum_input = self.windows.LoadInsert('Max')

        self.windows.LoadButton('Start', command_func=lambda: self.SetGameStatus(2))


    def GameStart(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Guess Number')
        self.windows.LoadContent('Your Number Value:')
        self.windows.LoadContent(f'Range: {self.minimum_value} to {self.maximum_value}')

        self.windows.LoadInsert('Guess Number')


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
