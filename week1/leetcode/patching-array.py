class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target= 1
        r = ans = 0
        while target <= n:
            if r< len(nums) and nums[r]<= target:
                target += nums[r]
                r+=1
            else:
                target *=2
                ans +=1
       
        return ans
            
            