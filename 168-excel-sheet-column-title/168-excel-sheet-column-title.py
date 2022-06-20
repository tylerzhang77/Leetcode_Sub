class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cap = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = []
        while columnNumber > 0:
            mod, div = (columnNumber-1) % 26, (columnNumber-1) // 26
            res.append(cap[mod])
            columnNumber = div
        res.reverse()
        return ''.join(res)
          