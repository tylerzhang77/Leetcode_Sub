class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}',  '[':']'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif len(stack) == 0 or i != dic[stack.pop()]:
                return False
        return len(stack) == 0