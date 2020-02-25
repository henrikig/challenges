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
HORIZONTAL = "-----------------------"
VERTICAL = "   {}   |   {}   |   {}   "
PLAYERS = ["X", "O"]


class TicToe:
    """A Game of TicTacToe with some simple AI implemented"""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = [''] + len(VALID_RANGE) * [DEFAULT]
        self.player = 0

    def __str__(self):
        # Clear screen
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')
        # Representation of game as string
        s = ""
        s += "DIFFICULTY: " + self.difficulty.upper() + "\n\n"
        for i in range(0, 3):
            s += VERTICAL.format(DEFAULT, DEFAULT, DEFAULT) + "\n"
            s += VERTICAL.format(self.board[1 + i * 3], self.board[2 + i * 3], self.board[3 + i * 3]) + "\n"
            s += VERTICAL.format(DEFAULT, DEFAULT, DEFAULT) + "\n"
            s += HORIZONTAL + "\n" if i != 2 else ""
        return s

    # Check if any of the combinations from the winning combinations are fulfilled
    def is_win(self, player):
        return self.evaluate(self.board, player)

    # Check if the game is either a win or the board is full
    @property
    def game_over(self):
        if self.is_win(PLAYERS[0]) or self.is_win(PLAYERS[1]):
            return True
        for element in self.board:
            if element == DEFAULT:
                return False
        return True

    # Raise exception if chosen location is not valid
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
            self.board[location] = PLAYERS[self.player]
            self.player = 1 - self.player
            return location

    # Ask player for move until integer between 1 through 9 is given
    def player_move(self):
        location = None
        while location not in VALID_RANGE:
            try:
                location = int(input("Please pick a move between numbers 1 through 9: "))
            except ValueError:
                print("This is not a number between numbers 1 through 9.")
        return self.move(int(location))

    # Choose a move strategy for the computer based on difficulty
    def computer_move(self):
        self.random_move() if self.difficulty == 'easy' else self.advanced_move()

    # Random computer move
    def random_move(self):
        locations = list(filter(lambda x: x[1] == " ", enumerate(self.board)))
        choice = random.choice([location[0] for location in locations])
        self.move(choice)

    def advanced_move(self):
        pass

    @staticmethod
    def evaluate(position, player):
        for combination in WINNING_COMBINATIONS:
            if position[combination[0]] != DEFAULT:
                if position[combination[0]] == position[combination[1]] == position[combination[2]]:
                    return 10 if position[combination[0]] == player else -10
        return 0

    def play(self):
        # Draw random who is player 1 and player 2
        choice = random.choice([0, 1])
        computer, player = PLAYERS[choice], PLAYERS[1 - choice]
        print(self)
        # Run while game is not yet over
        while not self.game_over:
            if computer == PLAYERS[self.player]:
                self.computer_move()
                print(self)
            else:
                if self.player_move():
                    print(self)
                    if not self.game_over:
                        print("Computer is thinking...")
                        sleep(1.5)
        # Determine who has won if any
        if self.is_win(player) > 0:
            print("Congratulations - you won against the computer.")
        elif self.is_win(computer) > 0:
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
