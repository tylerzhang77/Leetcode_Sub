class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            L, R = i + 1, n-1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s > 0:
                    R -= 1
                elif s < 0:
                    L += 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    while L != R and nums[L] == nums[L+1]:
                        L += 1
                    while L != R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return ans