class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        res =[]
        for key,val in count.items():
            if val > len(nums)//3:
                res.append(key)
        return res