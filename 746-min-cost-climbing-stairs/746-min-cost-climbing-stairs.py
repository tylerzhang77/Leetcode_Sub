class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        res = [0] * len(cost)
        res[0], res[1] = cost[0], cost[1]
        for i in range(2,len(cost)):
            res[i] = cost[i] + min(res[i-1], res[i-2])
        return min(res[-1], res[-2])
        
        