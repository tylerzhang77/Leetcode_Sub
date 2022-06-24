class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dac(st):
            if len(st) < 2:
                return ""
            bad = []
            for i, ch in enumerate(st):
                if ch.lower() and (ch.upper() not in st):
                    bad.append(i)
                if ch.upper() and (ch.lower() not in st):
                    bad.append(i)
            if not bad:
                return st
            else:
                mid = len(bad) // 2
                return max(dac(st[:bad[mid]]), dac(st[bad[mid]+1:]) , key = len)
        return dac(s)