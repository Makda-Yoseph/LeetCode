class Solution(object):
    def minOperations(self, boxes):
        res = []
        for i in range(len(boxes)):
            s = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    s += abs(i-j)
            res.append(s)
        return res
            
        