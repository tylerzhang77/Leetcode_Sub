class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp 
        return num