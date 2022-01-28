"""
Plays a game of Wordle
"""
from random import choice
import sys

from pywordle.wordle import GreyLetter, OrangeLetter, Win, Wordle

WORDS = list()


def random_word(game: Wordle):
    while True:
        word = choice(WORDS)
        if any(i in game.greys for i in word):
            continue
        return word


def run_game(answer):
    W = Wordle(answer)
    score = 0
    while True:
        word = random_word(W)
        try:
            W.guess(word)
            score += 1
        except (GreyLetter, OrangeLetter):
            continue
        except Win:
            return score


if __name__ == "__main__":

    with open('/usr/share/dict/words', 'r') as words:
        for line in words:
            if len(line) == int(sys.argv[1]):
                WORDS.append(
                    line.strip().lower()
                )

    answer = choice(WORDS)
    score = run_game(answer)
    print(f"Guessed '{answer}' in {score} shots")
