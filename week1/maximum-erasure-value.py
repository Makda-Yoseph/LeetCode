class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l ,r,s ,m = 0,0,0,0
        occur = {}
        while r<len(nums):
            occur[nums[r]] = occur.get(nums[r],0)+1
            if occur[nums[r]] == 2:
                s = sum(occur.keys())
                m = max(s,m)
                while occur[nums[r]] ==2:
                    occur[nums[l]] -=1
                    if occur[nums[l]] ==0:
                        del occur[nums[l]]
                    l+=1
            r+=1
        s = sum(occur.keys())
        m = max(m,s)
        return m

        