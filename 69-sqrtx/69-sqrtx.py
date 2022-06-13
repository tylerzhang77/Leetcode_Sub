class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1, x//2+1):
            if i * i <= x and (i+1) * (i+1) > x:
                return i