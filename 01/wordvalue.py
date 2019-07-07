from data import DICTIONARY, LETTER_SCORES
from functools import reduce

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as dictionary:
        data = dictionary.read()
        words = data.split()
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES.get(letter.upper(), 0)
    return score


def calc_word_value_with_reduce(word):
    return reduce(
        (lambda accum, char: accum + LETTER_SCORES.get(char.upper(), 0)), list(word), 0
    )

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    highscore = 0
    for word in words:
        current_word = calc_word_value(word)
        if current_word > highscore:
            highscore, highscore_word = current_word, word
    return highscore_word


if __name__ == "__main__":
    print("hello")
