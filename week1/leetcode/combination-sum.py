class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [[]]
        path = []
        candidates.sort()
        l = len(candidates)
        def backtrack(i,path,target):
            # if len(path)>l:
            #     i+=1
            #     return
            if sum(path)>target:
                i+1
                return
            for i in range(i,len(candidates)):
                path.append(candidates[i])
                
                if sum(path)== target:
                    ans.append(path[:])
                backtrack(i,path,target)
                path.pop()
                
        backtrack(0,[],target)
        return ans[1:]