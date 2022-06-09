class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            count = 0
            for char in word:
                if word.count(char) > chars.count(char):
                    count += 1
            if count == 0:
                res += len(word)
        return res