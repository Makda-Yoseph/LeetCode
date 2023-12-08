class Solution(object):
    def largestOddNumber(self, num):
        flag = 0
        for i in range(len(num)-1,-1,-1):
            if int(num[i] ) % 2 != 0:
                flag = 1
                res = num[:i+1]
                break
            else:
                continue
        if flag == 1:
            return res
        else:
            return ""
        