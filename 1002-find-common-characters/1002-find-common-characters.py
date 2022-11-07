class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = [0] * 26
        for i in words[0]:
            temp[ord(i)-ord('a')] += 1
        for i in words[1:]:
            ht = [0] * 26
            for j in i:
                ht[ord(j) - ord('a')] += 1
            for k in range(26):
                temp[k] = min(temp[k], ht[k])
        res = []
        for i in range(26):
            while temp[i] != 0:
                res.append(chr(i+ord('a')))
                temp[i] -= 1
        return res