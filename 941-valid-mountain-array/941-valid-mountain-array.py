class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        L, R = 0, len(arr) - 1
        while L <= R and arr[L] < arr[L+1] and L < len(arr)-2:
            L += 1
        while L <= R and arr[R] < arr[R-1] and R > 1:
            R -= 1
        return L == R
            