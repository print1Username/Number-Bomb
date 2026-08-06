from src.Windows import Windows
from src.Games import Games

class App:
    def __init__(self):
        self.windows = Windows()
        self.windows.LoadIconFiles('./assets/icon.ico')

        # Number Value
        self.games = Games()
        self.minimum_number = 0
        self.maximum_number = 0

        self.game_status = 1

        print('Window loaded successful.')


    def SetGameStatus(self, status):
        self.game_status = status
        self.GameLoop()


    def GameMenu(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Number Bomb')
        self.windows.LoadContent('This is the Number Bomb game,')

        self.minimum_number = self.windows.LoadInsert('Min')
        self.maximum_number = self.windows.LoadInsert('Max')

        self.windows.LoadButton('Start', command_func=lambda: self.SetGameStatus(2))


    def GameStart(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Guess Number')
        self.windows.LoadContent('Your Number Value:')

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
