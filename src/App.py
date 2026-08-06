from src.Windows import Windows
from src.Games import Games

class App:
    def __init__(self):
        self.windows = Windows()
        self.windows.LoadIconFiles('./assets/icon.ico')

        self.windows.LoadTitle('Number Bomb')
        self.windows.LoadContent('This is the Number Bomb game,')

        self.windows.LoadInsert('Min')
        self.windows.LoadInsert('Max')

        self.windows.LoadButton('Start')

        # Window loop
        self.windows.mainloop()