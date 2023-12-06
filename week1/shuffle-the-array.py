class Solution(object):
    def shuffle(self, nums, n):
        half1 = nums[:n]
        half2 = nums[n:n*2]
        res = []
        for i in range(n):
            res.append(half1[i])
            res.append(half2[i])
        return res


        