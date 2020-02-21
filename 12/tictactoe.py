from os import system, name
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


class TicToe:
    """A Game of TicTacToe with some simple AI implemented"""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = [""] + len(VALID_RANGE) * [DEFAULT]

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

    def is_win(self):
        for combination in WINNING_COMBINATIONS:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]]:
                return True
        return False

    def game_over(self):
        if self.is_win:
            return True
        for element in self.board:
            if element == DEFAULT:
                return False
        return True

    #def new_move(self, place):



if __name__ == '__main__':
    difficulty = ""
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
    tic = TicToe(difficulty)
    print(tic)
    # try:
    #     raise InputError(6, "Value not allowed")
    # except InputError as e:
    #     print(e.message)
