class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = 0
        indx = 0
        h,l = len(nums)-1,0
        while h>=l:
            mid = (h+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                h = mid -1
            else:
                l= mid +1
        return l