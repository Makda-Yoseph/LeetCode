class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack=[]
        num = []
        stack2 =[]
        i=0
        while i < len(s):
            if not stack and not (s[i]>='0' and s[i]<='9'):
                stack.append(s[i])
                i+=1
            elif s[i]>='0' and s[i]<='9' : 
                while  s[i]>='0' and s[i]<='9' :
                    num.append(s[i])
                    i+=1
                n = int(''.join(num))
                num = []
                stack.append(n)
                print(stack)
            elif s[i]==']':
                while stack[-1]!='[':
                    stack2.append(stack.pop())
                stack.pop()
                n = int(stack.pop())
                stack2.reverse()
                a = ''.join(stack2)
                ans = a*n
                stack.append(ans)
                stack2=[]
                i+=1
            else:
                stack.append(s[i])
                i+=1
        return ''.join(stack)

            
        