from os import system, name
import random
from time import sleep
import sys
from Error import InputError

VALID_RANGE = range(1, 10)
DEFAULT = " "
WINNING_COMBINATIONS = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
)
ROWS = ((0,),) + WINNING_COMBINATIONS[0:3]
HORIZONTAL = "-----------------------"
VERTICAL = "   {}   |   {}   |   {}   "
P1 = "X"
P2 = "O"

class TicToe:
    """A Game of TicTacToe with some simple AI implemented"""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = [""] + len(VALID_RANGE) * [DEFAULT]
        self.player = 0

    def __str__(self):
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')
        s = ""
        s += "DIFFICULTY: " + self.difficulty.upper() + "\n\n"
        for i in range(0, 3):
            s += VERTICAL.format(DEFAULT, DEFAULT, DEFAULT) + "\n"
            s += VERTICAL.format(self.board[1 + i * 3], self.board[2 + i * 3], self.board[3 + i * 3]) + "\n"
            s += VERTICAL.format(DEFAULT, DEFAULT, DEFAULT) + "\n"
            s += HORIZONTAL + "\n" if i != 2 else ""
        return s

    @property
    def is_win(self):
        for combination in WINNING_COMBINATIONS:
            if self.board[combination[0]] != DEFAULT:
                if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]]:
                    return self.board[combination[0]]
        return False

    @property
    def game_over(self):
        if self.is_win:
            return True
        for element in self.board:
            if element == DEFAULT:
                return False
        return True

    # Raise exception if location is not valid
    def validate(self, location):
        if self.game_over:
            raise InputError(location, "Game is over - you cannot make any more moves!")
        elif self.board[location] != DEFAULT:
            raise InputError(location, "This field is already taken. Please choose another one.")

    # Move to location if location is valid
    def move(self, location):
        try:
            self.validate(location)
        except InputError as e:
            print(e.message)
            return False
        else:
            self.board[location] = [P1, P2][self.player]
            self.player = 1 - self.player
            return location

    # Ask player for move until integer between 1 through 9 is given
    def player_move(self):
        location = None
        while location not in range(1, 10):
            try:
                location = int(input("Please pick a move between numbers 1 through 9: "))
            except ValueError:
                print("This is not a number between 1 through 9.")
        return self.move(int(location))

    # Random computer move
    def computer_move(self):
        locations = list(filter(lambda x: x[1] == " ", enumerate(self.board)))
        choice = random.choice([location[0] for location in locations])
        self.move(choice)

    def play(self):
        # Draw random who is player 1 and player 2
        choice = random.choice([0, 1])
        computer, player = [P1, P2][choice], [P1, P2][1 - choice]
        print(self)
        # Run while game is not yet over
        while not self.game_over:
            if computer == [P1, P2][self.player]:
                self.computer_move()
                print(self)
            else:
                self.player_move()
                print(self)
                if not self.is_win:
                    print("Computer is thinking...")
                    sleep(2)
        # Determine who has won if any
        if self.is_win and player != [P1, P2][self.player]:
            print("Congratulations - you won against the computer.")
        elif self.is_win:
            print("Too bad - the computer beat you.")
        else:
            print("Game over - no one won.")


if __name__ == '__main__':
    difficulty = "easy"
    # Set difficulty either from command-line arguments or ask player
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "easy":
            difficulty = "easy"
        elif sys.argv[1].lower() == "hard":
            difficulty = "hard"
        else:
            difficulty = ""
    while difficulty.lower() != "easy" and difficulty.lower() != "hard":
        print("You can choose between difficulty level 'easy' and 'hard' for this game.")
        difficulty = input("Type either 'easy' or 'hard' and press enter: ").lower()
    # Create a game of TicTacToe and play
    tic = TicToe(difficulty)
    tic.play()
