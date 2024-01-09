class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,s = 0,0
        minsize = len(nums)+1
        for left in range(len(nums)):
            s += nums[left]
            while s >= target:
                minsize = min(minsize,left-l+1)
                s -=nums[l]
                l+=1
        if minsize == len(nums)+1:
            return 0
        else:
            return minsize
            
        