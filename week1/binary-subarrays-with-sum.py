class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = 0
        prefix = []
        occur = {0:1}
        count = 0
        for i in range(0,len(nums)):
            pre += nums[i]
            prefix.append(pre)
            if prefix[i]-goal in occur:
                count +=occur[prefix[i]-goal]
            occur[prefix[i]]= occur.get(prefix[i],0) +1

        return count