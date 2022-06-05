class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = [1]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count.append(1)
            else:
                count[-1] += 1
        ans = 0
        for i in range(1, len(count)):
            ans += min(count[i], count[i-1])
        return ans