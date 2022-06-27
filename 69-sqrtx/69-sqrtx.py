class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            sqr = m ** 2
            if sqr > x:
                r = m - 1
            elif sqr < x:
                l = m + 1
            else:
                return m 
        return r