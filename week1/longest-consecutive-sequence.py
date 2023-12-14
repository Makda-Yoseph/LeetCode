class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        maxlen = 0
        for n in num:
            if n-1 not in num:
                l = 1
                while n+1 in num:
                    l+=1
                    n = n+1
                maxlen = max(maxlen,l)
        return maxlen
        