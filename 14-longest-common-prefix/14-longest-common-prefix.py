class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key = len)
        for i, letter in enumerate(shortest):
            for word in strs:
                if word[i] != letter:
                    return shortest[:i]
        return shortest