class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n):
            for j in range(i+1,n):
                s = math.sqrt(i**2 + j**2)
                if s % 1 == 0 and s <= n:
                    count += 2
        return count