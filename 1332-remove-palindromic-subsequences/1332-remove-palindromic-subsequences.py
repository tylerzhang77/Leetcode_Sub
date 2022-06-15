class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if s already a palindrom, 1 step
        # if s is empty, 0 step
        # otherwise, 2 step since all we have are 'a' and 'b'
        if len(s) == 0:
            return 0
        return 1 if s == s[::-1] else 2