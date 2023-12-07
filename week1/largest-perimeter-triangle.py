class Solution(object):
    def largestPerimeter(self, nums):
        num = sorted(nums)
        count = 0
        maxp = 0
        for i in range(len(num)-2):
            checker = num[i] +num[i+1] 
            if checker > num[i+2]:
                permi = num[i] +num[i+1] +num[i+2]
                maxp = max(maxp,permi)
        return maxp
                
        
        