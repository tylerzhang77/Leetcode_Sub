class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in dic:
                stack.append(char)
            elif len(stack) == 0 or dic[stack.pop()] != char:
                return False
        return len(stack) == 0