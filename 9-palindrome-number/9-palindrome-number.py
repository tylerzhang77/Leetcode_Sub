class Solution:
    def isPalindrome(self, x: int) -> bool:
        pos = []
        neg = []
        for letter in str(x):
            pos.append(letter)
            neg.insert(0,letter)
        
        for i in range(len(pos)):
            if pos[i] != neg[i]:
                return False
        return True
            
            