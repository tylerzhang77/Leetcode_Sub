class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, width, maxArea = 0, len(height)-1, len(height)-1, 0
        for i in range(width, 0, -1):
            if height[left]<height[right]:
                maxArea = max(maxArea, height[left]*i)
                left += 1
            else:
                maxArea = max(maxArea, height[right]*i)
                right -= 1
        return maxArea
    
    
            