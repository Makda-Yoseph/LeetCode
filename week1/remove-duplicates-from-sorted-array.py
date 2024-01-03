class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = 0
        s=1
        while s < len(nums):
            if nums[s]!=nums[h]:
                nums[h+1],nums[s] = nums[s],nums[h+1]
                s += 1
                h +=1
            else:
                s +=1
        return h+1
