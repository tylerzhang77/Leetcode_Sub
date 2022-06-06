class Solution:
    def isHappy(self, n: int) -> bool:
        collect = set()
        while n not in collect:
            collect.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return n == 1