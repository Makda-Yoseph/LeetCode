class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        ans = float('inf')
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid]>nums[r]:
                l = mid +1
                ans = min(ans,nums[r])
            else:
                r = mid-1
                ans = min(ans,nums[mid])
            if l == r:
                ans = min(ans,nums[l])
                ans = min(ans,nums[(l+1)%len(nums)])
                ans = min(ans,nums[(l-1)%len(nums)])
            ans = min(ans,nums[mid])
        
        return ans