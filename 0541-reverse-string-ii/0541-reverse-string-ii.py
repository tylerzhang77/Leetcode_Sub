class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p1 = 0
        while p1 < len(s):
            p2 = p1+k
            s = s[:p1] + s[p1:p2][::-1] + s[p2:]
            p1 = p2+k
        return s