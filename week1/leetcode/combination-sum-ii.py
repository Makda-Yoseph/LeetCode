class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [[]]
        path = []
    
        candidates.sort()
        a=0
        l = len(candidates)
        def backtrack(i,path,target,a):
            if sum(path)>=target:
                return
            if i>=len(candidates):
                return
            for j in range(i,len(candidates)):
                if candidates[j] ==a:
                    continue
                path.append(candidates[j])
                if sum(path)== target:
            
                    ans.append(path[:])
    
                backtrack(j+1,path,target,a)  
                a= path.pop()
           
            
                
        backtrack(0,[],target,a)
        return ans[1:]