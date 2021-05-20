''' 
    This is a library that allows you to generate and play a type of puzzle called a ``nonogram''. 
    A nonogram is presented as a grid where each square is either filled in or not. The object is 
    to figure out exactly which of the squares are supposed to be filled in. You are given two 
    lists as clues. The first list tells of you the the structure of the filled in spaces in each 
    of the rows. For example,
            the row: "■■■xx■xxx■" (where x is empty and ■ is filled) is given the clue (3,1,1).
    Similarly, the second list tells you the same structuce of the columns. Now, you may even get 
    the list in a state where some of the squares are alreadly filled in to makle this easier or 
    remove ambiguity in solutions. 
'''
from typing import Tuple
import numpy as np

# First is a class to represent a given game as just do the book keeping (not generate the game itself)
class Nonogram():
    def __init__(self,size: int, key: np.ndarray, game=None):
        self.size = size
        if game == None:
            # we are going to represent unrevealed spots as '0' and '1' for revealed but not filled and '2' for filled in.
            self.game = np.zeros(shape = (size, size), dtype = np.int8)
        else:
            self.game = game
        self.key = key
    def __repr__(self) -> str:
        def symbols(i:np.int8): 
            ''' Here is a Python 3.10 version of this code (which is currently unreleased)
            match i:
                case 0:
                    reutrn '?'
                case 1:
                    return '\u2610'
                case 2:
                    return '\u25A0'
            '''
            return {0:'?', 1:'\u2610', 2:'\u25A0'}[i]
        return str(np.matrix([[symbols(i) for i in x] for x in self.game]))
    # changes the game to reveal a particular entry
    # returns True if the square was filled in
    # returns False if the square was empty
    def reveal(self, row, col) -> bool:
        self.game[row,col] = self.key[row,col]
        return self.key[row,col] == 2
    # give a string representation of the key
    def key_repr(self):
        def symbols(i:np.int8): 
            ''' Here is a Python 3.10 version of this code (which is currently unreleased)
            match i:
                case 0:
                    reutrn '?'
                case 1:
                    return '\u2610'
                case 2:
                    return '\u25A0'
            '''
            return {0:'?', 1:'\u2610', 2:'\u25A0'}[i]
        return str(np.matrix([[symbols(i) for i in x] for x in self.key]))
    # checks if this game is solved
    def solved(self) -> bool:
        # np.any(expr) checks if all of the elements of the array evaluate to True
        return not np.any(self.game == 0)

# generate the clues of a given board
def clues(size: int, key: np.ndarray) -> Tuple:
    rows, cols = np.empty(size, list),np.empty(size, list)
    for i in range(size):
        rows[i] = find_pattern(key[i,:])
    for i in range(size):
        cols[i] = find_pattern(key[:,i])
    return (rows, cols)

# takes a line (row or col in our context) and returns an array of the pattern of filled in spaces
def find_pattern(line: np.array) -> list:
    flag = False # keeps track of whether we are going through a chain of filled in spaces
    count = 0
    res = []
    for space in line:
        if space == 2:
            count += 1
            if not flag:
                flag = True
        else:
            if flag:
                res.append(str(count))
                count = 0
                flag = False
    if flag:
        res.append(str(count))
    return res

