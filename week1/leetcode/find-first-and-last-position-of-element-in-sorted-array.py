class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [len(nums),-1]
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if  nums[mid]== target:
                if mid<ans[0]:
                    ans[0]= mid
                high = mid - 1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid + 1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if  nums[mid]== target:
                if mid>ans[1]:
                    ans[1]= mid
                low = mid + 1
            elif nums[mid]>target:
                high = mid -1
            else:
                low  = mid+1
        if ans==[len(nums),-1]:
            return [-1,-1]
        else:
            return ans
            
        