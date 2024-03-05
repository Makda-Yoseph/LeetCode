class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        path = []
        l = 2**len(nums)
        
        def backtrack(indx,path):
            if len(ans)== l:
                return
        
            for i in range(indx,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                for s in ans:
                    if Counter(s)==Counter(path):
                        break
                else:
                    ans.append(path[:])
                path.pop()
                
        backtrack(0,[])
        
        return ans
