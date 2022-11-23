import random

# creates class for puzzle
class Puzzle:
    # creates the random word for the player to guess using random.randint
    def __init__(self, words):
        self._word = words[random.randint(0, len(words) - 1)]
        self._guessed_word = ["_" for i in self._word]
    # the data input will replace every letter that has been guessed correct
    def guess(self, letter):
        guessed = False
        for i, data in enumerate(self._word):
            if letter == data:
                self._guessed_word[i] = letter
                guessed = True
        return guessed
    # if word has been guess it will print the words "You guess it!"
    def is_done(self):
        if self._word == "".join(self._guessed_word):
            print("You guessed it!")
            return False
        return True
    