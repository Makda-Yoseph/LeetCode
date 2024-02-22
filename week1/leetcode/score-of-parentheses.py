class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                count = 0
                while stack[-1] != '(':
                    count += int(stack[-1])
                    stack.pop()
                stack.pop()
                ans = 2*count
                if count == 0:
                    stack.append(1)
                else:
                    stack.append(ans)
                
        return sum(stack)
                

        