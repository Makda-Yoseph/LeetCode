class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        count =0
        while l<=r:
            if nums[l] != val:
                l+=1
                count +=1
            elif nums[l] == val and nums[r] == val:
                r -=1
            elif nums[l] == val and nums[r] != val:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                count +=1
        return count
                
        