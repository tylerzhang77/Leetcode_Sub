class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split(" ")
        lis = [c[::-1] for c in lis]
            
        return " ".join(lis)