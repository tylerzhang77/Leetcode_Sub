class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = dict()
        for char in s:
            data[char] = data.get(char , 0) + 1
        for i, c in enumerate(s):
            if data[c] == 1:
                return i
        return -1