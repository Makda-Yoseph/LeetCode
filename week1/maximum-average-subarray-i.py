class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        s = (sum(nums[l:r]))
        avg = s/k
        m = avg
        while r < len(nums):
            s -=nums[l]
            s += nums[r]
            m = max(m,s/k)
            r +=1
            l+=1

        return(m)
            

        