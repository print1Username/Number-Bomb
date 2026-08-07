from src.Windows import Windows
from src.Games import Games

class App:
    def __init__(self):
        self.windows = Windows()
        self.windows.LoadIconFiles('./assets/icon.ico')
        self.windows.bind('<Return>', self.HandleEnter)
        self.windows.bind('<Escape>', self.ConfirmExit)

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

        self.enter_action = None
        self.game_status = 1

        print('Window loaded successful.')


    def CheckNumberValid(self, input_value):
        if not input_value.isdigit():
            self.windows.ShowError(f"[{input_value}] is not a valid number.")
            return -1

        return int(input_value)


    def SetEnterAction(self, command_func):
        self.enter_action = command_func


    def HandleEnter(self, event=None):
        if self.enter_action is not None:
            self.enter_action()
        return 'break'


    def ConfirmExit(self, event=None):
        message = 'Are you sure you want to exit?\nPress Enter to exit, Esc to stay.'
        if self.windows.ShowConfirm(message):
            self.windows.destroy()
        return 'break'


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

        start_action = lambda: self.SetGameStatus(2)
        self.SetEnterAction(start_action)
        self.windows.LoadButton('Start', command_func=start_action)


    def GameStart(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Guess Number')
        self.windows.LoadContent('Your Number Value:')
        self.windows.LoadContent(f'range: {self.games.minimum} ~ {self.games.maximum}')
        self.windows.LoadContent(f'chance: {self.games.chance}')

        self.number_input = self.windows.LoadInsert('Guess Number')

        guess_action = lambda: self.NumberDeterminate()
        self.SetEnterAction(guess_action)
        self.windows.LoadButton('Guess', command_func=guess_action)


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
                self.SetGameStatus(3)

            case 1:
                self.windows.ShowInfo('Your number is smaller than the random number.')

            case 2:
                self.windows.ShowInfo('Your number is bigger than the random number.')

        if result != 0:
            if self.games.chance <= 0:
                self.SetGameStatus(4)
            else:
                self.GameStart()


    def GameWin(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Congratulations')
        self.windows.LoadContent('You guessed the number!')
        self.windows.LoadContent(f'The correct answer is {self.games.random_number}.')

        back_action = lambda: self.SetGameStatus(1)
        self.SetEnterAction(back_action)
        self.windows.LoadButton('Back', command_func=back_action)


    def GameLose(self):
        self.windows.ClearWindows()

        self.windows.LoadTitle('Game Over')
        self.windows.LoadContent('You did not guess the number.')
        self.windows.LoadContent(f'The correct answer is {self.games.random_number}.')

        back_action = lambda: self.SetGameStatus(1)
        self.SetEnterAction(back_action)
        self.windows.LoadButton('Back', command_func=back_action)


    def GameLoop(self):
        # Window loop
        match self.game_status:
            case 1:
                self.GameMenu()
            case 2:
                self.GameStart()
            case 3:
                self.GameWin()
            case 4:
                self.GameLose()


    def Run(self):
        self.GameLoop()
        self.windows.mainloop()