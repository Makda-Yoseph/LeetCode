class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        nums = [i for  i in range(1,n+1)]
        def backtrack(i,comb):
            if len(comb)==k:
                ans.append(comb[:])
                return
            if i>=n:
                return
            backtrack(i+1,comb)
            comb.append(nums[i])
            backtrack(i+1,comb)
            comb.pop()
        backtrack(0,comb)
        return ans