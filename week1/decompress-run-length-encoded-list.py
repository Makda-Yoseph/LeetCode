class Solution(object):
    def decompressRLElist(self, nums):
        res = []
        i = 0
        while i < len(nums):
            s= []
            s.append(nums[i+1])
            s = s*nums[i]
            res.extend(s)
            i +=2
        return res

        