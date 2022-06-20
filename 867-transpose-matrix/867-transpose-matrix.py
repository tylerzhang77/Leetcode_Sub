class Solution:
    def transpose(self, matrix):
        M, N = len(matrix), len(matrix[0])
        res = [[0]*M for i in range(N)]
        for x,i in enumerate(matrix):
            for y,elem in enumerate(i):
                res[y][x] = elem
                
        return res