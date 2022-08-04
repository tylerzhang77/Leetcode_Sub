class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            x = -x
            symbol = -1
        else:
            symbol = 1
        while x:
            res = res * 10 + x % 10
            x //= 10
        return 0 if res > pow(2, 31) else res*symbol