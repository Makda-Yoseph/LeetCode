class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        occur = {0:1}
        prefix = []
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefix.append(pre)
            
            if prefix[i]%k in occur:
                count +=occur[prefix[i]%k]
            occur[prefix[i]%k] = occur.get(prefix[i]%k,0)+1
            # occur[abs(prefix[i])]= occur.get(abs(prefix[i]),0) +1
        print(-1%2)
        return count
        