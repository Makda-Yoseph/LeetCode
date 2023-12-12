class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        result = []
        for i, n in enumerate(nums):
            c = target - n
            if c in numdict:
                result.append(i)
                result.append(numdict[c])
            numdict[n] = i
        
        return sorted(result)