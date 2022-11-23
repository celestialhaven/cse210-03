# creates the jumper class
class Jumper:
    # print the person with parachute
    def __init__(self):
        self._person_para = ["   ___", " /     \\", "  -----", " \\     /", "  \\   /", "    O", "   /|\\", "   / \\\n", "^^^^^^^^^^^^\n"]
    # removes every list in array once letter is not is random word
    def kill(self):
        self._person_para.pop(0)
    # once the parachute is gone the head or the person will change to "x" and prints game over
    def is_dead(self):
        if len(self._person_para) == 4:
            self._person_para[0] = "    x"
            print("Game over!")
            return False
        return True