class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        size = 1
        while n > 0:
            if n >= size:
                count += 1
            n -= size
            size += 1
        return count