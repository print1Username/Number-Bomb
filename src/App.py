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

    def GameStatus(self):
        if self.game_status == 1:
            self.GameMenu()

    def GameMenu(self):
        self.windows.LoadTitle('Number Bomb')
        self.windows.LoadContent('This is the Number Bomb game,')

        self.minimum_number = self.windows.LoadInsert('Min')
        self.maximum_number = self.windows.LoadInsert('Max')

        self.windows.LoadButton('Start')

    def GameLoop(self):
        # Window loop
        self.windows.mainloop()