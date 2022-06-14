class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lis = [0] * (n+1)
        for a, b in trust:
            lis[a] -= 1
            lis[b] += 1
        for i in range(1,n+1):
            if lis[i] == (n-1):
                return i
        return -1