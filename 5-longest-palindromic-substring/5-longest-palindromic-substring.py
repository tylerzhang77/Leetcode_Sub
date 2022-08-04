class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        max_len = ''
        for i in range(len(s)):
            max_len = max(self.helper(s,i,i), self.helper(s,i,(i+1)), max_len, key = len)
        return max_len
        
    def helper(self, s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]