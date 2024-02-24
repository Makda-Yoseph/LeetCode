class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = []
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefix.append(pre)
        print(prefix)
        for i in range(len(nums)):
            prefix[i] = ceil(prefix[i]/(i+1))
        print(prefix)
        return max(prefix)