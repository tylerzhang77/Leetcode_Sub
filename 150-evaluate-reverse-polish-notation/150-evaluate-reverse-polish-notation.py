class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                temp.append(i)
            else:
                fig1, fig2 = temp.pop(), temp.pop()
                temp.append(int(eval(f'{fig2}{i}{fig1}')))
        return int(temp[-1])
    