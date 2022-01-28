"""
The class which holds a Wordle game along with the state of the plays.
"""

class GreyLetter(Exception):
    pass


class OrangeLetter(Exception):
    pass


class Win(Exception):
    pass


def filter_letter(method):
    """
    Decorator to stop bad guesses being allowed.
    Stops grey letters being used and orange letters
    being used in the wrong place.
    """
    def inner(ref, position, letter):
        if letter in ref.greys:
            raise GreyLetter("Bad letter guessed")
        if letter in ref.oranges[position]:
            raise OrangeLetter("Orange letter guessed")
        return method(ref, position, letter)

    return inner


class Wordle:
    def __init__(self, answer: str):
        self.answer = answer
        self.oranges = [set() for _ in answer]
        self.greens = [None for _ in answer]
        self.greys = set()


    def guess(self, word: str):
        if word == self.answer:
            raise Win("Wordle win!")
        if len(word) != len(self.answer):
            raise Exception('Inputted word is too long.')

        for position, letter in enumerate(word):
            self.check_letter(position, letter)


    @filter_letter
    def check_letter(self, position: int, letter: str):
        if letter not in self.answer:  # grey
            self.greys.add(letter)
        elif letter == self.answer[position]:  # green
            self.greens[position] = letter
        else:  # orange
            self.oranges[position].add(letter)
