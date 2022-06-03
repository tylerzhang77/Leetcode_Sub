class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                counter += 1
        return counter