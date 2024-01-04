class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l=0
        while l < len(nums):
            x = nums[l]
            left,right = l+1,len(nums)-1
            while left < right:
                if nums[left] + nums[right] > x*-1:
                    right -=1
                elif nums[left] + nums[right] < x*-1:
                    left +=1
                else:
                    ans=(x,nums[left],nums[right])
                    
                    res.append(ans)
                    left +=1
                    right -=1
            l+=1
        s = set(res)
        return s