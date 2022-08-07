class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.row(board) and self.col(board) and self.square(board)
    
    def check(self, entry):
        elem = [i for i in entry if i != '.']
        return len(elem) == len(set(elem))
    
    def row(self, entry):
        for i in entry:
            if not self.check(i):
                return False
        return True
    
    def col(self, entry):
        for i in zip(*entry):
            if not self.check(i):
                return False
        return True
    
    def square(self, entry):
        for i in (0,3,6):
            for j in (0,3,6):
                board = [entry[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.check(board):
                    return False
        return True