class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n+1):
            ans[i] = bin(i).replace('0b', '').count('1')
        return ans
            