class Solution(object):
    def missingNumber(self, nums):
        
        ran = Counter(nums)
        for i in range(len(nums)+1):
            if ran[i] == 0:
                return i
        