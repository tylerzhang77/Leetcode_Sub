class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]):
        row = [0] * m 
        col = [0] * n
        count = 0
        for a,b in indices:
            row[a] += 1
            col[b] += 1
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 != 0:
                    count += 1
        return count