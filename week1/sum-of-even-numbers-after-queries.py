class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        occurnums = dict((i,n) for i,n in enumerate(nums))
        result = []
        s = 0
        for i in nums:
            if i %2 ==0:
                s +=  i
        for v,i in queries:
            if occurnums[i] % 2 == 0:
                s  = s - occurnums[i]
            occurnums[i] = occurnums[i] + v
            if occurnums[i] % 2 == 0:
                s = s + occurnums[i]
            result.append(s)
        return result


            
        