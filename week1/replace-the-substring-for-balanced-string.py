class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s)/4
        def check(count:dict,target:int )->bool:
            for v in count.values():
                if v >target:
                    return False  
            return True  
        count = {'Q':0, 'W':0, 'E':0,'R':0}
        for letter in s:
            count[letter] +=1
        if check(count,target):
            return 0
        mi = float('inf')
        l= 0
        for r in range(len(s)):
            count[s[r]] -=1
            if  check(count,target):
                mi = min(mi,r-l+1)
                while check(count,target) and l<r:
                    count[ s[l]]  +=1
                    mi = min(mi,r-l+1)
                    l +=1
              
        return mi

        





        