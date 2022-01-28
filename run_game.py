"""
Plays a game of Wordle
"""
import argparse
from ast import arg
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

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', '--word', type=str, help='The word to guess.')
    group.add_argument('-l', '--length', type=int, help='The length of the random word to be chosen.')
    parser.add_argument('-d', '--dictionary', help='Location of local dictionary file', default='/usr/share/dict/words')
    args = parser.parse_args()

    word_length = args.length if args.length else len(args.word)
    with open(args.dictionary, 'r') as words:
        for line in words:
            if len(line) - 1 == word_length:
                WORDS.append(
                    line.strip().lower()
                )

    answer = args.word if args.word else choice(WORDS)
    score = run_game(answer)
    print(f"Guessed '{answer}' in {score} shots")
