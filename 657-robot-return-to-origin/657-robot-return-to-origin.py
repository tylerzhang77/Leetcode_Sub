class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h, v = 0, 0
        for i in moves:
            if i == 'U':
                v += 1
            elif i == 'D':
                v -= 1
            elif i == 'L':
                h -= 1
            elif i == 'R':
                h += 1
        return h==0 and v==0