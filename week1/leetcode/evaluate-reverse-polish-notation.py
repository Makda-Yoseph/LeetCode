class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == "+":
                    c = a+b
                elif i =='-':
                    c = b-a
                elif i=='*':
                    c = a*b
                elif i =='/':
                    c = b/a
                stack.append(c)
        return int(stack[0])
        