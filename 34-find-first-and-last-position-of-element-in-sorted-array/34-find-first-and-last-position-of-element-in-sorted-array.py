class Solution:
    def searchRange(self, nums, target):
        def findleft(nums, target):
            L, R = 0, len(nums) - 1
            left_ind = -2
            while L <= R:
                mid = (L+R) // 2
                if nums[mid] >= target:
                    R = mid - 1
                    left_ind = R
                else:
                    L = mid + 1
            return left_ind
        def findright(nums, target):
            L, R = 0, len(nums) - 1
            right_ind = -2
            while L <= R:
                mid = (L+R) // 2
                if nums[mid] <= target:
                    L = mid + 1
                    right_ind = L
                else:
                    R = mid - 1
            return right_ind
        Lind, Rind = findleft(nums, target), findright(nums, target)
        if Lind == -2 or Rind == -2: return [-1, -1]

        if Rind - Lind >1: return [Lind + 1, Rind - 1]

        return [-1, -1]

            
                 