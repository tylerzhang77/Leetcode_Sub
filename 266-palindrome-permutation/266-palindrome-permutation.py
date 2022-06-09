class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1 
        counter = 0
        for val in dic.values():
            if val % 2 == 1:
                counter += 1
        return counter < 2
            