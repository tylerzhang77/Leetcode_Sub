class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        if num < 0: num += 2**32
        char = '0123456789abcdef'
        res = ''
        while num > 0:
            digit = num % 16
            num = (num - digit) // 16
            res += char[digit]
        return res[::-1]