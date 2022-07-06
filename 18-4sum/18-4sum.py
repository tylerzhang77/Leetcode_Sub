class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for k in range(i+1, n):
                if k > i + 1 and nums[k] == nums[k-1]:
                    continue
                L, R = k + 1, n - 1
                while L < R:
                    s = nums[L] + nums[R] + nums[i] + nums[k]
                    if s > target:
                        R -= 1
                    elif s < target:
                        L += 1
                    else:
                        ans.append([nums[i], nums[k], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                        L += 1
                        R -= 1
        return ans
