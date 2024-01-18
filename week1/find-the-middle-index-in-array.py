class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = 0
        prefix = []
        for p in range(len(nums)):
            pre += nums[p]
            prefix.append(pre)
        suff = 0
        suffix = [0]*len(nums)
        l = len(nums)-1
        for s in range(len(nums)):
            suff += nums[l-s]
            suffix[l-s] = suff
        for i in range(len(nums)):
            if suffix[i] == prefix[i]:
                return i
        return -1

            



            