class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if len(set(nums) ) and nums[0] == 1:
        #     return len(nums)-1
        # elif len(set(nums) ) and nums[0] == 0:
        #     return 0
        # else:
        ma = 0
        l= 0
        ct = 0
        for r in range(len(nums)):
            ct +=1 if nums[r] == 0 else 0
            while ct >1:
                if nums[l] == 0:
                    ct -=1
                l+=1
            ma = max(ma,r-l)
        return ma
