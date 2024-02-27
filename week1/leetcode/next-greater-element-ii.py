class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        n = len(nums)
        for i in range(n*2):
            if not stack:
                stack.append([i%n,nums[i%n]])
            else:
                if stack[-1][1]< nums[i%n]:
                    while stack and stack[-1][1]< nums[i%n]:
                        a = stack.pop()
                        ans[a[0]%n]= nums[i%n]
                    stack.append([i%n,nums[i%n]])
                else:
                    stack.append([i%n,nums[i%n]])
        return ans