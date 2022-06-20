class Solution:
    def maxDepth(self, s: str) -> int:
        maxlen = 0
        temp = []
        for c in s:
            if c == '(':
                temp.append(c)
            elif c == ')':
                temp.pop()
            maxlen = max(maxlen, len(temp))
        return maxlen