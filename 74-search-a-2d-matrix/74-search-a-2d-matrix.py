class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        up, down = 0, row*col - 1
        while up <= down:
            mid = (down - up) // 2 + up
            val = matrix[mid // col][mid % col]
            
            if val < target:
                up = mid + 1
            elif val > target:
                down = mid - 1
            else:
                return True
        return False