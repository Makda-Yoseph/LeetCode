class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rangeNums = len(nums)+1
        for i in range(rangeNums):
            if i not in nums:
                return i
            
