from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    
    # Attributes:
        # jumper (Jumper): The game's jumper.
        # is_playing (boolean): Whether or not to keep playing.
        # puzzle (Puzzle): The game's Puzzle.
        # self.letter: Input for the guessed letter.
        # self._guess_result: set to None
        # self._words: array of word and set to random
        # self._terminal_service: helper validator for inputs
    def __init__(self):
        
        self._words = ["water", "fire", "earth", "wind"]
        self._jumper = Jumper()
        self._is_playing = True
        self._letter = ""
        self._guess_result = None
        self._puzzle = Puzzle(self._words)
        self._terminal_service = TerminalService()
        
    def start_game(self):
        # Starts the game by running the main game loop.
        while True:
            if not self._is_playing:
                self._output()
                break
            self._game()

    def _output(self):
        # prints the random word in "_" and use join function
        print("\n" + " ".join(self._puzzle._guessed_word) + "\n")

        for i in self._jumper._person_para:
            print(i)

    def _game(self):
        # prints the update of the guessed word
        self._output()
        self._letter = input("Please input the letter: ")
        self._guess_result = self._puzzle.guess(self._letter)

        if not self._guess_result:
            self._jumper.kill()
        
        self._is_playing = self._jumper.is_dead()
        self._is_playing = self._puzzle.is_done()


        
    

        

        
 