class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [(-1,0)]
        ans = 0
        for i in range(len(arr)):
            while stack and arr[i]<= stack[-1][1]:
                a = stack.pop()[0]
                s = stack[-1][0]
                ans += (a-s)*(i-a)*arr[a]
            stack.append((i,arr[i]))
        for  i in range(1,len(stack)):
            ans += (stack[i][0]-stack[i-1][0])*abs(stack[i][0]-len(arr))*stack[i][1]
        return ans%(10**9+7)

