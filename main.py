"""
In the real game, tiles are taken at random from a 'bag'
 containing a fixed number of each tile. Assign seven 
 tiles to a rack using a bag containing the above 
 distribution.
"""
import random

letter_scores = {
  "E": 1, "A": 1, "I": 1, "O": 1,
  "N": 1, "R": 1, "T": 1, "L": 1,
  "S": 1, "U": 1, "D": 2, "G": 2,
  "B": 3, "C": 3, "M": 3, "P": 3,
  "F": 4, "H": 4, "V": 4, "W": 4,
  "Y": 4, "K": 5, "J": 8, "X": 8,
  "Q": 10, "Z": 10
}

def get_score(word: str) -> int:
    """Takes word and returns scrabble score"""
    if not isinstance(word, str):
        raise TypeError("Not a word.")
    score = 0
    word = word.upper()
    for i in range(len(word)):
        score += letter_scores[word[i]] 

    return score


def get_letters() -> list:
    """Picks 7 letters from alphabet"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hand = []
    for i in range(7):
        num = random.randint(0, 25)
        hand.append(alphabet[num])

    return hand
    


def get_letters_from_bag() -> list:
    """Picks 7 letters from bag of letters"""
    bag = "eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooonnnnnnrrrrrrttttttllllssssuuuuddddgggbbccmmppffhhvvwwyykjxqz"

    hand = []
    for i in range(7):
        num = random.randint(0, len(bag) - 1)
        hand.append(bag[num])
        bag.replace(bag[num], "", 1)

    return hand

