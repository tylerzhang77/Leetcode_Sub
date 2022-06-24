class Solution:
    def checkString(self, s: str) -> bool:
        ind = False
        res = True
        for i in s:
            if i == 'b':
                ind = True
            else:
                if ind:
                    res = False
        return res
                