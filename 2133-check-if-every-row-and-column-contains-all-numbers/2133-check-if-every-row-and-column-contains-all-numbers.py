class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        col = [0] * N
        for i in matrix:
            if len(set(i)) != N:
                return False
            for j in range(N):
                col[j] += i[j]
        return len(set(col)) == 1