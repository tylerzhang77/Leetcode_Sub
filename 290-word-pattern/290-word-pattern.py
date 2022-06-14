class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        dic = {}
        if len(set(pattern)) != len(set(word)) or len(pattern) != len(word):
            return False
        for i, c in enumerate(pattern):
            if c in dic:
                if dic[c] != word[i]:
                    return False
            else:
                dic[c] = word[i]
        return True