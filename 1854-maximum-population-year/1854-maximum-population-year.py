class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs = sorted(logs, key = lambda x: x[0])
        resdic = {}
        for i in range(len(logs)):
            a, b = logs[i][0], logs[i][1]
            counter = 1
            for j in range(i):
                c, d = logs[j][0], logs[j][1]
                if d > a:
                    counter += 1
            resdic[a] = counter
        return max(resdic, key = resdic.get)
            
                