class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            res = max(res, len(list(i.split())))
        return res
            