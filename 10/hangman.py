from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman:
    def __init__(self, word=None):
        if word is None:
            word = get_word()
        self.word = list(word.lower())
        self.allowed_guesses = ALLOWED_GUESSES
        self.guessed = []
        self.correct_letters = []
        self.wrong_letters = []
        self.won = False

    def letter_input(self, letter):
        letter = letter.lower()
        if letter not in ASCII:
            prompt_input("This is not a valid letter")
        elif letter in self.guessed:
            prompt_input("This letter is already guessed")
        else:
            self.guessed.append(letter)
            if letter in self.word:
                self.correct_letters.append(letter)
            else:
                self.wrong_letters.append(letter)

    def play(self):
        if len(self.wrong_letters) <= self.allowed_guesses and not self.won:


    def prompt_input(self, message):
        print(message)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)
    print(ASCII)

    # init / call program
