class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,ma ,ct = 0,0,0,0
        while r <len(nums):
            if ct <= k:
                if nums[r] == 0:
                    ct +=1
                if ct >k:
                    d = r-l
                    ma = max(d,ma)
                    while ct >k:
                        if nums[l] == 0:
                            ct -=1
                        l+=1
            r +=1
            
        d = r-l
        ma = max(ma,d)
        return ma
                

            

            

        