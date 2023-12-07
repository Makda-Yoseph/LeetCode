class Solution(object):
    def multiply(self, num1, num2):
        num={'0':0,'1':1,'2':2,'3':3 ,'4':4 ,'5':5 ,'6':6 ,'7':7 ,'8':8 ,'9':9}
        m1,m2 = len(num1),len(num2)
        x,y = 0,0
        for i in range(len(num1)):
            x += num[num1[i]] * 10**(m1-1)
            m1 -=1
        for i in range(len(num2)):
            y += num[num2[i]] * 10**(m2-1)
            m2 -= 1
        
        return str(x*y)

        
        
            