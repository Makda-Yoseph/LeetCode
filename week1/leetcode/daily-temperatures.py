class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # idx = dict((i,n)for i,n in enumerate(temperatures) )
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append([i,temperatures[i]])
            else:
                if stack[-1][1]< temperatures[i]:
                    while stack and stack[-1][1]< temperatures[i]:
                        a = stack.pop()
                        ans[a[0]]= i-a[0]
                    stack.append([i,temperatures[i]])
                else:
                    stack.append([i,temperatures[i]])
        return ans