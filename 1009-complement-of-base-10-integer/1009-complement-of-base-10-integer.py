class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = str(bin(n)).replace('0b', '')
        return int("".join("0" if c == '1' else "1" for c in s),2)