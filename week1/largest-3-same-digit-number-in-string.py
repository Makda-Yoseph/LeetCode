class Solution(object):
    def largestGoodInteger(self, num):
        ans=""
        flag = False
        count = 0
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                ans += num[i:i+3]
                flag = True
        
        if flag == False:
            return ""
        else:
            a = sorted(ans , reverse =True)
            return "".join(a[:3])


