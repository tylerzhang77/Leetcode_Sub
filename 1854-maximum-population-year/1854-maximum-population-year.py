class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        log = []
        for live, death in logs:
            log.append((live, 1))
            log.append((death, -1))
        log.sort()
        currpop = maxpop = maxyear = 0
        for year, ind in log:
            currpop += ind
            if currpop > maxpop:
                maxpop = currpop
                maxyear = year
        return maxyear
            
                