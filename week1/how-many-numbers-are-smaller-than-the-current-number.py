class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        numss = list(nums)
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
        dictr={}
        space = []
        for k in range(len(nums)):
            if nums[k] not in dictr:
                dictr[nums[k]] = k
        for i in numss:
            space.append(dictr[i])
        return space 
        
        