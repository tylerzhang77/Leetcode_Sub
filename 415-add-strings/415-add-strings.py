class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = 0
        len1 = len(num1)
        len2 = len(num2)
        for i in range(len1):
            ans += int(num1[i])*10**(len1-1-i)
        for i in range(len2):
            ans += int(num2[i])*10**(len2-1-i)
        return str(ans)