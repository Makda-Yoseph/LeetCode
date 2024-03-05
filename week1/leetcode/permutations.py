class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # s= set()
        ans = []
        path = []
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                # s.add(i)
                backtrack(path)
                path.pop()
                # s.remove(i)
                
        backtrack([])
        return ans

