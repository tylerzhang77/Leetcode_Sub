class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cumsum = sum(nums[:k])
        maxsum = cumsum
        for i in range(len(nums)-k):
            cumsum = cumsum - nums[i] + nums[i+k]
            maxsum = max(cumsum, maxsum)
        return maxsum / k