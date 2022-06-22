class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        counter = 0
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] != i:
                    stack.pop()
                else:
                    stack.append(i)
            if not stack:
                counter += 1
        return counter