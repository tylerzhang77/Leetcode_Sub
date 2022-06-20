class Solution:
    def findComplement(self, num: int) -> int:
        tar = bin(num).replace('0b','')
        new = ['0' if i == '1' else '1' for i in tar]
        return int(''.join(new),2)
     