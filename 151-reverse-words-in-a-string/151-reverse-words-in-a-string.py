class Solution:
    def reverseWords(self, s: str) -> str:
        st = self.trim_space(s)
        self.rev_string(st, 0, len(st)-1)
        self.rev_word(st)
        return ''.join(st)
    def trim_space(self, s):
        n = len(s)
        l, r = 0, n-1
        while l<=r and s[l] == ' ':
            l += 1
        while l<=r and s[r] == ' ':
            r -= 1
        temp = []
        while l <= r:
            if s[l]!=' ':
                temp.append(s[l])
            elif temp[-1]!=' ':
                temp.append(s[l])
            l+=1
        return temp
            
    def rev_string(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return None
            
    def rev_word(self, s):
        start = 0
        end = 0
        n = len(s)
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            self.rev_string(s, start, end-1)
            start = end + 1
            end += 1
        return None 
    
        