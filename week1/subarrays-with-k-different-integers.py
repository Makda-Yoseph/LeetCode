class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l ,r = 0,0
        occur = {}
        ct = 0
        while r < len(nums):
            occur[nums[r]] = occur.get(nums[r],0) +1
            if len(occur)> k:
                while len(occur)>k:
                    occur[nums[l]] -=1
                    if occur[nums[l]] == 0:
                        del occur[nums[l]]
                    l+=1
            
            ct += r-l+1
            r+=1

        left ,right = 0,0
        occurs = {}
        count = 0
        while right < len(nums):
            occurs[nums[right]] = occurs.get(nums[right],0) +1
            if len(occurs)> k-1:
                while len(occurs)>k-1:
                    occurs[nums[left]] -=1
                    if occurs[nums[left]] == 0:
                        del occurs[nums[left]]
                    left+=1
            
            count += right-left+1
            right+=1
        return ct-count



