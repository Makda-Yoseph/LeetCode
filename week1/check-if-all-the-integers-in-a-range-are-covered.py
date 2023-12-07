class Solution(object):
    def isCovered(self, ranges, left, right):
        x = set()
        
        for i in range(len(ranges)):
            
            x.update(j for j in range(ranges[i][0],ranges[i][1]+1))
        for k in range(left,right+1):
            if k not in x:
                return False
        return True
            
            