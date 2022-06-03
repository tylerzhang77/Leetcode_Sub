class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        tg = []
        res = []
        for i in range(len(s)):
            if s[i] == c:
                tg.append(i)
        for i in range(len(s)):
            temp = [abs(i-j) for j in tg]
            res.append(min(temp))
        return res