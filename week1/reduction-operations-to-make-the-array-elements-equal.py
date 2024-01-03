class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        x =sorted(nums)
        dictx = Counter(x)
        s = sorted(set(x))
        i = 0
        sm = 0
        for n in s:
            sm += i*dictx[n]
            i+=1
        return sm

        
