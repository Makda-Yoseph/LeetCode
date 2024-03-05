class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone= {
                2:['a','b','c'],
                3:['d','e','f'],4:['g','h','i'],
                5:['j','k','l'],
                6:['m','n','o'],
                7:['p','q','r','s'],
                8:['t','u','v'],
                9:['w','x','y','z']}
        ans = [[]]
        path = []

        def backtrack(p,path):
            if len(path)==len(digits):
                ans.append(''.join(path[:]))
                return
            if p>=len(digits):
                return
            for i in range(len(phone[int(digits[p])])):
                path.append(phone[int(digits[p])][i])
                backtrack(p+1,path)
                path.pop()
        if digits =="":
            return []
        backtrack(0,[])
        return ans[1:]
