class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        t = len(nums)-1
        ans = 0
        while t>0:
            r = t-1
            l = 0
            while l<r:
                if nums[l]+nums[r]>nums[t]:
                    ans += r-l
                    r-=1
                else:
                    l+=1
            t-=1
        return ans
                

