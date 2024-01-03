class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # l ,r= 0,1
        # ct = 0
        # while l<len(nums)-1:
        #     if rnums[l]+nums[r] < target:
        #         ct +=1
                
        #     if r ==len(nums)-1:
        #         l +=1
        #         r = l+1
        #     r+=1
        # return ct
        ct = 0
        for i in range(len(nums)-1):
            r = i+1
            while r < len(nums):
                if nums[i]+nums[r] < target:
                    ct +=1
                r +=1
        return ct



        