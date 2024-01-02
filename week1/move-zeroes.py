class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = 0
        l = 0
        while l< len(nums):
            if nums[l] != 0:
                nums[ct],nums[l] = nums[l],nums[ct]
                ct +=1
            l+=1
            
        