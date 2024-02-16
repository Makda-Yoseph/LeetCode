class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        pre = 0
        for i in range(len(nums)):
            if pre < 0:
                pre = 0
            pre +=nums[i]
            maxi = max(pre,maxi)
        return maxi