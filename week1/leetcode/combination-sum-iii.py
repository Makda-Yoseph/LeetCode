class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = [[]]
        path = []
        target = n
        a=0
        def backtrack(i,path,target,a):
            if sum(path)>=target:
                return
            if len(path)> k:
                return
            if i>=10:
                return
            for j in range(i,10):
                if j ==a:
                    continue
                path.append(j)
                if sum(path)== target and len(path)==k:
            
                    ans.append(path[:])
    
                backtrack(j+1,path,target,a)  
                a= path.pop()
           
            
                
        backtrack(0,[],target,a)
        return ans[1:]