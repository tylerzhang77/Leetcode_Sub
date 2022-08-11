class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for char in strs:
            key = tuple(sorted(char))
            res[key] = res.get(key, []) + [char]
        return res.values()