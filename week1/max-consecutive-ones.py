class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        ones = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                count +=1
                ones = max(count,ones)
            else:
                ones = max(count,ones)
                count = 0
                continue
        return ones

            
        