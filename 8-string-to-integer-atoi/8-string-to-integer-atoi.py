class Solution:
    def myAtoi(self, s: str) -> int:

        s = list(s.strip())
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ['-','+'] : del s[0] 
        i = 0
        res = 0
        while i<len(s) and s[i].isdigit():
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        res = res*sign
        if res<-2**31: return -2**31
        elif res>2**31-1: return 2**31-1
        else: return res
        
