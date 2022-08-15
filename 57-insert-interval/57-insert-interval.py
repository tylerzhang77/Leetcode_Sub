class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        intervals.append(newInterval)
        res = []
        for ran in sorted(intervals, key = lambda x: x[0]):
            if res and res[-1][1] >= ran[0]:
                res[-1][1] = max(res[-1][1], ran[1])
            else:
                res.append(ran)
        return res