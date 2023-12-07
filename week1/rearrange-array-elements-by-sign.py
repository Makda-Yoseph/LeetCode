class Solution(object):
    def rearrangeArray(self, nums):
        p = []
        n = []
        num = []

        for i in nums:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)

        for j in range(len(nums) // 2):
            num.append(p[j])
            num.append(n[j])

        return num