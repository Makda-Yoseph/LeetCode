class Solution:
    def simplifyPath(self, path: str) -> str:
        p= path.split('/')
        stack =[]
        for c in p:
            if c!='' :
                if c=='..':
                    if stack:
                        stack.pop()
                elif c != '.' :
                    stack.append(c)
        
        return '/'+('/').join(stack)

