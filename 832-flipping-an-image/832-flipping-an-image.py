class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[0 if num ==1 else 1 for num in x][::-1] for x in image]
            