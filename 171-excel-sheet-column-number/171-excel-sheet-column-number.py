class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char, i in zip(columnTitle, range(len(columnTitle),0, -1)):
            res += 26 ** (i-1)*(ord(char)-ord('A')+1)
        return res
    
 