class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        counter = 0
        for i in range(1, max(s)):
            if i not in s:
                counter += 1
                if counter == k:
                    return i
        return max(s) + k - counter
                