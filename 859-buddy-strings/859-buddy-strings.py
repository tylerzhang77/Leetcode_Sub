class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        d1, d2 = -1, -1
        alet = set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                if d1 == -1:
                    d1 = i
                elif d2 == -1:
                    d2 = i
                else:
                    return False
            alet.add(s[i])
        if d1 != -1 and d2 != -1:
            return s[d1] == goal[d2] and s[d2] == goal[d1]
        if d1 != -1:
            return False
        return len(alet) < len(s)
        