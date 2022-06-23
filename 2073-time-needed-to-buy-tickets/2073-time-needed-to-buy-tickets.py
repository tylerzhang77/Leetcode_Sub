class Solution:
    def timeRequiredToBuy(self, t, k):
        return sum([min(t[i], t[k] if i<=k else t[k]-1) for i in range(len(t))])
        