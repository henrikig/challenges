from string import ascii_lowercase
import sys
from os import system, name

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS) - 1
PLACEHOLDER = '_'


class Hangman:
    def __init__(self, word=None):
        if word is None:
            word = get_word()
        self.word = word
        self.secret_word = list(word.lower())
        self.allowed_characters = ASCII
        self.guessed_letters = []
        self.allowed_guesses = ALLOWED_GUESSES
        self.graphics_counter = 0
        self.won = False
        self.game_over = False

    @property
    def guessed_word(self):
        return ["_" if letter not in self.guessed_letters and letter in self.allowed_characters
                else letter for letter in self.secret_word]

    @property
    def wrong_letters(self):
        return [letter for letter in self.guessed_letters
                if letter not in self.secret_word]

    def letter_input(self, letter):
        status = ""
        letter = letter.lower()
        if letter in self.guessed_letters:
            status = "This letter is already guessed. Please try another letter: "
        elif letter not in self.allowed_characters:
            status = "This is not a valid letter. Please try again: "
        else:
            self.guessed_letters.append(letter)
            if letter in self.secret_word:
                if self.guessed_word == self.secret_word:
                    self.won = True
                else:
                    status = "Correct. Please guess another letter: "
            else:
                if len(self.wrong_letters) == self.allowed_guesses:
                    self.game_over = True
                else:
                    status = "Wrong. Please guess another letter: "
                self.graphics_counter += 1
        return status

    def play(self):
        status = "Please guess a letter: "
        clear()
        print("Welcome to this game of Hangman.\n")
        while not (self.won or self.game_over):
            print(HANG_GRAPHICS[self.graphics_counter])
            letter = self.prompt_input(status)
            clear()
            status = self.letter_input(letter)
        print(HANG_GRAPHICS[self.graphics_counter])
        if self.won:
            print("Congratulations - you won!")
        else:
            print("Game over - you lost!")
        print("The word was '" + self.word + "'")

    def prompt_input(self, message="Please guess a letter: "):
        print("Wrong guessed: ", ", ".join(self.wrong_letters)) if len(self.wrong_letters) > 0 else print("")
        print(" ".join(self.guessed_word))
        letter = input(message)
        return letter


def clear():
    if name=="nt":
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        word = " ".join(sys.argv[1:])
    else:
        word = get_word()

    # init / call program
    game = Hangman(word)
    game.play()
