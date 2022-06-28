class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = Counter()
        l = r = 0
        res = 0
        typ = 0
        while r < len(fruits):
            if dic[fruits[r]] == 0:
                typ += 1
            dic[fruits[r]] += 1
            
            while typ>2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    typ -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
            r += 1
        return res