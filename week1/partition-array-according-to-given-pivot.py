class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        equal = []
        greater = []
    
        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i< pivot:
                less.append(i)
            else:
                equal.append(i)
        r = less + equal + greater
        
        return r
        