

from copy import copy, deepcopy
from pprint import pprint
class Boggle:
    maxCols=3
    maxRows=3
    dictionary = {"GEEKS":1,
                  "FOR":1,
                  "QUIZ":1,
                  "OZ": 1,
                  "SEE": 1,
                  "GO" : 1 };

    gameBoard = [['G', 'O', 'Z'],
                 ['U', 'E', 'K'],
                 ['Q', 'S', 'E']]

    direction={
        'right': [ 1, 0],
        'left':  [-1, 0],
        'up':    [ 0,-1],
        'down':  [ 0, 1],
        'nw':    [ 1, 1],
        'sw':    [-1,-1],
        'ne':    [ 1,-1],
        'se':    [-1, 1]
    }

    def copyBoard(self, board):
        return deepcopy(board)

    def printBoard(self, board):
        for i in range(self.maxCols):
            for j in range(self.maxRows):
                print(board[i][j], end=" " )
            print()

    def inBound(self, x, y):
        if x >= 0 and x < self.maxCols and y >=0 and y < self.maxRows:
            return True
        else:
            return False

    def findWordsHelper(self, board, i, j, string):
        if string in self.dictionary:
            self.wordsFound[string] = 1

        newboard = self.copyBoard(board)
        newboard[i][j]='*'
        for dir in self.direction:
            delta = self.direction[dir]
            x = i + delta[0]
            y = j + delta[1]

            if self.inBound(x, y) and newboard[x][y] != '*':
                # if string in {'G':1, 'GE':1, 'GEE':1, 'GEEK':1, 'GEEKS':1}:
                #     print(f"str={string}")
                #     self.printBoard(newboard)
                #     print()
                self.findWordsHelper(newboard, x, y, string + board[x][y])


    def findWords(self):
        self.wordsFound={}
        for i in range(0, self.maxCols):
            for j in range(0, self.maxRows):
                board=self.copyBoard(self.gameBoard)
                self.findWordsHelper(board, i, j, '')

        pprint(self.wordsFound)


boggle = Boggle()
#boggle.printBoard(boggle.gameBoard)
boggle.findWords()