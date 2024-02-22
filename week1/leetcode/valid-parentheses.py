class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)==1:
        #     return False
        stack = []
        match = { '(': ')', '{': '}', '[' : ']'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if stack==[]:
                    return False
                else:
                    p = stack.pop()
                    if match[p]!= c :
                        return False
        if stack==[]:
            return True
        else:
            return False