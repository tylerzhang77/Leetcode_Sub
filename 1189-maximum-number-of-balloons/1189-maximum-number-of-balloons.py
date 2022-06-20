class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = set('balon')
        d = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in s:
                d[i] = d.get(i) + 1
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2
        return min(d.values())